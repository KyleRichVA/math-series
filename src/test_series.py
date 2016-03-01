import pytest


FIB_NUMS = [
    (-3, 0),
    (-2, 0),
    (0, 0),
    (1, 0),
    (2, 1),
    (3, 1),
    (7, 8)
]

LUCAS_NUMS = [
    (-3, 0),
    (0, 0),
    (1, 2),
    (2, 1),
    (3, 3),
    (4, 4),
    (5, 7),
    (7, 18)
]

SERIES_NUMS = [
    ((2,), 1),
    ((3, 2, 1), 3),
    ((4, 0, 1), 2),
    ((2, 5, 10), 10),
    ((3, 5, 5), 10)
]


@pytest.mark.parametrize('n, result', FIB_NUMS)
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUCAS_NUMS)
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('args, result', SERIES_NUMS)
def test_sum_series(args, result):
    from series import sum_series
    assert sum_series(*args) == result
