"""EX04 - Utility Functions - Implementing Alogrithms!"""

__author__ = "730711612"


def all(x: list[int], y: int) -> bool:
    """Checks if all the values in list x are equal to the number y."""
    if len(x) == 0:
        return False

    counter: int = 0
    while counter < len(x):
        if x[counter] != y:
            return False
        counter += 1 

    return True


def max(x: list[int]) -> int:
    """Finds the largest number in list x."""
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")

    largest: int = x[0]
    counter: int = 1
    while counter < len(x):
        if x[counter] > largest:
            largest = x[counter]
        counter += 1
    return largest 


def is_equal(x: list[int], y: list[int]) -> bool:
    """Checks if two lists are equal to each other."""
    if len(x) != len(y):
        return False
    
    counter: int = 0
    while counter < len(x):
        if x[counter] != y[counter]:
            return False
        counter += 1

    return True