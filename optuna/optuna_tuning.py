from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import optuna
from stable_baselines3 import DQN, PPO
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv, VecEnv

from environment_creation import (
    create_custom_lunar_lander,
    create_original_lunar_lander,
)


def make_env(env_selection: str, render_mode: str | None = None) -> Any:
    if env_selection == "custom":
        return Monitor(create_custom_lunar_lander(render_mode=render_mode))
    if env_selection == "original":
        return Monitor(create_original_lunar_lander(render_mode=render_mode))
    raise ValueError("env_selection must be 'custom' or 'original'")


def make_vec_env(env_selection: str, num_envs: int, *, force_dummy: bool = False) -> VecEnv:
    env_fns = [lambda: make_env(env_selection) for _ in range(num_envs)]
    if force_dummy:
        return DummyVecEnv(env_fns)
    vec_cls = SubprocVecEnv if num_envs > 1 else DummyVecEnv
    return vec_cls(env_fns)


@dataclass
class TrainConfig:
    algo: str
    env_selection: str
    total_timesteps: int
    eval_freq: int
    n_eval_episodes: int
    num_envs: int
    seed: int
    log_dir: Path
    model_dir: Path


class TrialEvalCallback(BaseCallback):
    def __init__(
        self,
        trial: optuna.Trial,
        eval_env: VecEnv,
        eval_freq: int,
        n_eval_episodes: int,
    ) -> None:
        super().__init__()
        self.trial = trial
        self.eval_env = eval_env
        self.eval_freq = eval_freq
        self.n_eval_episodes = n_eval_episodes
        self.best_mean_reward = -np.inf
        self.last_eval_step = 0

    def _on_step(self) -> bool:
        if self.eval_freq <= 0:
            return True
        if self.num_timesteps - self.last_eval_step < self.eval_freq:
            return True
        self.last_eval_step = self.num_timesteps

        mean_reward, _std = evaluate_policy(
            self.model,
            self.eval_env,
            n_eval_episodes=self.n_eval_episodes,
            deterministic=True,
        )
        self.trial.report(mean_reward, step=self.num_timesteps)

        if mean_reward > self.best_mean_reward:
            self.best_mean_reward = mean_reward

        if self.trial.should_prune():
            raise optuna.TrialPruned()

        return True


# ── PPO v3 ────────────────────────────────────────────────────────────────────
#
# Manual grid search findings (original env, 1M steps):
#   lr:         1e-3 → 277.56,  3e-3 → 275.25,  3e-4 baseline → 232.78
#               → keep [3e-4, 3e-3]; baseline was already solid
#   n_steps:    2048 → 247.87,  1024 → 232.78 (baseline),  512 → 176, 256 → 147
#               → focus on [1024, 2048]; 512/256 clearly worse
#   batch_size: 64 → 270.69,  128 → 276.00,  256 → 232.78,  512 → 201.12
#               → small batches win; keep [64, 128, 256] drop 512
#   n_epochs:   20 → 277.06,  10 → baseline,  5 → 160.69
#               → keep [10, 20]; 5 clearly worse
#   gamma:      0.995 → 277.03,  0.99 → 232.78,  0.98 → 173.69,  0.5 → -8.28
#               → keep [0.99, 0.999]; low gamma kills performance
#   gae_lambda: 0.95 baseline → best; 0.97 → 224, 0.90 → 213
#               → tighten to [0.93, 0.97]
#   clip_range: 0.1 → 261, 0.2 → 232 (baseline), 0.3 → 268
#               → full range [0.1, 0.3] still useful
#   ent_coef:   0.0 baseline → 232, 0.01 → 251, 0.05 → 255, 0.1 → 207
#               → [0.0, 0.05]; above 0.05 hurts
#   vf_coef:    0.3 → 269, 0.5 → 232 (baseline), 0.7 → 271
#               → [0.3, 0.8]; higher vf_coef seems fine
#   max_grad_norm: only 0.5 tested; keep [0.3, 1.0]
#
# Key insight: PPO is very competitive with DQN at 1M steps and closes the gap
# fast with timesteps. At 5M it already hits 270; best combo of lr/epochs/batch
# could push above 280 at 1M.
def sample_ppo_params(trial: optuna.Trial) -> dict:
    return {
        # 1e-3 and 3e-3 both outperformed the 3e-4 baseline
        "learning_rate": trial.suggest_float("learning_rate", 3e-4, 3e-3, log=True),

        # 0.995 matched 0.99 best; anything below 0.99 collapses
        "gamma": trial.suggest_float("gamma", 0.99, 0.999),

        # 256 and 512 underperformed; 1024/2048 consistently better
        "n_steps": trial.suggest_categorical("n_steps", [1024, 2048]),

        # Smaller batches win; 512 clearly worse
        "batch_size": trial.suggest_categorical("batch_size", [64, 128, 256]),

        # 20 epochs improved; 5 clearly worse
        "n_epochs": trial.suggest_categorical("n_epochs", [10, 20]),

        # Full range still useful; no clear winner
        "clip_range": trial.suggest_float("clip_range", 0.1, 0.3),

        # 0.95 baseline best; tighten range around it
        "gae_lambda": trial.suggest_float("gae_lambda", 0.93, 0.98),

        # Small ent_coef helps; above 0.05 hurts
        "ent_coef": trial.suggest_float("ent_coef", 0.0, 0.05),

        # Higher vf_coef seems fine (0.7 → 271)
        "vf_coef": trial.suggest_float("vf_coef", 0.3, 0.8),

        "max_grad_norm": trial.suggest_float("max_grad_norm", 0.3, 1.0),
    }


