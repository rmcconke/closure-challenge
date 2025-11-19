import numpy as np
from .dataset_utils import _ground_truth, case_names, evaluation_points, _velocity_field
from pathlib import Path

def score(predictions):
    """
    Calculate the overall benchmark score.
    
    Args:
        predictions: Dict mapping case names to prediction arrays
                    e.g., {'case1': array([...]), 'case2': array([...])}
    
    Returns:
        float: Overall score (lower is better)
    """
    scores = evaluate_by_case(predictions)
    return np.sum(list(scores.values())) 

def score_from_csv(path, delimiter=','):
    """Score predictions from CSV files.
    
    Args:
        path: Either:
            - Path to folder containing {case}.csv files
            - Dict mapping case names to CSV file paths
        delimiter: Delimiter used in the CSV files (default: ',')
    Returns:
        float: Overall score (lower is better)
    """
    predictions = _load_csv_predictions(path, delimiter)
    return score(predictions)

def _load_csv_predictions(path, delimiter):
    """Load predictions from CSV files."""
    
    # one option: pass in a dict of case names to file paths
    if isinstance(path, dict):
        # Dict of file paths
        return {case: np.genfromtxt(file, delimiter=delimiter) 
                for case, file in path.items()}
    
    # another option: pass in a folder path
    folder = Path(path)
    predictions = {}
    
    for case in case_names():
        csv_file = folder / f"{case}.csv"
        predictions[case] = np.loadtxt(csv_file, delimiter=delimiter)
    
    return predictions

def evaluate_by_case(predictions):
    scores = {}
    for case in case_names():
        scores[case] = evaluate_individual_case(case, predictions)
    return scores

def evaluate_individual_case(case, predictions):
    """
    Calculate scaled MAE for a single test case.
    Scales error by mean(|U_true|).
    """
    U_true = _velocity_field(case)
    U_pred = predictions[case] if isinstance(predictions, dict) else predictions

    mae = np.mean(np.abs(U_pred - U_true))
    scale = np.mean(np.abs(U_true))

    return mae / scale

def evaluate_from_csv_by_case(path, delimiter=','):
    """
    Calculate scaled MAE for a single test case.
    Scales error by mean(|U_true|).
    """
    predictions = _load_csv_predictions(path, delimiter)
    return evaluate_by_case(predictions)