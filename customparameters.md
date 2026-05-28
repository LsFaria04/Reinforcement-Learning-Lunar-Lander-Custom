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