# ── DQN v3 ────────────────────────────────────────────────────────────────────
#
# Combining manual grid search + Optuna run 1. These two data sources partially
# DISAGREE — here is how to reconcile them:
#
# Manual grid search (1M steps, lr=1e-3 anchor, grad_steps=1 throughout):
#   lr:               1e-3 → 247 (baseline), 3e-3 → 247, 1e-4 → 44, 3e-4 → -70
#                     → lr must be ≥ 1e-3; low lr is harmful at grad_steps=1
#   batch_size:       128 → 271.45 ★ best 1M result, 64 → 247, 256 → 226
#                     → 128 is the sweet spot at lr=1e-3
#   learning_starts:  10k → 247 (baseline), 5k → 226, 50k → -48
#                     → 50k is BAD at lr=1e-3 + grad_steps=1 (not enough gradient steps)
#   train_freq:       1 → best, 5 → 87, 10 → -12
#                     → train_freq=1 confirmed
#   gradient_steps:   1 → 247 (baseline), 5 → 237, 10 → 211
#                     → grad_steps=1 better than 5/10 AT lr=1e-3
#   exploration_frac: 0.1 → 247 baseline, 0.05 → 151, 0.2 → 123, 0.3 → 173
#                     → 0.1 is clearly best; wider exploration hurts at 1M
#   exploration_eps:  0.05 → 247 baseline, 0.01 → 94, 0.1 → 6, 0.2 → 214
#                     → 0.05 is best; very low eps causes instability
#   target_update:    1000 → 247, 500 → 220, 5000 → 181
#                     → 1000 confirmed best
#   buffer_size:      100k → 244, 1M → 247, 10M → 247  → doesn't matter much
#   gamma:            0.99 → 247, 0.995 → 195, 0.98 → 107  → 0.99 is best
#
# Reconciliation — why Optuna best trial used lr=5e-5 + learning_starts=50k:
#   At grad_steps=5 with a tiny lr, 50k warmup gives the buffer time to fill
#   with diverse transitions before the slow learning begins. It's a different
#   regime from the manual runs (which used grad_steps=1 + lr=1e-3).
#   The question is: which regime scales better to 5M steps?
#   Manual "Best original run" answers this: lr=1e-3, batch=128, grad_steps=1,
#   learning_starts=10k, 5M steps → 280.60. That IS the target.
#
# v3 strategy: search around the confirmed best regime, not the Optuna outlier.
#   Core anchor: lr≈1e-3, batch=128, grad_steps=1, learning_starts=10k
#   Search: lr [5e-4, 3e-3], batch [64,128,256], grad_steps [1,2],
#           learning_starts [5k,10k], exploration more conservative,
#           also include grad_steps=5 with lower lr as an alternative regime
#           so Optuna can decide which is better at the eval budget.
def sample_dqn_params(trial: optuna.Trial) -> dict:
    # Two regimes, let Optuna pick:
    #   "fast"  — high lr + low grad_steps (confirmed by manual search Best Run)
    #   "slow"  — low lr + high grad_steps (Optuna run 1 best trial)
    # We encode this as a categorical choice so Optuna tracks it cleanly.
    regime = trial.suggest_categorical("regime", ["fast", "slow"])

    if regime == "fast":
        learning_rate = trial.suggest_float("lr_fast", 5e-4, 3e-3, log=True)
        gradient_steps = trial.suggest_categorical("gs_fast", [1, 2])
        learning_starts = trial.suggest_categorical("ls_fast", [5_000, 10_000])
        exploration_fraction = trial.suggest_float("ef_fast", 0.08, 0.15)
        exploration_final_eps = trial.suggest_float("efe_fast", 0.03, 0.07)
    else:  # slow
        learning_rate = trial.suggest_float("lr_slow", 1e-5, 2e-4, log=True)
        gradient_steps = trial.suggest_categorical("gs_slow", [5, 8])
        learning_starts = 50_000
        exploration_fraction = trial.suggest_float("ef_slow", 0.20, 0.35)
        exploration_final_eps = trial.suggest_float("efe_slow", 0.03, 0.07)

    return {
        "learning_rate": learning_rate,
        # 0.99 best in manual search; Optuna top trials used 0.975–0.988
        "gamma": trial.suggest_float("gamma", 0.985, 0.999),
        # 128 → best 1M result; 256 also appeared in Optuna winners
        "batch_size": trial.suggest_categorical("batch_size", [128, 256]),
        # Doesn't significantly matter (100k–10M all ~same); fix to 1M
        "buffer_size": 1_000_000,
        "learning_starts": learning_starts,
        # train_freq=1 confirmed across both data sources
        "train_freq": 1,
        "gradient_steps": gradient_steps,
        # 1000 best in manual search
        "target_update_interval": trial.suggest_categorical(
            "target_update_interval", [500, 1000, 2000]
        ),
        "exploration_fraction": exploration_fraction,
        "exploration_final_eps": exploration_final_eps,
        # Manual baseline used 10.0; Optuna winners ~6–9; keep wide
        "max_grad_norm": trial.suggest_float("max_grad_norm", 5.0, 12.0),
    }


