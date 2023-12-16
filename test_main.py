import numpy as np

import pytest

from main import add_arrays_c


@pytest.mark.parametrize(
    ("arr1", "arr2"),
    [
        (np.array([1.0, 2.0, 3.0]), np.array([3.0, 2.0, 1.0])),
        (np.arange(1, 10, dtype=float), np.ones(9, dtype=float)),
        (np.linspace(0, 1), np.linspace(1, 2)),
    ],
)
def test_add_arrays_c(arr1, arr2):
    res = add_arrays_c(arr1, arr2)
    np.testing.assert_array_almost_equal(res, arr1 + arr2)
