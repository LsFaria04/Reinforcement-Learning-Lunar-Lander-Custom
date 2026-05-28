from functools import partial

import gymnasium as gym
import numpy as np
import torch
from stable_baselines3 import DQN, PPO
from stable_baselines3.common.base_class import BaseAlgorithm
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv, VecEnv

from environment_creation import (
    create_custom_lunar_lander,
    create_original_lunar_lander,
    CUSTOM_ENV_ID,
    RewardTweaks,
)

CUSTOM_ENV_OPTIONS = {
    "render_mode": None,
    "random_spawn": True,
    "gravity": -10.0,
    "enable_wind": False,
    "wind_power": 15.0,
    "turbulence_power": 1.5,
    "random_spawn_x_range": (-0.6, 0.6),
    "noise_std": 0.005, # noise to x, y, vx, vy, and angle observations
    "reward_tweaks": RewardTweaks(fuel_bonus=50.0),
}

ALGORITHM_SELECTION = "dqn"  # Options: "dqn", "ppo"

ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 15
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 5_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 1e-3,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 20,
    "gamma": 0.995,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.01,
    "vf_coef": 0.7,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}

DQN_KWARGS = {
    "learning_rate": 1e-3,
    "buffer_size": 1_000_000,
    "learning_starts": 10_000,
    "batch_size": 128,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1_000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}

ALGORITHM_CONFIGS = {
    "dqn": {
        "cls": DQN,
        "kwargs": DQN_KWARGS,
        "save_path": "dqn_lunar_lander",
    },
    "ppo": {
        "cls": PPO,
        "kwargs": PPO_KWARGS,
        "save_path": "ppo_lunar_lander",
    },
}




def _get_algorithm_config() -> tuple[type[BaseAlgorithm], dict, str]:
    config = ALGORITHM_CONFIGS.get(ALGORITHM_SELECTION)
    if config is None:
        valid = ", ".join(sorted(ALGORITHM_CONFIGS))
        raise ValueError(
            f"Unknown ALGORITHM_SELECTION={ALGORITHM_SELECTION!r}. Use one of: {valid}."
        )
    return config["cls"], config["kwargs"], config["save_path"]


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
    return partial(_make_env, seed=seed, render_mode=render_mode, random_spawn=random_spawn)


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

def train_agent(train_env: VecEnv) -> BaseAlgorithm:
    """Train an RL agent on the provided environment."""

    cuda_available = False
    try:
        cuda_available = torch.cuda.is_available()
    except RuntimeError as e:
        print(f"Warning: Could not check CUDA availability due to error: {e}")
        print("Defaulting to CPU training.")
    if cuda_available:
        print("CUDA is available")
    device = "cuda" if cuda_available and ALGORITHM_SELECTION == "dqn" else "cpu"
    if device == "cuda":
        print("Training on GPU with CUDA support.")
        print("Your GPU is: ", torch.cuda.get_device_name(0))
        print("CUDA version: ", torch.version.cuda)
    else:
        print("Training on CPU (no CUDA support detected).")
    
    model_cls, algo_kwargs, save_path = _get_algorithm_config()
    model = model_cls(
        "MlpPolicy",
        train_env,
        verbose=0,
        device=device,
        seed=SEED,
        **algo_kwargs,
    )
    model.learn(
        total_timesteps=TOTAL_TIMESTEPS,
        progress_bar=True,
    )

    model.save(save_path)

    return model

def load_agent(model_path: str | None = None) -> BaseAlgorithm:
    """Load a trained RL agent from the specified path."""
    cuda_available = False
    try:
        cuda_available = torch.cuda.is_available()
    except RuntimeError as e:
        print(f"Warning: Could not check CUDA availability due to error: {e}")
        print("Defaulting to CPU loading.")
    device = "cuda" if cuda_available and ALGORITHM_SELECTION == "dqn" else "cpu"
    if device == "cuda":
        print("Loading model on GPU with CUDA support.")
        print("Your GPU is: ", torch.cuda.get_device_name(0))
        print("CUDA version: ", torch.version.cuda)
    else:
        print("Loading model on CPU (no CUDA support detected).")
    
    model_cls, _algo_kwargs, default_path = _get_algorithm_config()
    model = model_cls.load(model_path or default_path, device=device)
    return model

def run_demo(*, train: bool = True, model_path: str | None = None) -> None:
    """Train or load, then evaluate and render a policy against the selected env."""

    set_random_seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)

    train_env = None
    if train:
        train_env = create_vec_env(
            seed=SEED,
            render_mode=None,
            random_spawn=None,
            num_envs=NUM_ENVS,
        )
    eval_env = create_vec_env(
        seed=SEED + 1,
        render_mode=None,
        random_spawn=False,
        num_envs=1,
        use_subproc=False,
    )
    env_name = CUSTOM_ENV_ID if ENV_SELECTION == "custom" else "LunarLander-v3"
    print(f"Using environment: {env_name}")
    print(f"Using algorithm: {ALGORITHM_SELECTION}")
    if ENV_SELECTION == "custom":
        print(f"Custom options: {CUSTOM_ENV_OPTIONS}")

    if train:
        model = train_agent(train_env)
    else:
        model = load_agent(model_path)

    mean_reward, std_reward = evaluate_policy(
        model,
        eval_env,
        n_eval_episodes=EVAL_EPISODES,
        deterministic=True,
    )
    print(
        f"Evaluated trained agent over {EVAL_EPISODES} episodes: mean reward = {mean_reward:.2f} +/- {std_reward:.2f}"
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
    if train_env is not None:
        train_env.close()
    eval_env.close()
    demo_env.close()



if __name__ == "__main__":
    run_demo(train=False, model_path="runs/custom/best_custom_run.zip")