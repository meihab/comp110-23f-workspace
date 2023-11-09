"""Drawing a desert landscape using turtle!

Above and beyond: 
Functions we didn't use in the tutorial: bgcolor() in line 44, circle() in line 54. 
Loops for interesting pattern: drawing cacti in line 110.
"""

__author__ = "730711612"

from turtle import Turtle, colormode, done, speed, bgcolor, hideturtle
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    land: Turtle = Turtle()
    mountain_1: Turtle = Turtle()
    mountain_2: Turtle = Turtle()
    mountain_3: Turtle = Turtle()
    sky_: Turtle = Turtle()
    cactus_1: Turtle = Turtle()
    cactus_2: Turtle = Turtle()
    cactus_3: Turtle = Turtle()
    cactus_4: Turtle = Turtle()

    landscape(land, -360, -100) 
    mountain(mountain_1, -400, -100)
    mountain(mountain_2, -100, -100)
    mountain(mountain_3, 200, -100)
    sky(sky_, -220, 100)
    cactus(cactus_1, -300, -300)
    cactus(cactus_2, -150, -200)
    cactus(cactus_3, 0, -280)
    cactus(cactus_4, 120, -175)

    done()


def sky(sun: Turtle, x: float, y: float) -> None:
    """Function for drawing the sky."""
    speed(0)

    # Color of the sky
    bgcolor('orange')
    hideturtle()

    # Drawing the sun
    sun.speed(0)
    sun.penup()
    sun.goto(x, y)
    sun.pendown()
    sun.fillcolor(255, 135, 2)
    sun.begin_fill()
    sun.circle(100)
    sun.end_fill()
    sun.hideturtle()


def landscape(land: Turtle, x: float, y: float) -> None:
    """Function for drawing the landscape.""" 
    land.speed(0)
    land.pencolor(184, 129, 8)
    land.fillcolor(253, 206, 100)
    land.penup()
    land.goto(x, y)
    land.pendown()
    land.begin_fill()
    i: int = 0
    while i < 4:
        land.forward(720)
        land.right(90)
        i += 1
    land.end_fill()
    land.hideturtle()


def mountain(mount: Turtle, x: float, y: float) -> None:
    """Function for drawing mountains."""
    mount.speed(0)
    mount.fillcolor(156, 117, 30)
    mount.penup()
    mount.goto(x, y)
    mount.pendown()
    mount.begin_fill()

    mount.left(60)
    mount.forward(180)
    mount.right(60)
    mount.forward(80)
    mount.right(60)
    mount.forward(180)
    mount.right(135)

    mount.end_fill()
    mount.ht()


def cactus(cac: Turtle, x: float, y: float) -> None:
    """Function for drawing cacti."""
    cac.speed(0)
    cac.fillcolor('green')
    cac.penup()
    cac.goto(x, y)
    cac.pendown()
    cac.begin_fill()

    cac.left(45)
    cac.forward(50)
    i: int = 0
    while i < 2:
        cac.right(90)
        cac.forward(25)
        cac.left(90)
        cac.forward(25)
        i += 1
    cac.right(90)
    cac.forward(25)
    cac.left(90)
    cac.forward(25)
    cac.right(90)
    cac.forward(50)

    cac.end_fill()
    cac.ht()


if __name__ == "__main__":
    main()