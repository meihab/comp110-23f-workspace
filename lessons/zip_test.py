"""Test my zip function!"""

__author__ = "730711612"

from lessons.zip import zip


def test_empty_lists() -> None:
    """zip([], []) should return {}."""
    assert zip([], []) == {}


def test_different_lengths() -> None:
    """zip() returns 0 when the input lists are of different lengths."""
    assert zip(["First"], [1, 2]) == {}


def test_same_lengths() -> None:
    """zip() combines the two lists into a dictionary if the lists are of the same lengths."""
    my_dictionary: dict(str, int) = {"First": 1, "Second": 2, "Third": 3}
    assert zip(["First", "Second", "Third"], [1, 2, 3]) == my_dictionary