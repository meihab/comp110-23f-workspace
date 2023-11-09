"""Testing my methods."""

from lessons.CQ07.point import Point

my_point = Point(1.0, 2.0)
new_point: Point = my_point + 3

print(str(new_point))