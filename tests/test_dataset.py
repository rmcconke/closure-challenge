from closure_challenge import case_names, velocity_field, evaluation_grid
import numpy as np

def test_all_cases_have_same_shape():
    for case in case_names():
        assert velocity_field(case).shape == (1000, 3)
        assert evaluation_grid(case).shape == (1000, 3)

def test_all_data_points_are_unique():
    for case in case_names():
        assert len(np.unique(evaluation_grid(case), axis=0)) == len(evaluation_grid(case))
        assert len(np.unique(velocity_field(case), axis=0)) == len(velocity_field(case))

test_all_cases_have_same_shape()
test_all_data_points_are_unique()