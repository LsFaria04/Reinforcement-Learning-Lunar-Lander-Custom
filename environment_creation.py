from __future__ import annotations
from dataclasses import dataclass
from gymnasium.envs.registration import register, registry

import gymnasium as gym
import numpy as np


BASE_ENV_ID = "LunarLander-v3"
CUSTOM_ENV_ID = "CustomLunarLander-v0"
VIEWPORT_W = 600.0
VIEWPORT_H = 400.0
SCALE = 30.0
FPS = 50.0
LEG_DOWN = 18.0

BASE_ENV_KWARGS = {
    "render_mode": None,
    "continuous": False,
    "gravity": -10.0,
    "enable_wind": False,
    "wind_power": 15.0,
    "turbulence_power": 1.5,
}

CUSTOM_ENV_DEFAULTS = {
    "render_mode": None,
    "continuous": False,
    "gravity": -10.0,
    "enable_wind": False,
    "wind_power": 15.0,
    "turbulence_power": 1.5,
    "random_spawn": True,
    "random_spawn_x_range": (-0.9, 0.9), # Add stronger horizontal spawn range
}


@dataclass
class RewardTweaks:
    distance_penalty: float = 0.0
    velocity_penalty: float = 0.0
    angle_penalty: float = 0.0
    contact_bonus: float = 0.0
    landing_bonus: float = 0.0
    crash_penalty: float = 0.0
    fuel_bonus: float = 0.0


