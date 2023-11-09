"""Practicing functions with dictionaries!"""

__author__ = "730711612"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values."""
    new_dict: dict[str, str] = {}
    for i in x:
        if x[i] in new_dict:
            raise KeyError()
        new_dict[x[i]] = i
    return new_dict


def favorite_color(a: dict[str, str]) -> str:
    """Determines which color appears most frequently."""
    if len(a) == 0:
        return None
    else:
        my_list = []
        for i in a:
            my_list.append(a[i])

        count_list: list[int] = []
        for i in my_list:
            count_list.append(my_list.count(i))
        idx = count_list.index(max(count_list))

        return my_list[idx]


def count(my_list: list[str]) -> dict[str, int]:
    """Gives the count of each value in a list in dictionary format."""
    new_dict: dict[str, int] = {}
    for i in my_list:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """Groups words by first letter."""
    new_dict: dict[str, list[str]] = {}

    for i in x:
        if i[0].lower() not in new_dict:
            new_dict[i[0].lower()] = [i]
        else:
            new_dict[i[0].lower()].append(i)
    return new_dict


def update_attendance(a: dict[str, list[str]], day: str, name: str) -> dict[str, list[str]]:
    """Updating dictionaries."""
    if day not in a:
        a[day] = [name]
    else:
        if name not in a[day]:
            a[day].append(name)
    return a