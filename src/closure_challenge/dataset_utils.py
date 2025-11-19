import numpy as np
from pathlib import Path

def _ground_truth():
    data_path = Path(__file__).parent / "data" / "ground_truth_test.npz"
    raw = np.load(data_path)

    dataset = {}

    for full_key in raw.keys():
        case, field = full_key.split("/", 1)

        if case not in dataset:
            dataset[case] = {}

        dataset[case][field] = raw[full_key]

    return dataset


def case_names():
    data_path = Path(__file__).parent / "data" / "ground_truth_test.npz"
    raw = np.load(data_path)
    cases = [k.split("/", 1)[0] for k in raw.keys()]
    return list(dict.fromkeys(cases))  # deduplicate, preserve order

def evaluation_grid(case):
    """
    Get the x, y, z coordinates for the evaluation grid.
    """
    return _ground_truth()[case]['coords']

def _velocity_field(case):
    """
    Get the velocity field for a given case.
    """
    return _ground_truth()[case]['U']