def _make_lunar_lander(
    *,
    render_mode: str | None,
    continuous: bool,
    gravity: float,
    enable_wind: bool,
    wind_power: float,
    turbulence_power: float,
) -> gym.Env:
    try:
        return gym.make(
            BASE_ENV_ID,
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


class CustomLunarLander(gym.Env):
    """Editable local copy of LunarLander for assignment experiments.

    The environment behavior is controlled here, while `main.py` only decides
    which factory to call and which options to pass.
    """

    def __init__(
        self,
        render_mode: str | None = None,
        continuous: bool = False,
        gravity: float = -10.0,
        enable_wind: bool = False,
        wind_power: float = 15.0,
        turbulence_power: float = 1.5,
        random_spawn: bool = False,
        random_spawn_x_range: tuple[float, float] = (-0.6, 0.6),
        reward_tweaks: RewardTweaks | None = None,
        noise_std: float = 0.1,
        max_fuel: int = 300,
    ):
        self.env = _make_lunar_lander(
            render_mode=render_mode,
            continuous=continuous,
            gravity=gravity,
            enable_wind=enable_wind,
            wind_power=wind_power,
            turbulence_power=turbulence_power,
        )
        self.reward_tweaks = reward_tweaks or RewardTweaks()
        self.random_spawn = random_spawn
        self.random_spawn_x_range = random_spawn_x_range
        self.action_space = self.env.action_space
        self.observation_space = self.env.observation_space
        self.render_mode = render_mode
        self.noise_std = noise_std
        self.max_fuel = float(max_fuel)
        self.fuel = self.max_fuel
        self.main_engine_cost = 1.0
        self.side_engine_cost = 0.3
        self._init_observation_space()

    def _init_observation_space(self) -> None:
        base_space = self.env.observation_space
        if not isinstance(base_space, gym.spaces.Box):
            raise TypeError("CustomLunarLander expects a Box observation space")

        low = np.concatenate([base_space.low, np.array([0.0], dtype=base_space.dtype)])
        high = np.concatenate([base_space.high, np.array([1.0], dtype=base_space.dtype)])
        self.observation_space = gym.spaces.Box(low=low, high=high, dtype=base_space.dtype)

    def _shape_reward(
        self,
        observation,
        reward: float,
        terminated: bool,
        done: bool,
    ) -> float:
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

        if done and self.max_fuel > 0:
            fuel_ratio = self.fuel / self.max_fuel
            shaped_reward += self.reward_tweaks.fuel_bonus * fuel_ratio

        return shaped_reward

    def _add_observation_noise(self, observation):
        observation = np.asarray(observation, dtype=np.float32).copy()

        if self.noise_std <= 0:
            return observation

        # Add noise only to continuous state variables:
        # x, y, vx, vy, angle, angular_velocity
        continuous_indices = [0, 1, 2, 3, 4, 5]

        observation[continuous_indices] += self.env.unwrapped.np_random.normal(
            loc=0.0,
            scale=self.noise_std,
            size=len(continuous_indices),
        )

        # Keep leg-contact indicators exactly binary.
        observation[6] = float(observation[6] >= 0.5)
        observation[7] = float(observation[7] >= 0.5)

        return observation

    def _append_fuel(self, observation):
        observation = np.asarray(observation, dtype=np.float32)
        if self.max_fuel <= 0:
            fuel_ratio = 0.0
        else:
            fuel_ratio = float(self.fuel / self.max_fuel)
        return np.append(observation, fuel_ratio)


    def step(self, action):
        fuel_cost = 0.0

        if self.env.unwrapped.continuous:
            main_throttle = float(np.clip(action[0], 0.0, 1.0))
            side_throttle = float(np.clip(abs(action[1]), 0.0, 1.0))
            fuel_cost = (main_throttle * self.main_engine_cost) + (
                side_throttle * self.side_engine_cost
            )
        else:
            if action == 2:  # main engine
                fuel_cost = self.main_engine_cost
            elif action in [1, 3]:  # side engines
                fuel_cost = self.side_engine_cost

        self.fuel = max(0.0, self.fuel - fuel_cost)

        if self.fuel <= 0:
            if self.env.unwrapped.continuous:
                action = np.array([0.0, 0.0], dtype=np.float32)
            else:
                action = 0

        observation, reward, terminated, truncated, info = self.env.step(action)
        observation = self._add_observation_noise(observation)
        done = terminated or truncated
        shaped_reward = self._shape_reward(observation, reward, terminated, done)

        info = dict(info)
        info["base_reward"] = float(reward)
        info["custom_reward"] = shaped_reward
        observation = self._append_fuel(observation)
        return observation, shaped_reward, terminated, truncated, info

    def reset(self, *, seed: int | None = None, options: dict | None = None):
        self.fuel = self.max_fuel
        # If random_spawn is enabled, always ignore seed to force stochastic resets.
        if self.random_spawn:
            _, info = self.env.reset(options=options)
            self._apply_random_x_spawn()
            return self._append_fuel(self._get_state()), info

        # Otherwise respect the provided seed when present.
        if seed is None:
            observation, info = self.env.reset(options=options)
        else:
            observation, info = self.env.reset(seed=seed, options=options)

        return self._append_fuel(observation), info

    def _apply_random_x_spawn(self) -> None:
        base_env = self.env.unwrapped
        if base_env.lander is None or not getattr(base_env, "legs", None):
            return

        low, high = self.random_spawn_x_range
        center_x = VIEWPORT_W / SCALE / 2.0
        offset_x = base_env.np_random.uniform(low=low, high=high) * center_x

        bodies = [base_env.lander, *base_env.legs]
        for body in bodies:
            body.position = (body.position.x + offset_x, body.position.y)

    def _get_state(self):
        base_env = self.env.unwrapped
        pos = base_env.lander.position
        vel = base_env.lander.linearVelocity
        return [
            (pos.x - VIEWPORT_W / SCALE / 2.0) / (VIEWPORT_W / SCALE / 2.0),
            (pos.y - (base_env.helipad_y + LEG_DOWN / SCALE)) / (VIEWPORT_H / SCALE / 2.0),
            vel.x * (VIEWPORT_W / SCALE / 2.0) / FPS,
            vel.y * (VIEWPORT_H / SCALE / 2.0) / FPS,
            base_env.lander.angle,
            20.0 * base_env.lander.angularVelocity / FPS,
            1.0 if base_env.legs[0].ground_contact else 0.0,
            1.0 if base_env.legs[1].ground_contact else 0.0,
        ]

    def render(self):
        render_result = self.env.render()

        if self.render_mode == "human":
            try:
                import pygame
            except Exception:
                return render_result

            base_env = self.env.unwrapped
            screen = getattr(base_env, "screen", None)
            if screen is None:
                return render_result

            font = pygame.font.Font(None, 24)
            fuel_text = font.render(f"Fuel: {int(self.fuel)}", True, (255, 255, 255))
            screen.blit(fuel_text, (10, 10))
            pygame.display.flip()

        return render_result

    def close(self):
        return self.env.close()

    @property
    def unwrapped(self):
        return self.env.unwrapped


def register_custom_lunar_lander() -> None:
    """Register the custom env once for gym.make()."""
    if CUSTOM_ENV_ID not in registry:
        register(
            id=CUSTOM_ENV_ID,
            entry_point="environment_creation:CustomLunarLander",
            max_episode_steps=1000,
            reward_threshold=200,
        )


register_custom_lunar_lander()


def create_original_lunar_lander(render_mode: str | None = None) -> gym.Env:
    """Create the unmodified LunarLander baseline environment."""
    env_kwargs = dict(BASE_ENV_KWARGS)
    env_kwargs["render_mode"] = render_mode
    return gym.make(BASE_ENV_ID, **env_kwargs)


def create_custom_lunar_lander(
    *,
    render_mode: str | None = None,
    continuous: bool = False,
    gravity: float = -10.0,
    enable_wind: bool = False,
    wind_power: float = 15.0,
    turbulence_power: float = 1.5,
    random_spawn: bool = True,
    random_spawn_x_range: tuple[float, float] = (-0.9, 0.9),
    reward_tweaks: RewardTweaks | None = None,
    noise_std: float = 0.1,
) -> CustomLunarLander:
    return CustomLunarLander(
        render_mode=render_mode,
        continuous=continuous,
        gravity=gravity,
        enable_wind=enable_wind,
        wind_power=wind_power,
        turbulence_power=turbulence_power,
        random_spawn=random_spawn,
        random_spawn_x_range=random_spawn_x_range,
        reward_tweaks=reward_tweaks,
        noise_std=noise_std,
    )
