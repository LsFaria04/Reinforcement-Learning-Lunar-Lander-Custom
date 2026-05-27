## Differences between the custom environment and the original one (actual tweaks):

- Finite fuel: engines consume fuel; thrust is forced to 0 at fuel=0 (max_fuel=300).
- Observation has an extra feature: normalized remaining fuel.
- Reward adds terminal leftover-fuel bonus (fuel_bonus=50.0).
- Observation noise is enabled (noise_std=0.005).
- Random spawn is enabled (random_spawn=True).
- Human render shows a fuel HUD.
- Uses a separate env ID: CustomLunarLander-v0.
