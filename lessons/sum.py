"""Summing the elements of a list using different loops!"""

__author__ = "730711612"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of values in a list using a while loop."""
    counter: int = 0
    total: float = 0.0
    while counter < len(vals):
        total += vals[counter]
        counter += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Returns the sum of values in a list using a for loop."""
    total: float = 0.0
    for i in vals:
        total += i
    return total


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of values in a list using a for loop with the range keyword."""
    total: float = 0.0
    for i in range(len(vals)):
        total += vals[i]
    return total