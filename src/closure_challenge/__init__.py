"""Closure Challenge - RANS benchmark evaluation."""

__version__ = "0.1.0"

from .eval import score, evaluate_by_case
from .dataset_utils import case_names, ground_truth, evaluation_grid, velocity_field

__all__ = ["score", "evaluate_by_case", "case_names", "ground_truth", "evaluation_grid", "velocity_field"]