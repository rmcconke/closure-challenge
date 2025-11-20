# Closure Challenge

[![PyPI version](https://badge.fury.io/py/closure-challenge.svg)](https://badge.fury.io/py/closure-challenge)

A benchmark challenge for evaluating machine learning-augmented RANS closure models. The main challenge page is [https://github.com/rmcconke/closure-challenge-benchmark](https://github.com/rmcconke/closure-challenge-benchmark). This repo is for the evaluation source code.

## Installation
```bash
pip install closure-challenge
```

## Quick Start
You need to interpolate your data onto the evaluation points:
```python
from closure_challenge import evaluation_points
xyz_eval = evaluation_points(case) #(1000,3) numpy array for each case
```

Then, there are **2 ways** to get your score from the package:
### Method 1: Direct scoring, using python

```python
from closure_challenge import score, evaluation_points, case_names
from scipy.interpolate import griddata # interpolation method/library is up to you

your_grid_points = {...}   # Dict[case_name -> (N, 3) array of xyz coordinates]
your_model_results = {...} # Dict[case_name -> (N, 3) array of velocity vectors]

predictions = {}
for case in case_names():
    # your model predictions on your grid
    xyz_your_points = your_grid_points[case]
    U_your_points = your_model_results[case]  

    # evaluation_points returns shape (1000, 3) where columns are [x, y, z]
    xyz_eval = evaluation_points(case)       

    # again, interpolation method/library is up to you
    U_pred = griddata(xyz_your_points, U_your_points, xyz_eval, method='nearest') 
    
    predictions[case] = U_pred


final_score = score(predictions)
```

### Method 2: Loading from CSV files
This is what will be used when updating the main challenge [github](https://github.com/rmcconke/closure-challenge-benchmark) with your submitted files.

You can pass in either:
1. The path to a folder containing your interpolated predictions on the test cases, which should be stored in the files:
- `alpha_15_13929_4048.csv`
- `alpha_15_13929_2024.csv`
- `alpha_05_4071_4048.csv`
- `alpha_05_4071_2024.csv`
- `AR_1_Ret_360.csv`
- `AR_3_Ret_360.csv`
- `AR_14_Ret_180.csv`
- `PHLL10595.csv`
- `CBFS13700.csv`

```python
from closure_challenge import score_from_csv
final_score = score_from_csv("path/to/predictions/")
```
2. A dictionary containing paths to your interpolated predictions for each of the test cases.

```python
from closure_challenge import score_from_csv
final_score = score_from_csv({
    "alpha_15_13929_4048": "path/to/your/alpha_15_13929_4048/predictions.csv",
    "alpha_15_13929_2024": "path/to/your/alpha_15_13929_2024/predictions.csv",
    "alpha_05_4071_4048": "path/to/your/alpha_05_4071_4048/predictions.csv",
    "alpha_05_4071_2024": "path/to/your/alpha_05_4071_2024/predictions.csv",
    "AR_1_Ret_360": "path/to/your/AR_1_Ret_360/predictions.csv",
    "AR_3_Ret_360": "path/to/your/AR_3_Ret_360/predictions.csv",
    "AR_14_Ret_180": "path/to/your/AR_14_Ret_180/predictions.csv",
    "PHLL10595": "path/to/your/PHLL10595/predictions.csv",
    "CBFS13700": "path/to/your/CBFS13700/predictions.csv",
})
```

## Scoring

The benchmark uses scaled Mean Absolute Error (MAE). Each case's error is normalized by the mean magnitude of the true velocity field, then summed across all cases.

## Available functions
i.e., you can do `from closure_challenge import`:
- `case_names()` - List of test cases
- `evaluation_points(case)` - Get evaluation (x, y, z) coordinates for a case
- `score(predictions)` - Calculate final benchmark score (see Method 1 above)
- `evaluate_by_case(predictions)` - Get individual case scores returned (Method 1)
- `score_from_csv(path)` - Calculate final benchmark score from CSV files (see Method 2 above)
- `evaluate_from_csv_by_case(path)` - Get individual case scores returned (Method 2)

## Test Cases

The current scoring set includes these cases, which you can get by
- `alpha_15_13929_4048`
- `alpha_15_13929_2024`
- `alpha_05_4071_4048`
- `alpha_05_4071_2024`
- `AR_1_Ret_360`
- `AR_3_Ret_360`
- `AR_14_Ret_180`
- `PHLL10595`
- `CBFS13700`

You can get these names using
```python
from closure_challenge import case_names
print(case_names())
```


**Reminder: DO NOT *train* or *validate* on any of these cases. In other words, you cannot use them during training in any way. This violates the challenge rules.**