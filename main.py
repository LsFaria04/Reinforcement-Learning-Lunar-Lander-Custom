from functools import partial

import gymnasium as gym
import numpy as np
import torch
from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv, VecEnv

from environment_creation import (
    create_custom_lunar_lander,
    create_original_lunar_lander,
    CUSTOM_ENV_ID,
)

ENV_SELECTION = "original"  # Set to "original" to use the unmodified environment.

CUSTOM_ENV_OPTIONS = {
    "render_mode": None,
    "random_spawn": True,
    "gravity": -10.0,
    "enable_wind": False,
    "wind_power": 15.0,
    "turbulence_power": 1.5,
}

SEED = 42
NUM_ENVS = 20
NUM_STEPS = 10000
TOTAL_TIMESTEPS = 3_000_000
EVAL_EPISODES = 100

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

def train_agent(train_env: VecEnv) -> DQN:
    """Train an RL agent on the provided environment."""

    cuda_available = False
    try:
        cuda_available = torch.cuda.is_available()
    except RuntimeError as e:
        print(f"Warning: Could not check CUDA availability due to error: {e}")
        print("Defaulting to CPU training.")
    device = "cuda" if cuda_available else "cpu"
    if device == "cuda":
        print("Training on GPU with CUDA support.")
        print("Your GPU is: ", torch.cuda.get_device_name(0))
        print("CUDA version: ", torch.version.cuda)
        torch.backends.cudnn.benchmark = True
        if hasattr(torch, "set_float32_matmul_precision"):
            torch.set_float32_matmul_precision("high")
    else:
        print("Training on CPU (no CUDA support detected).")

    model = DQN(
        "MlpPolicy",
        train_env,
        verbose=0,
        device=device,
        seed=SEED,
        **DQN_KWARGS,
    )
    model.learn(
        total_timesteps=TOTAL_TIMESTEPS,
        progress_bar=True,
    )
    model.save("dqn_lunar_lander")
    return model


def run_demo() -> None:
    """Train, evaluate, and render a policy against the selected LunarLander env."""

    set_random_seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)

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
    if ENV_SELECTION == "custom":
        print(f"Custom options: {CUSTOM_ENV_OPTIONS}")

    model = train_agent(train_env)
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
    train_env.close()
    eval_env.close()
    demo_env.close()


if __name__ == "__main__":
    run_demo()