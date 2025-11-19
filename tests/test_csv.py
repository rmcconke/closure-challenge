import numpy as np
from closure_challenge import score, score_from_csv, case_names, evaluation_points, evaluate_from_csv_by_case
from closure_challenge.dataset_utils import _velocity_field

def test_csv_loading():
    predictions = dict.fromkeys(case_names())
    for case in case_names():
        predictions[case] = _velocity_field(case)
        np.savetxt(f"tests/example_submission/{case}.csv", predictions[case], delimiter=',')
        np.savetxt(f"tests/example_submission/{case}_spaces.csv", predictions[case], delimiter=' ')
        np.savetxt(f"tests/example_submission/{case}_tabs.csv", predictions[case], delimiter='\t')
        points = evaluation_points(case)
        np.savetxt(f"tests/example_submission/{case}_points.csv", points, delimiter=',')
    assert score_from_csv("tests/example_submission") == 0

    csv_dict_commas = {}
    csv_dict_spaces = {}
    csv_dict_tabs = {}
    for case in case_names():
        csv_dict_commas[case] = f"tests/example_submission/{case}.csv"
        csv_dict_spaces[case] = f"tests/example_submission/{case}_spaces.csv"
        csv_dict_tabs[case] = f"tests/example_submission/{case}_tabs.csv"
    assert score_from_csv(csv_dict_commas, delimiter=',') == 0
    assert score_from_csv(csv_dict_spaces, delimiter=' ') == 0
    assert score_from_csv(csv_dict_tabs, delimiter='\t') == 0

def test_evaluate_from_csv_by_case():
    predictions = dict.fromkeys(case_names())
    for case in case_names():
        predictions[case] = _velocity_field(case)
        np.savetxt(f"tests/example_submission/{case}.csv", predictions[case], delimiter=',')
    result = evaluate_from_csv_by_case("tests/example_submission")
    assert all(value == 0 for value in result.values()), f"Expected all zeros, got: {result}"
