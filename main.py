import gymnasium as gym

env = gym.make(
    "LunarLander-v3",
    render_mode="human",
    continuous=False,
    gravity=-10.0,
    enable_wind=False,
    wind_power=15.0,
    turbulence_power=1.5,
)

observation, info = env.reset(seed=42)
episode_reward = 0.0
episode = 1

for _ in range(1000):
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