def objective(
    trial: optuna.Trial,
    cfg: TrainConfig,
    *,
    force_dummy: bool,
    device: str,
) -> float:
    train_env = make_vec_env(cfg.env_selection, cfg.num_envs, force_dummy=force_dummy)
    eval_env = make_vec_env(cfg.env_selection, 1, force_dummy=force_dummy)

    if cfg.algo == "ppo":
        params = sample_ppo_params(trial)
        model = PPO(
            "MlpPolicy",
            train_env,
            seed=cfg.seed,
            verbose=0,
            device=device,
            **params,
        )
    elif cfg.algo == "dqn":
        params = sample_dqn_params(trial)
        model = DQN(
            "MlpPolicy",
            train_env,
            seed=cfg.seed,
            verbose=0,
            device=device,
            **params,
        )
    else:
        raise ValueError("algo must be 'ppo' or 'dqn'")

    callback = TrialEvalCallback(
        trial=trial,
        eval_env=eval_env,
        eval_freq=cfg.eval_freq,
        n_eval_episodes=cfg.n_eval_episodes,
    )

    model.learn(total_timesteps=cfg.total_timesteps, callback=callback)

    mean_reward, _std = evaluate_policy(
        model,
        eval_env,
        n_eval_episodes=cfg.n_eval_episodes,
        deterministic=True,
    )

    train_env.close()
    eval_env.close()

    return float(mean_reward)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", choices=["ppo", "dqn"], default="ppo")
    parser.add_argument("--env", choices=["original", "custom"], default="original")
    parser.add_argument("--trials", type=int, default=20)
    parser.add_argument("--timesteps", type=int, default=1_000_000)
    parser.add_argument("--eval-freq", type=int, default=100_000)
    parser.add_argument("--eval-episodes", type=int, default=20)
    parser.add_argument("--num-envs", type=int, default=8)
    parser.add_argument("--n-jobs", type=int, default=1)
    parser.add_argument("--force-dummy", action="store_true")
    parser.add_argument("--device", choices=["cpu", "cuda", "auto"], default="auto")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    log_dir = Path("runs") / "optuna" / f"{args.env}_{args.algo}"
    model_dir = Path("runs") / "optuna" / "best_model"
    log_dir.mkdir(parents=True, exist_ok=True)
    model_dir.mkdir(parents=True, exist_ok=True)

    cfg = TrainConfig(
        algo=args.algo,
        env_selection=args.env,
        total_timesteps=args.timesteps,
        eval_freq=args.eval_freq,
        n_eval_episodes=args.eval_episodes,
        num_envs=args.num_envs,
        seed=args.seed,
        log_dir=log_dir,
        model_dir=model_dir,
    )

    # n_warmup_steps=3: let 3 evals complete before pruning kicks in.
    # With eval_freq=100k and timesteps=1M that means ~300k steps before any
    # trial can be pruned — enough to distinguish good from bad.
    pruner = optuna.pruners.MedianPruner(n_warmup_steps=3)
    study = optuna.create_study(direction="maximize", pruner=pruner)

    if args.device == "auto":
        try:
            import torch
            device = "cuda" if torch.cuda.is_available() else "cpu"
        except Exception:
            device = "cpu"
    else:
        device = args.device

    study.optimize(
        lambda t: objective(t, cfg, force_dummy=args.force_dummy, device=device),
        n_trials=args.trials,
        n_jobs=args.n_jobs,
    )

    print("Best trial:")
    print(study.best_trial)

    best_params = study.best_trial.params
    # Strip the internal regime key before passing to the model constructor
    best_params.pop("regime", None)
    # Rename regime-scoped keys back to their canonical SB3 names
    for prefix in ("lr_fast", "lr_slow"):
        if prefix in best_params:
            best_params["learning_rate"] = best_params.pop(prefix)
    for prefix in ("gs_fast", "gs_slow"):
        if prefix in best_params:
            best_params["gradient_steps"] = best_params.pop(prefix)
    for prefix in ("ls_fast",):
        if prefix in best_params:
            best_params["learning_starts"] = best_params.pop(prefix)
    for prefix in ("ef_fast", "ef_slow"):
        if prefix in best_params:
            best_params["exploration_fraction"] = best_params.pop(prefix)
    for prefix in ("efe_fast", "efe_slow"):
        if prefix in best_params:
            best_params["exploration_final_eps"] = best_params.pop(prefix)
    # learning_starts is fixed for slow regime — add it back if missing
    if "learning_starts" not in best_params:
        best_params["learning_starts"] = 50_000

    train_env = make_vec_env(cfg.env_selection, cfg.num_envs, force_dummy=args.force_dummy)
    if cfg.algo == "ppo":
        model = PPO(
            "MlpPolicy",
            train_env,
            seed=cfg.seed,
            verbose=0,
            device=device,
            **best_params,
        )
    else:
        model = DQN(
            "MlpPolicy",
            train_env,
            seed=cfg.seed,
            verbose=0,
            device=device,
            **best_params,
        )

    model.learn(total_timesteps=cfg.total_timesteps)
    model.save(model_dir / f"best_{cfg.env_selection}_{cfg.algo}")
    train_env.close()


if __name__ == "__main__":
    main()