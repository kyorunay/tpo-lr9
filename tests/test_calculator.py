# Модульные тесты класса Calculator
import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    # новый объект калькулятора для каждого теста
    return Calculator()


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-2, -3, -5),
    (-2, 5, 3),
    (0, 0, 0),
    (0.1, 0.2, 0.3),
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 6),
    (4, 10, -6),
    (-5, -5, 0),
    (7.5, 2.5, 5),
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [
    (6, 7, 42),
    (-3, 4, -12),
    (-3, -4, 12),
    (5, 0, 0),
    (2.5, 2, 5),
])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [
    (8, 2, 4),
    (7, 2, 3.5),
    (-9, 3, -3),
    (0, 5, 0),
    (1, 3, 0.3333333),
])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a", [5, 0, -5, 2.5])
def test_divide_by_zero(calc, a):
    # деление на ноль должно вызывать исключение
    with pytest.raises(ZeroDivisionError, match="Деление на ноль невозможно"):
        calc.divide(a, 0)


@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (13, True),
    (97, True),
    (1, False),
    (0, False),
    (-7, False),
    (4, False),
    (9, False),
    (100, False),
])
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) == expected
