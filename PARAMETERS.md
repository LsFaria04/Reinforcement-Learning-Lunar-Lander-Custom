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

Changes Train freq

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
    "train_freq": 5,
    "gradient_steps": 1,
    "target_update_interval": 1_000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 87.40 +/- 97.66

#### Run 10

Changes Train freq

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
    "train_freq": 10,
    "gradient_steps": 1,
    "target_update_interval": 1_000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = -12.32 +/- 99.20

#### Run 11

Changes gradient steps

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
    "gradient_steps": 5,
    "target_update_interval": 1_000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 237.46 +/- 57.82

#### Run 12

Changes gradient steps

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
    "gradient_steps": 10,
    "target_update_interval": 1_000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}

```

Evaluated trained agent over 100 episodes: mean reward = 211.92 +/- 105.88

#### Run 13

Changes exploration fraction

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
    "exploration_fraction": 0.05,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 151.15 +/- 42.55

#### Run 14

Changes exploration fraction

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
    "exploration_fraction": 0.2,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 123.75 +/- 91.71

#### Run 15

Changes exploration fraction

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
    "exploration_fraction": 0.3,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 173.75 +/- 58.79

#### Run 16

Changes exploration final_eps

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
    "exploration_final_eps": 0.01,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 94.99 +/- 137.95

#### Run 17

Changes exploration final_eps

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
    "exploration_final_eps": 0.1,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 6.01 +/- 84.11

#### Run 18

Changes exploration final_eps

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
    "exploration_final_eps": 0.2,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 214.07 +/- 64.59

#### Run 19

Changes buffer size

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
    "buffer_size": 100_000,
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

Evaluated trained agent over 100 episodes: mean reward = 244.79 +/- 52.89

#### Run 20

Changes buffer size

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
    "buffer_size": 10_000_000,
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

#### Run 21

Changes batch size

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

Evaluated trained agent over 100 episodes: mean reward = 271.45 +/- 23.14

#### Run 22

Changes batch size

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
    "batch_size": 256,
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

Evaluated trained agent over 100 episodes: mean reward = 226.05 +/- 104.15

#### Run 23

Changes target update interval

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
    "target_update_interval": 500,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 220.15 +/- 107.22

#### Run 24

Changes target update interval

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
    "target_update_interval": 5000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 181.62 +/- 97.82

#### Run 25

Changes tau

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
    "tau": 0.5,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 5000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 217.31 +/- 71.58

#### Run 26

Changes tau

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
    "tau": 0.1,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 5000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = -16.62 +/- 95.23

#### Run 27

Changes tau

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
    "tau": 0.01,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 5000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = -18.11 +/- 176.77

#### Run 28

Changes gamma

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
    "gamma": 0.98,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 5000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 107.91 +/- 102.59


#### Run 29

Changes gamma

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
    "gamma": 0.5,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 5000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 17.35 +/- 178.67

#### Run 30

Changes gamma

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
    "gamma": 0.995,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 5000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 195.45 +/- 88.89

### Best original run

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