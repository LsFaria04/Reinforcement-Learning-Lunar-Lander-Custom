from __future__ import annotations

from dataclasses import dataclass

import gymnasium as gym
from gymnasium.envs.registration import register, registry


CUSTOM_ENV_ID = "CustomLunarLander-v0"


@dataclass
class RewardTweaks:
    distance_penalty: float = 1.0
    velocity_penalty: float = 1.0
    angle_penalty: float = 1.0
    contact_bonus: float = 0.0
    landing_bonus: float = 0.0
    crash_penalty: float = 0.0


class CustomLunarLander(gym.Env):
    """Editable local copy of LunarLander for assignment experiments."""

    def __init__(
        self,
        render_mode: str | None = None,
        continuous: bool = False,
        gravity: float = -10.0,
        enable_wind: bool = False,
        wind_power: float = 15.0,
        turbulence_power: float = 1.5,
        reward_tweaks: RewardTweaks | None = None,
    ):
        try:
            self.env = gym.make(
                "LunarLander-v3",
                render_mode=render_mode,
                continuous=continuous,
                gravity=gravity,
                enable_wind=enable_wind,
                wind_power=wind_power,
                turbulence_power=turbulence_power,
            )
        except gym.error.DependencyNotInstalled as exc:
            raise RuntimeError(
                "LunarLander needs the Box2D extras. Use a Python 3.10-3.13 environment and install `gymnasium[box2d]`."
            ) from exc
        self.reward_tweaks = reward_tweaks or RewardTweaks()
        self.action_space = self.env.action_space
        self.observation_space = self.env.observation_space
        self.render_mode = render_mode

    def step(self, action):
        observation, reward, terminated, truncated, info = self.env.step(action)

        x, y, vx, vy, angle, angular_velocity, left_contact, right_contact = observation
        shaped_reward = float(reward)

        shaped_reward -= self.reward_tweaks.distance_penalty * (abs(x) + abs(y))
        shaped_reward -= self.reward_tweaks.velocity_penalty * (abs(vx) + abs(vy))
        shaped_reward -= self.reward_tweaks.angle_penalty * abs(angle)
        shaped_reward += self.reward_tweaks.contact_bonus * (left_contact + right_contact)

        if terminated and reward > 0:
            shaped_reward += self.reward_tweaks.landing_bonus
        elif terminated and reward < 0:
            shaped_reward -= self.reward_tweaks.crash_penalty

        info = dict(info)
        info["base_reward"] = float(reward)
        info["custom_reward"] = shaped_reward
        return observation, shaped_reward, terminated, truncated, info

    def reset(self, *, seed: int | None = None, options: dict | None = None):
        return self.env.reset(seed=seed, options=options)

    def render(self):
        return self.env.render()

    def close(self):
        return self.env.close()

    @property
    def unwrapped(self):
        return self.env.unwrapped


def register_custom_lunar_lander() -> None:
    if CUSTOM_ENV_ID not in registry:
        register(
            id=CUSTOM_ENV_ID,
            entry_point="environment_creation:CustomLunarLander",
            max_episode_steps=1000,
            reward_threshold=200,
        )


register_custom_lunar_lander()
