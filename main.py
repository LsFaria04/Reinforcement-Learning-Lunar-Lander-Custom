from functools import partial
from pathlib import Path
import re

import gymnasium as gym
import numpy as np
import torch
from stable_baselines3 import DQN
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv, VecEnv

from environment_creation import (
    create_custom_lunar_lander,
    create_original_lunar_lander,
    CUSTOM_ENV_ID,
)

# ============================================================
# Run mode
# ============================================================
# "train"  = train from scratch
# "resume" = resume from latest checkpoint if available
# "demo"   = do not train; load existing model/checkpoint and run/evaluate
RUN_MODE = "demo"

# Force CPU even if CUDA exists.
# Set to False if you want to use GPU when available.
FORCE_CPU = True

ENV_SELECTION = "original"

CUSTOM_ENV_OPTIONS = {
    "render_mode": None,
    "random_spawn": True,
    "gravity": -10.0,
    "enable_wind": False,
    "wind_power": 15.0,
    "turbulence_power": 1.5,
}

SEED = 42
NUM_ENVS = 4
NUM_STEPS = 10000
TOTAL_TIMESTEPS = 2_000_000
EVAL_EPISODES = 100

MODEL_DIR = Path("models")
MODEL_PATH = MODEL_DIR / "dqn_lunar_lander.zip"

CHECKPOINT_DIR = Path("checkpoints")
CHECKPOINT_NAME = "dqn_lunar_lander"
CHECKPOINT_EVERY_TIMESTEPS = 50_000

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 1e-3,
    "buffer_size": 1_000_000,
    "learning_starts": 10_000,
    "batch_size": 64,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1_000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}


def _make_env_options(*, render_mode: str | None, random_spawn: bool | None) -> dict:
    if ENV_SELECTION == "custom":
        options = dict(CUSTOM_ENV_OPTIONS)
        options["render_mode"] = render_mode
        if random_spawn is not None:
            options["random_spawn"] = random_spawn
        return options

    if ENV_SELECTION == "original":
        return {"render_mode": render_mode}

    raise ValueError(
        f"Unknown ENV_SELECTION={ENV_SELECTION!r}. Use 'original' or 'custom'."
    )


def _make_env(*, seed: int, render_mode: str | None, random_spawn: bool | None) -> gym.Env:
    if ENV_SELECTION == "original":
        env = create_original_lunar_lander(render_mode=render_mode)
    else:
        env = create_custom_lunar_lander(
            **_make_env_options(render_mode=render_mode, random_spawn=random_spawn)
        )

    env = Monitor(env)
    env.reset(seed=seed)
    env.action_space.seed(seed)
    return env


def _make_env_factory(*, seed: int, render_mode: str | None, random_spawn: bool | None):
    return partial(
        _make_env,
        seed=seed,
        render_mode=render_mode,
        random_spawn=random_spawn,
    )


def create_vec_env(
    *,
    seed: int,
    render_mode: str | None,
    random_spawn: bool | None,
    num_envs: int = 1,
    use_subproc: bool | None = None,
) -> VecEnv:
    if num_envs < 1:
        raise ValueError("num_envs must be >= 1")

    if use_subproc is None:
        use_subproc = num_envs > 1 and render_mode is None

    env_fns = [
        _make_env_factory(
            seed=seed + i,
            render_mode=render_mode,
            random_spawn=random_spawn,
        )
        for i in range(num_envs)
    ]

    vec_env_cls = SubprocVecEnv if use_subproc else DummyVecEnv
    return vec_env_cls(env_fns)


def get_device() -> str:
    if FORCE_CPU:
        print("FORCE_CPU=True, using CPU.")
        return "cpu"

    try:
        cuda_available = torch.cuda.is_available()
    except RuntimeError as e:
        print(f"Warning: Could not check CUDA availability due to error: {e}")
        print("Defaulting to CPU.")
        return "cpu"

    if cuda_available:
        print("Using GPU with CUDA support.")
        print("GPU:", torch.cuda.get_device_name(0))
        print("CUDA version:", torch.version.cuda)

        torch.backends.cudnn.benchmark = True
        if hasattr(torch, "set_float32_matmul_precision"):
            torch.set_float32_matmul_precision("high")

        return "cuda"

    print("Using CPU.")
    return "cpu"


def _extract_step_number(path: Path) -> int:
    match = re.search(rf"{CHECKPOINT_NAME}_(\d+)_steps\.zip$", path.name)
    if not match:
        return -1
    return int(match.group(1))


def find_latest_checkpoint() -> Path | None:
    checkpoint_files = list(CHECKPOINT_DIR.glob(f"{CHECKPOINT_NAME}_*_steps.zip"))

    if not checkpoint_files:
        return None

    checkpoint_files.sort(key=_extract_step_number)
    return checkpoint_files[-1]


def find_replay_buffer_for_checkpoint(checkpoint_path: Path) -> Path | None:
    steps = _extract_step_number(checkpoint_path)
    if steps < 0:
        return None

    replay_buffer_path = CHECKPOINT_DIR / f"{CHECKPOINT_NAME}_replay_buffer_{steps}_steps.pkl"

    if replay_buffer_path.exists():
        return replay_buffer_path

    return None


