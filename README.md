# Closure Challenge

A benchmark for evaluating RANS closure models.

## Installation

```bash
pip install closure-challenge
```

## Quick Start

```python
from closure_challenge import score, evaluation_grid, case_names

predictions = {}

# Interpolate your results onto the evaluation grid
for case in case_names():
    # Get target grid for this case
    x, y, z = evaluation_grid(case)
    
    # You have predictions on your own grid
    U_your_grid = your_model_results[case]  
    x_your, y_your, z_your = your_grid_coordinates[case]
    
    # Interpolate onto evaluation grid (example using scipy)
    from scipy.interpolate import griddata
    points = np.column_stack([x_your.ravel(), y_your.ravel(), z_your.ravel()])
    U_pred = griddata(points, U_your_grid.ravel(), (x, y, z))
    
    predictions[case] = U_pred

# Calculate benchmark score
final_score = score(predictions)
print(f"Score: {final_score:.4f}")  # lower is better
```

## What you need to provide

A dictionary mapping case names to velocity field predictions:
```python
predictions = {
    'case1': np.array([...]),  # shape matches evaluation grid
    'case2': np.array([...]),
    ...
}
```

Each prediction array should be interpolated onto the corresponding evaluation grid.

## Scoring

The benchmark uses scaled Mean Absolute Error (MAE). Each case's error is normalized by the mean magnitude of the true velocity field, then summed across all cases.

## Available functions

- `case_names()` - List of test cases
- `evaluation_grid(case)` - Get (x, y, z) coordinates for a case
- `velocity_field(case)` - Ground truth velocity (for testing)
- `score(predictions)` - Calculate final benchmark score
- `evaluate_by_case(predictions)` - Get individual case scores

## Test Cases

The current scoring set includes these cases:
- `alpha_15_13929_4048`
- `alpha_15_13929_2024`
- `alpha_05_4071_4048`
- `alpha_05_4071_2024`
- `AR_1_Ret_360`
- `AR_3_Ret_360`
- `AR_14_Ret_180`
- `PHLL10595`
- `CBFS13700`

**Reminder: DO NOT train or validate on any of these cases. This violates the challenge rules.**