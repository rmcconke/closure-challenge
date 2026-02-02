"""Closure Challenge - RANS benchmark evaluation."""

__version__ = "0.2.1"

from .eval import score, score_from_csv, evaluate_by_case, evaluate_from_csv_by_case
from .dataset_utils import case_names, evaluation_points

__all__ = ["score", "score_from_csv", "evaluate_by_case", "evaluate_from_csv_by_case", "case_names", "evaluation_points"]