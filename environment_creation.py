from __future__ import annotations

from dataclasses import dataclass

import gymnasium as gym
from gymnasium.envs.registration import register, registry


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
    "random_spawn_x_range": (-0.6, 0.6),
}


@dataclass
class RewardTweaks:
    distance_penalty: float = 1.0
    velocity_penalty: float = 1.0
    angle_penalty: float = 1.0
    contact_bonus: float = 0.0
    landing_bonus: float = 0.0
    crash_penalty: float = 0.0


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

    def _shape_reward(
        self,
        observation,
        reward: float,
        terminated: bool,
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

        return shaped_reward

    def step(self, action):
        observation, reward, terminated, truncated, info = self.env.step(action)
        shaped_reward = self._shape_reward(observation, reward, terminated)

        info = dict(info)
        info["base_reward"] = float(reward)
        info["custom_reward"] = shaped_reward
        return observation, shaped_reward, terminated, truncated, info

    def reset(self, *, seed: int | None = None, options: dict | None = None):
        # If random_spawn is enabled, always ignore seed to force stochastic resets.
        if self.random_spawn:
            _, info = self.env.reset(options=options)
            self._apply_random_x_spawn()
            return self._get_state(), info

        # Otherwise respect the provided seed when present.
        if seed is None:
            return self.env.reset(options=options)
        return self.env.reset(seed=seed, options=options)

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
        return self.env.render()

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
    reward_tweaks: RewardTweaks | None = None,
) -> CustomLunarLander:
    """Create the custom LunarLander with explicit override points."""
    return CustomLunarLander(
        render_mode=render_mode,
        continuous=continuous,
        gravity=gravity,
        enable_wind=enable_wind,
        wind_power=wind_power,
        turbulence_power=turbulence_power,
        random_spawn=random_spawn,
        reward_tweaks=reward_tweaks,
    )

