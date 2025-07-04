"""
my_calc_app - Operaciones matemáticas básicas
"""

from math import isclose


def add(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Resta b a a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiplica dos números."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide a entre b.

    Lanza ZeroDivisionError si b == 0.
    """
    if isclose(b, 0.0):
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b
