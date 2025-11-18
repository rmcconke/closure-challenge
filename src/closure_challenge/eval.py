import numpy as np
from .dataset_utils import ground_truth, case_names, evaluation_grid, velocity_field


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
    U_true = velocity_field(case)
    U_pred = predictions[case] if isinstance(predictions, dict) else predictions

    mae = np.mean(np.abs(U_pred - U_true))
    scale = np.mean(np.abs(U_true))

    return mae / scale
