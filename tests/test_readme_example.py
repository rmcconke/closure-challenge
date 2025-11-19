from closure_challenge import score, evaluation_points, case_names
from closure_challenge.dataset_utils import _velocity_field
import numpy as np
from scipy.interpolate import griddata


def test_readme_example():
    predictions = {}
    your_model_results = {}
    your_grid_points = {}

    for case in case_names():
        your_model_results[case] = _velocity_field(case)
        your_grid_points[case] = evaluation_points(case)
        your_grid_points[case][:, 0] = your_grid_points[case][:, 0] + np.random.randn(1000) * 0.01
        your_grid_points[case][:, 1] = your_grid_points[case][:, 1] + np.random.randn(1000) * 0.01
        your_grid_points[case][:, 2] = your_grid_points[case][:, 2] + np.random.randn(1000) * 0.01

    for case in case_names():
        # Your model predictions on your grid
        xyz_your_points = your_grid_points[case]
        U_your_points = your_model_results[case]  

        # evaluation_points returns shape (1000, 3) where columns are [x, y, z]
        xyz_eval = evaluation_points(case)        

        U_pred = griddata(xyz_your_points, U_your_points, xyz_eval, method='nearest') # The interpolation method is up to you
        
        predictions[case] = U_pred

    final_score = score(predictions)
    print(final_score)
    assert final_score > 0
