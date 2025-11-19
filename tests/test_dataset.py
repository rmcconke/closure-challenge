from closure_challenge import case_names, evaluation_points
from closure_challenge.dataset_utils import _velocity_field
import numpy as np

def test_all_cases_have_same_shape():
    for case in case_names():
        assert _velocity_field(case).shape == (1000, 3)
        assert evaluation_points(case).shape == (1000, 3)

def test_all_data_points_are_unique():
    for case in case_names():
        assert len(np.unique(evaluation_points(case), axis=0)) == len(evaluation_points(case))
        assert len(np.unique(_velocity_field(case), axis=0)) == len(_velocity_field(case))
