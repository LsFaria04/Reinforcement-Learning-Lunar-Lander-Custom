# Reinforcement-Learning

### Python Version Requirement

This project requires **Python 3.13** or earlier (3.10-3.13).

### To create or update the virtual environment

If you don't have the environment yet, create it with Python 3.13:

```powershell
conda create -n Reinforcement-Learning python=3.13
```

If you already have the environment but it's on Python 3.14, recreate it:

```powershell
conda remove -n Reinforcement-Learning --all
conda create -n Reinforcement-Learning python=3.13
```

### To activate the virtual environment

If you have conda installed and initialized in your shell:

```powershell
conda activate Reinforcement-Learning
```

If `conda` is not recognized, open the Anaconda Prompt or Miniconda Prompt once and run:

```powershell
conda init powershell
```

Then close and reopen PowerShell before running `conda activate Reinforcement-Learning`.

You can also use the Anaconda Prompt or Miniconda Prompt if you prefer not to initialize PowerShell.

### To install the base gymnasium library

Make sure the environment is active first, then run:

```powershell
python -m pip install gymnasium
python -m pip install swig
python -m pip install "gymnasium[box2d]"
```


### To install stable_baselines 3

```powershell
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu132 #Only needed to work with nvidia gpus
pip install 'stable-baselines3[extra]'
```
### To run the project

Run the main demo with LunarLander:

```powershell
python main.py
```

This will open a window showing the agent interacting with the environment.

### Switching Between Original and Custom Environments

**To use the original LunarLander-v3 (unmodified):**

Edit `main.py` and use:
```python
env = gym.make("LunarLander-v3", ...)
```

**To use the custom LunarLander (with reward modifications):**

Edit `main.py` and use:
```python
from environment_creation import CUSTOM_ENV_ID, register_custom_lunar_lander

register_custom_lunar_lander()
env = gym.make(CUSTOM_ENV_ID, ...)
```

### Customizing the Environment

The custom environment reward function is defined in `environment_creation.py`. You can modify rewards by changing the `RewardTweaks` class:

```python
@dataclass
class RewardTweaks:
    distance_penalty: float = 1.0        # Penalty for distance from landing pad
    velocity_penalty: float = 1.0        # Penalty for speed
    angle_penalty: float = 1.0           # Penalty for tilt angle
    contact_bonus: float = 0.0           # Bonus for leg contact with ground
    landing_bonus: float = 0.0           # Bonus for safe landing
    crash_penalty: float = 0.0           # Penalty for crashing
```

**Example: Make landing easier by reducing distance penalty and adding landing bonus:**

```python
@dataclass
class RewardTweaks:
    distance_penalty: float = 0.5        # Reduced from 1.0
    velocity_penalty: float = 1.0
    angle_penalty: float = 1.0
    contact_bonus: float = 0.0
    landing_bonus: float = 50.0          # Added bonus
    crash_penalty: float = 0.0
```

These tweaks are applied in the `step()` method to modify the base reward from the environment.