"""Combining two lists into a dictionary."""

__author__ = "730711612"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Combines the two lists into a dictionary."""
    my_dict: dict[str, int] = {}

    if len(list1) != len(list2):
        return my_dict
    else:
        for i in range(len(list1)):
            my_dict[list1[i]] = list2[i]

    return my_dict


print(zip(["Happy", "Tuesday"], [1, 2]))
print(zip([], []))