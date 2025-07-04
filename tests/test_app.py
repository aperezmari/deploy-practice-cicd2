import pytest
from my_calc_app.app import add, subtract, multiply, divide


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(1, 2, 3), (-1, 1, 0), (0.5, 0.5, 1.0)],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(5, 2, 3), (-1, -1, 0), (10, 0.5, 9.5)],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(3, 4, 12), (-2, 2, -4), (0.5, 0.5, 0.25)],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


def test_divide_ok():
    assert divide(10, 2) == 5


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
