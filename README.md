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