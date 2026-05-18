import gymnasium as gym

from environment_creation import (
    create_custom_lunar_lander,
    create_original_lunar_lander,
    CUSTOM_ENV_ID,
)

ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

CUSTOM_ENV_OPTIONS = {
    "render_mode": "human",
    "random_spawn": True,
    "gravity": -10.0,
    "enable_wind": False,
    "wind_power": 15.0,
    "turbulence_power": 1.5,
}

NUM_STEPS = 1000


def create_env() -> gym.Env:
    """Create whichever environment variant is selected for this run."""
    if ENV_SELECTION == "original":
        return create_original_lunar_lander(render_mode="human")

    if ENV_SELECTION == "custom":
        return create_custom_lunar_lander(**CUSTOM_ENV_OPTIONS)

    raise ValueError(
        f"Unknown ENV_SELECTION={ENV_SELECTION!r}. Use 'original' or 'custom'."
    )


def run_demo() -> None:
    """Run a simple random policy against the selected LunarLander env."""

    env = create_env()
    env_name = CUSTOM_ENV_ID if ENV_SELECTION == "custom" else "LunarLander-v3"
    print(f"Using environment: {env_name}")
    if ENV_SELECTION == "custom":
        print(f"Custom options: {CUSTOM_ENV_OPTIONS}")

    observation, info = env.reset()
    episode_reward = 0.0
    episode = 1

    for _ in range(NUM_STEPS):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)
        episode_reward += reward

        if terminated or truncated:
            print(f"Episode {episode} finished with reward {episode_reward:.2f}")
            episode += 1
            episode_reward = 0.0
            observation, info = env.reset()

    print("Finished running LunarLander-v3")
    env.close()


if __name__ == "__main__":
    run_demo()