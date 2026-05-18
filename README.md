# Reinforcement-Learning

This project experiments with the `LunarLander-v3` environment from Gymnasium. It includes:

- the original environment
- a custom wrapper with reward shaping
- an optional random-spawn mode for the custom wrapper

## Requirements

Use **Python 3.10-3.13**. `LunarLander` needs the Box2D extras.

## Setup

Create the environment:

```powershell
conda create -n Reinforcement-Learning python=3.13
```

Activate it:

```powershell
conda activate Reinforcement-Learning
```

Install dependencies:

```powershell
python -m pip install gymnasium
python -m pip install swig
python -m pip install "gymnasium[box2d]"
```

If `conda` is not available in PowerShell, run `conda init powershell` once in Anaconda Prompt or Miniconda Prompt, then reopen PowerShell.

## Run

Run the demo:

```powershell
python main.py
```

`main.py` uses a single selector:

```python
ENV_SELECTION = "custom"  # or "original"
```

## Choose the environment in `main.py`

Use `ENV_SELECTION = "original"` to run the unmodified `LunarLander-v3`.

Use `ENV_SELECTION = "custom"` to run the custom wrapper. The custom options live in `CUSTOM_ENV_OPTIONS`:

```python
CUSTOM_ENV_OPTIONS = {
    "render_mode": "human",
    "random_spawn": True,
    "gravity": -10.0,
    "enable_wind": False,
    "wind_power": 15.0,
    "turbulence_power": 1.5,
}
```

## Tweak the custom environment

The custom behavior is defined in `environment_creation.py` inside `CustomLunarLander`.

Change these if you want to diverge from the original environment:

- `gravity`, `enable_wind`, `wind_power`, `turbulence_power` for physics
- `random_spawn` to ignore reset seeds and keep the start state stochastic
- `RewardTweaks` to change the shaped reward

The helper `create_custom_lunar_lander(...)` is the recommended way to build the custom env from code.

Example:

```python
from environment_creation import create_custom_lunar_lander

env = create_custom_lunar_lander(
    render_mode="human",
    random_spawn=True,
    gravity=-8.0,
)
```

## Files to edit

- [main.py](main.py) controls which environment variant is used for a run.
- [environment_creation.py](environment_creation.py) controls the custom environment behavior.