import pytest


FIB_NUMS = [
    (-3, 0),
    (0, 0),
    (1, 0),
    (2, 1),
    (3, 1),
    (7, 8)
]


@pytest.mark.parametrize('n, result', FIB_NUMS)
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result


def test_lucas():
    from series import lucas
