"""Testing dictionary functions!"""

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest

__author__ = "730711612"


# invert 
def test_empty() -> None:
    """invert({}) should return {}."""
    assert invert({}) == {}


def test_not_empty() -> None:
    """invert({'First': 1, 'Second': 2}) should return {1: 'First', 2: 'Second'}."""
    assert invert({'First': 1, 'Second': 2}) == {1: 'First', 2: 'Second'}


def test_repeated_key() -> None:
    """Repeated key should raise ValueError."""
    with pytest.raises(KeyError):
        my_dict = {'First': 1, 'Second': 1}
        invert(my_dict)


# favorite_color
def test_color() -> None:
    """favorite_color() should return the most repeated color, in this case blue."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_color_tie() -> None:
    """If colors tie, favorite color should return the one the comes first in the sequence (yellow)."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Mo": "yellow"}) == "yellow"


def test_color_empty() -> None:
    """favorite_color({}) should return None."""
    assert favorite_color({}) is None


# count
def test_count() -> None:
    """When each element appears once."""
    assert count([1, 2, 3]) == {1: 1, 2: 1, 3: 1}


def test_count_elements_repeat() -> None:
    """When elements in the list are repeated."""
    assert count([1, 2, 2, 2, 2, 2, 3, 3, 3]) == {1: 1, 2: 5, 3: 3}


def test_count_empty() -> None:
    """count([]) should return {}."""
    assert count([]) == {}


# alphabetizer
def test_alphabetizer() -> None:
    """When each letter appears once."""
    assert alphabetizer(['apple', 'cat', 'ball']) == {'a': ['apple'], 'c': ['cat'], 'b': ['ball']}


def test_alphabetizer_multiple() -> None:
    """When each letter appears multiple times."""
    assert alphabetizer(['apple', 'cat', 'ball', 'city']) == {'a': ['apple'], 'c': ['cat', 'city'], 'b': ['ball']}


def test_alphabetizer_type_error() -> None:
    """Type error if element is not a string."""
    with pytest.raises(TypeError):
        alphabetizer(['apple', 1])


# update_attendance
def test_update_attendance() -> None:
    """Add new name."""
    my_dict: dict[str, list[str]] = {'Monday': ['a', 'b'], 'Tuesday': ['c', 'd']}
    assert update_attendance(my_dict, 'Tuesday', 'a') == {'Monday': ['a', 'b'], 'Tuesday': ['c', 'd', 'a']}


def test_update_attendance_() -> None:
    """Add new day and name."""
    my_dict: dict[str, list[str]] = {'Monday': ['a', 'b'], 'Tuesday': ['c', 'd']}
    assert update_attendance(my_dict, 'Wednesday', 'x') == {'Monday': ['a', 'b'], 'Tuesday': ['c', 'd'], 'Wednesday': ['x']}


def test_update_attendance_attribute_error() -> None:
    """Attribute error if a value in the dictionary is not a list."""
    with pytest.raises(AttributeError):
        my_dict: dict[str, list[str]] = {'Monday': 'a', 'Tuesday': ['c', 'd']}
        update_attendance(my_dict, 'Monday', 'x')
