# Parameters used to test

This file includes the paramters used for each test run. The model results are stored inside the runs folder.

## Original environment

### HyperParameters

#### Baseline

```python
ENV_SELECTION = "original"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 1e-3,
    "buffer_size": 1_000_000,
    "learning_starts": 10_000,
    "batch_size": 64,
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

Evaluated trained agent over 100 episodes: mean reward = 247.27 +/- 65.35

#### Run 1

Chnages number of steps

```python
ENV_SELECTION = "original"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 500_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 1e-3,
    "buffer_size": 1_000_000,
    "learning_starts": 10_000,
    "batch_size": 64,
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
Evaluated trained agent over 100 episodes: mean reward = 123.38 +/- 123.28

#### Run 2

Chnages number of steps

```python
ENV_SELECTION = "original"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 5_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 1e-3,
    "buffer_size": 1_000_000,
    "learning_starts": 10_000,
    "batch_size": 64,
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

Evaluated trained agent over 100 episodes: mean reward = 275.07 +/- 42.68

#### Run 3

Chnages number of steps

```python
ENV_SELECTION = "original"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 10_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 1e-3,
    "buffer_size": 1_000_000,
    "learning_starts": 10_000,
    "batch_size": 64,
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

Evaluated trained agent over 100 episodes: mean reward = 260.72 +/- 72.39

#### Run 4

Changes the learning rate

```python
ENV_SELECTION = "original"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 1e-4,
    "buffer_size": 1_000_000,
    "learning_starts": 10_000,
    "batch_size": 64,
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

Evaluated trained agent over 100 episodes: mean reward = 44.77 +/- 80.29

#### Run 5

Changes the learning rate

```python
ENV_SELECTION = "original"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 3e-4,
    "buffer_size": 1_000_000,
    "learning_starts": 10_000,
    "batch_size": 64,
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

Evaluated trained agent over 100 episodes: mean reward = -70.50 +/- 36.78

#### Run 6

Changes the learning rate

```python
ENV_SELECTION = "original"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 3e-3,
    "buffer_size": 1_000_000,
    "learning_starts": 10_000,
    "batch_size": 64,
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

Evaluated trained agent over 100 episodes: mean reward = 247.63 +/- 35.74

#### Run 7

Changes the learning_starts

```python
ENV_SELECTION = "original"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 1e-3,
    "buffer_size": 1_000_000,
    "learning_starts": 5_000,
    "batch_size": 64,
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

Evaluated trained agent over 100 episodes: mean reward = 226.21 +/- 41.28

#### Run 8

Changes the learning_starts

```python
ENV_SELECTION = "original"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 1e-3,
    "buffer_size": 1_000_000,
    "learning_starts": 50_000,
    "batch_size": 64,
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

Evaluated trained agent over 100 episodes: mean reward = -48.50 +/- 75.83

#### Run 9
 changes train freq and gradient steps
