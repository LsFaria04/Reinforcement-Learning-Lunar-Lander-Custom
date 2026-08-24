# Reinforcement-Learning

**Final Grade: 19.8**

This project experiments with the `LunarLander-v3` environment from Gymnasium. It includes:

- the original environment
- a custom environment with random spawning, environment noise and limited fuel including also a new reward for efficient fuel use.

## Requirements

Use **Python 3.10-3.13**. `LunarLander` needs the Box2D extras.

## Setup

Create the environment (we use anaconda but you can use others):

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
python -m pip install seaborn
python -m pip install optuna
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu132 #Only needed to work with nvidia gpus
pip install 'stable-baselines3[extra]'
```

If `conda` is not available in PowerShell, run `conda init powershell` once in Anaconda Prompt or Miniconda Prompt, then reopen PowerShell.

## Run

Run the demo:

```powershell
python main.py
```

## Tweak the setting and choose the environment in `main.py`

Use `ENV_SELECTION = "original"` to run the unmodified `LunarLander-v3`.

Use `ENV_SELECTION = "custom"` to run the custom wrapper. The custom options live in `CUSTOM_ENV_OPTIONS`:

The `CUSTOM_ENV_OPTIONS` allow you to make changes to the custom environment.

The `ALGORITHM_SELECTION` allows you to choose the algoritm you want to run. The options available are "dqn" and "ppo"

The PPO_KWARGS and the DQN_KWARGS can be used to change the algorithms hyperparameters.

`SEED` is used to create a reproducible seed

`NUM_ENVS` is used to determine the number of environments that will be run in parallel during the training. Be careful with this setting because it can lead to huge RAM consumption in your PC.

`TOTAL_TIMESTEPS`is the number of training steps that will be used in the training phase.

`NUM_STEPS`is the number of steps that will be shown on the screen when the training ends or when a run is loaded

`EVAL_EPISODES` is the number of episodes that will be used to evaluate the performance of the run.

`CHECKPOINT_PCTS`lets you choose checkpoints for the training model. This means that it will save the a checkpoint of the model for when a percentage os steps is achieved.

```python
CUSTOM_ENV_OPTIONS = {
    "render_mode": "human",
    "random_spawn": True,
    "gravity": -10.0,
    "enable_wind": False,
    "wind_power": 15.0,
    "turbulence_power": 1.5,
}

ALGORITHM_SELECTION = "ppo"  # Options: "dqn", "ppo"

ENV_SELECTION = "original"  # Set to "original" to use the unmodified environment.
RUN_BEST_SUITE = False

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100
CHECKPOINT_PCTS = (5, 10,25,50, 100)

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
```

## Run Pre trained models

To quickly see results, some runs where previouly trained and stored inside the `/runs` folder. Each run uses the parameters stored in the files [CUSTOM_PARAMETERS.md](CUSTOM_PARAMETERS.md) and [PARAMETERS.md](PARAMETERS.md).

Inside the main.py file, change train to FALSE and provide the model path to the model you want to load.

```python
if __name__ == "__main__":
    run_demo(train=False, model_path="runs/checkpoints/original_ppo/original_ppo_100pct")
```
