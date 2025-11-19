import numpy as np
from closure_challenge import score, evaluate_by_case, case_names
from closure_challenge.dataset_utils import _velocity_field

def test_perfect_prediction_score_is_zero():
    predictions = dict.fromkeys(case_names())
    for case in case_names():
        predictions[case] = _velocity_field(case)
    assert score(predictions) == 0

def test_imperfect_prediction_score_is_positive():
    predictions = dict.fromkeys(case_names())
    for case in case_names():
        predictions[case] = _velocity_field(case) * 0.9
    assert score(predictions) > 0

    for case in case_names():
        predictions[case] = _velocity_field(case) * 1.1
    assert score(predictions) > 0

def test_scores_are_similar_scale():
    """
    Add scaled random noise to each case and check that the
    scaled MAE scores across all cases do not differ by more than 25%.
    """

    predictions = {}

    for case in case_names():
        U_true = _velocity_field(case)

        # noise level = 10% of mean(|U_true|)
        scale = np.mean(np.abs(U_true))
        noise = 0.10 * scale * np.random.randn(*U_true.shape)

        predictions[case] = U_true + noise

    scores = evaluate_by_case(predictions)  # dict: {case: score}
    values = np.array(list(scores.values()))
    max_score = values.max()
    min_score = values.min()

    # Require max/min <= 1.25  (i.e., within 25%)
    assert max_score / min_score <= 1.25

