# Parameters used to test (custom environment)

This file includes the parameters used for each test run. The model results are stored inside the runs folder.

## Custom environment

### HyperParameters

#### Baseline

Baseline

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 15
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 269.72 +/- 68.64

#### Run 1

Changes number of steps

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 15
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 500000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 188.85 +/- 131.82

#### Run 2

Changes number of steps

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 15
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 5000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 113.21 +/- 142.51

#### Run 3

Changes number of steps

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 15
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 10000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 274.88 +/- 81.81

#### Run 4

Changes the learning rate

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 15
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.0001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = -87.62 +/- 166.43

#### Run 5

Changes the learning rate

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 14
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.0003,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 231.30 +/- 130.13

#### Run 6

Changes the learning rate

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.003,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = -70.28 +/- 18.89

#### Run 7

Changes the learning_starts

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 5000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = -33.06 +/- 21.35

#### Run 8

Changes the learning_starts

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 50000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 215.47 +/- 101.23

#### Run 9

Changes train_freq

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 5,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = -160.21 +/- 48.94

#### Run 10

Changes train_freq

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 10,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = -190.57 +/- 26.18

#### Run 11

Changes gradient_steps

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 5,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 271.62 +/- 30.44

#### Run 12

Changes gradient_steps

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 10,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 262.04 +/- 76.64

#### Run 13

Changes exploration_fraction

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 15
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.05,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 147.47 +/- 129.05

#### Run 14

Changes exploration_fraction

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.2,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = -119.87 +/- 25.54

#### Run 15

Changes exploration_fraction

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.3,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 34.74 +/- 150.17

#### Run 16

Changes exploration_final_eps

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.01,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 251.56 +/- 97.17

#### Run 17

Changes exploration_final_eps

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.1,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 211.25 +/- 97.45

#### Run 18

Changes exploration_final_eps

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.2,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 220.16 +/- 112.07

#### Run 19

Changes buffer_size

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 100000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 250.78 +/- 41.63

#### Run 21

Changes batch_size

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 128,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = -93.82 +/- 36.05

#### Run 22

Changes batch_size

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 256,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 160.09 +/- 160.68

#### Run 23

Changes target_update_interval

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
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

Evaluated trained agent over 100 episodes: mean reward = 279.22 +/- 62.80

#### Run 24

Changes target_update_interval

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
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

Evaluated trained agent over 100 episodes: mean reward = 180.33 +/- 166.95

#### Run 25

Changes tau

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
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

Evaluated trained agent over 100 episodes: mean reward = 119.50 +/- 166.32

#### Run 26

Changes tau

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
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

Evaluated trained agent over 100 episodes: mean reward = -145.32 +/- 56.68

#### Run 27

Changes tau

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
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

Evaluated trained agent over 100 episodes: mean reward = 38.97 +/- 160.49

#### Run 28

Changes gamma

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
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

Evaluated trained agent over 100 episodes: mean reward = -116.51 +/- 83.00

#### Run 29

Changes gamma

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
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

Evaluated trained agent over 100 episodes: mean reward = 8.59 +/- 164.45

#### Run 30

Changes gamma

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
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

Evaluated trained agent over 100 episodes: mean reward = 150.34 +/- 124.08

### Best custom run

```python
ENV_SELECTION = "custom"  # Set to "custom" to use the modified environment.

SEED = 42
NUM_ENVS = 15
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 10000000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

DQN_KWARGS = {
    "learning_rate": 0.001,
    "buffer_size": 1000000,
    "learning_starts": 10000,
    "batch_size": 64,
    "tau": 1.0,
    "gamma": 0.99,
    "train_freq": 1,
    "gradient_steps": 1,
    "target_update_interval": 1000,
    "exploration_fraction": 0.1,
    "exploration_final_eps": 0.05,
    "max_grad_norm": 10.0,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 274.88 +/- 81.81

### HyperParameters PPO

#### Baseline PPO

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 202.80 +/- 61.87

#### Run 1 PPO

Changes the number of steps

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

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 83.04 +/- 122.09

#### Run 2 PPO

Changes the number of steps

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 5_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 224.48 +/- 38.31

#### Run 3 PPO

Changes the number of steps

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 10_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 251.33 +/- 29.10

#### Run 4 PPO

Changes the learning rate

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 1e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = -63.99 +/- 51.13

#### Run 5 PPO

Changes the learning rate

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 1e-3,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 300.23 +/- 29.29

#### Run 6 PPO

Changes the learning rate

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-3,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 141.70 +/- 126.59

#### Run 7 PPO

Changes the n_steps

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 256,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 207.71 +/- 106.76

#### Run 8 PPO

Changes the n_steps

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 512,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 51.14 +/- 109.46

#### Run 9 PPO

Changes the n_steps

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 2048,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 202.68 +/- 63.63

#### Run 10 PPO

Changes the batch size

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 64,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 217.30 +/- 76.75

#### Run 11 PPO

Changes the batch size

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 128,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 196.22 +/- 75.68

#### Run 12 PPO

Changes the batch size

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 512,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 170.73 +/- 90.23

#### Run 13 PPO

Changes the n_epochs

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 5,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 157.23 +/- 113.91

#### Run 14 PPO

Changes the n_epochs

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 20,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 278.51 +/- 37.11

#### Run 15 PPO

Changes the gamma

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.98,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 79.45 +/- 134.60

#### Run 16 PPO

Changes the gamma

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.5,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 22.62 +/- 175.02

#### Run 17 PPO

Changes the gamma

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.995,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 243.47 +/- 21.15

#### Run 18 PPO

Changes the gae_lambda

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.97,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 237.60 +/- 24.09

#### Run 19 PPO

Changes the gae_lambda

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.90,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 173.91 +/- 115.44

#### Run 20 PPO

Changes the clip_range

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.1,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 89.78 +/- 119.87

#### Run 21 PPO

Changes the clip_range

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.3,
    "ent_coef": 0.0,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 167.03 +/- 100.15

#### Run 22 PPO

Changes the ent_coef

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.01,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 220.01 +/- 72.36

#### Run 23 PPO

Changes the ent_coef

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.05,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 263.12 +/- 58.15

#### Run 24 PPO

Changes the ent_coef

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.1,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = -33.36 +/- 22.88

#### Run 25 PPO

Changes the vf_coef

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.3,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 175.04 +/- 103.59

#### Run 26 PPO

Changes the vf_coef

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 1_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 3e-4,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 10,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.0,
    "vf_coef": 0.7,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 203.95 +/- 64.36

#### Best Run PPO

Changes the vf_coef

```python
ENV_SELECTION = "custom"  # Set to "original" to use the unmodified environment.

SEED = 42
NUM_ENVS = 16
NUM_STEPS = 1000
TOTAL_TIMESTEPS = 5_000_000
EVAL_EPISODES = 100

POLICY_KWARGS = {
    "net_arch": [256, 256],
}

PPO_KWARGS = {
    "learning_rate": 1e-3,
    "n_steps": 1024,
    "batch_size": 256,
    "n_epochs": 20,
    "gamma": 0.99,
    "gae_lambda": 0.95,
    "clip_range": 0.2,
    "ent_coef": 0.01,
    "vf_coef": 0.5,
    "max_grad_norm": 0.5,
    "policy_kwargs": POLICY_KWARGS,
}
```

Evaluated trained agent over 100 episodes: mean reward = 314.85 +/- 52.45