def create_checkpoint_callback() -> CheckpointCallback:
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)

    # SB3 callback frequency counts VecEnv steps, not total env transitions.
    # With NUM_ENVS=4, one callback step is 4 environment transitions.
    save_freq = max(CHECKPOINT_EVERY_TIMESTEPS // NUM_ENVS, 1)

    return CheckpointCallback(
        save_freq=save_freq,
        save_path=str(CHECKPOINT_DIR),
        name_prefix=CHECKPOINT_NAME,
        save_replay_buffer=True,
        save_vecnormalize=True,
    )


def train_agent(train_env: VecEnv, *, device: str) -> DQN:
    """Train an RL agent from scratch."""

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    model = DQN(
        "MlpPolicy",
        train_env,
        verbose=1,
        device=device,
        seed=SEED,
        **DQN_KWARGS,
    )

    model.learn(
        total_timesteps=TOTAL_TIMESTEPS,
        callback=create_checkpoint_callback(),
        progress_bar=True,
    )

    model.save(str(MODEL_PATH))
    print(f"Saved final model to: {MODEL_PATH}")

    return model


def resume_training(train_env: VecEnv, *, device: str) -> DQN:
    """Resume training from latest checkpoint if possible."""

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    latest_checkpoint = find_latest_checkpoint()

    if latest_checkpoint is None:
        if MODEL_PATH.exists():
            print(f"No checkpoint found. Resuming from final model: {MODEL_PATH}")
            model = DQN.load(str(MODEL_PATH), env=train_env, device=device)
        else:
            print("No checkpoint or final model found. Training from scratch.")
            return train_agent(train_env, device=device)
    else:
        print(f"Loading latest checkpoint: {latest_checkpoint}")
        model = DQN.load(str(latest_checkpoint), env=train_env, device=device)

        replay_buffer_path = find_replay_buffer_for_checkpoint(latest_checkpoint)
        if replay_buffer_path is not None:
            print(f"Loading replay buffer: {replay_buffer_path}")
            model.load_replay_buffer(str(replay_buffer_path))
        else:
            print("No replay buffer found for checkpoint. Continuing without it.")

    model.learn(
        total_timesteps=TOTAL_TIMESTEPS,
        callback=create_checkpoint_callback(),
        progress_bar=True,
        reset_num_timesteps=False,
    )

    model.save(str(MODEL_PATH))
    print(f"Saved final model to: {MODEL_PATH}")

    return model


def load_existing_model(env: VecEnv, *, device: str) -> DQN:
    """Load existing model/checkpoint without training."""

    latest_checkpoint = find_latest_checkpoint()

    if latest_checkpoint is not None:
        print(f"Loading latest checkpoint without training: {latest_checkpoint}")
        return DQN.load(str(latest_checkpoint), env=env, device=device)

    if MODEL_PATH.exists():
        print(f"Loading final model without training: {MODEL_PATH}")
        return DQN.load(str(MODEL_PATH), env=env, device=device)

    raise FileNotFoundError(
        "No trained model found.\n"
        f"Expected either:\n"
        f"  - {MODEL_PATH}\n"
        f"  - checkpoint in {CHECKPOINT_DIR}/\n\n"
        "Set RUN_MODE='train' first to train a model, or RUN_MODE='resume' to resume training."
    )


def run_demo() -> None:
    """Train/load, evaluate, and render a policy against the selected LunarLander env."""

    set_random_seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)

    device = get_device()

    env_name = CUSTOM_ENV_ID if ENV_SELECTION == "custom" else "LunarLander-v3"
    print(f"Using environment: {env_name}")
    print(f"RUN_MODE: {RUN_MODE}")
    print(f"Device: {device}")

    if ENV_SELECTION == "custom":
        print(f"Custom options: {CUSTOM_ENV_OPTIONS}")

    train_env = None
    eval_env = None
    demo_env = None

    try:
        eval_env = create_vec_env(
            seed=SEED + 1,
            render_mode=None,
            random_spawn=False,
            num_envs=1,
            use_subproc=False,
        )

        if RUN_MODE == "train":
            train_env = create_vec_env(
                seed=SEED,
                render_mode=None,
                random_spawn=None,
                num_envs=NUM_ENVS,
            )
            model = train_agent(train_env, device=device)

        elif RUN_MODE == "resume":
            train_env = create_vec_env(
                seed=SEED,
                render_mode=None,
                random_spawn=None,
                num_envs=NUM_ENVS,
            )
            model = resume_training(train_env, device=device)

        elif RUN_MODE == "demo":
            model = load_existing_model(eval_env, device=device)

        else:
            raise ValueError("RUN_MODE must be one of: 'train', 'resume', 'demo'")

        mean_reward, std_reward = evaluate_policy(
            model,
            eval_env,
            n_eval_episodes=EVAL_EPISODES,
            deterministic=True,
        )

        print(
            f"Evaluated agent over {EVAL_EPISODES} episodes: "
            f"mean reward = {mean_reward:.2f} +/- {std_reward:.2f}"
        )

        demo_env = create_vec_env(
            seed=SEED + 2,
            render_mode="human",
            random_spawn=False,
            num_envs=1,
            use_subproc=False,
        )

        observation = demo_env.reset()
        episode_reward = 0.0
        episode = 1

        for _ in range(NUM_STEPS):
            action, _states = model.predict(observation, deterministic=True)
            observation, rewards, dones, infos = demo_env.step(action)
            episode_reward += float(rewards[0])
            demo_env.render()

            if dones[0]:
                print(f"Episode {episode} finished with reward {episode_reward:.2f}")
                episode += 1
                episode_reward = 0.0
                observation = demo_env.reset()

        print("Finished running LunarLander-v3")

    finally:
        if train_env is not None:
            train_env.close()
        if eval_env is not None:
            eval_env.close()
        if demo_env is not None:
            demo_env.close()


if __name__ == "__main__":
    run_demo()