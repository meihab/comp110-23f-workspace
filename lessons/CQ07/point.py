"""Challenge question: practicing object oriented programming!"""

from __future__ import annotations

__author__ = "730711612"


class Point:
    """Takes attributes x, y and creats a point."""
    # attributes
    x: float 
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor, takes x and y."""
        self.x: float = x_init
        self.y: float = y_init

    def scale_by(self, factor: int) -> None:
        """Scales the point by factor, changes the original values of x and y."""
        self.x *= factor
        self.y *= factor 

    def scale(self, factor: int) -> Point:
        """Scales the point by factor, does not change the original values of x and y."""
        self.new_x = self.x * factor
        self.new_y = self.y * factor 

        new_point = Point(self.new_x, self.new_y)

        return new_point
    
    def __str__(self) -> str:
        """Overwriting str()."""
        string: str = f"x: {self.x}; y: {self.y}"
        return string
    
    def __mul__(self, factor: int | float) -> Point:
        """Overwriting * operator."""
        new_x = self.x * factor
        new_y = self.y * factor 

        new_point = Point(new_x, new_y)

        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Overwriting + operator."""
        new_x = self.x + factor
        new_y = self.y + factor 

        new_point = Point(new_x, new_y)

        return new_point
    