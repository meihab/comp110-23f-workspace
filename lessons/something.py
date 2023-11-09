import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("skyblue")  # Set the background color

# Create a Turtle object for drawing
desert = turtle.Turtle()
desert.speed(0)  # Fastest drawing speed

# Function to draw a cactus
def draw_cactus():
    desert.penup()
    desert.goto(-30, -100)
    desert.pendown()
    desert.color("green")
    desert.begin_fill()
    desert.left(90)
    desert.forward(60)
    for _ in range(3):
        desert.right(90)
        desert.forward(20)
        desert.left(90)
        desert.forward(20)
    desert.right(90)
    desert.forward(20)
    desert.left(90)
    desert.forward(20)
    desert.right(90)
    desert.forward(60)
    desert.end_fill()

# Function to draw a sand dune
def draw_sand_dune():
    desert.penup()
    desert.goto(-400, -100)
    desert.pendown()
    desert.color("yellow")
    desert.begin_fill()
    desert.goto(0, 50)
    desert.goto(400, -100)
    desert.goto(-400, -100)
    desert.end_fill()

# Function to draw the sun
def draw_sun():
    desert.penup()
    desert.goto(200, 200)
    desert.pendown()
    desert.color("yellow")
    desert.begin_fill()
    desert.circle(40)
    desert.end_fill()

# Draw the desert scene
draw_sand_dune()
draw_cactus()
draw_sun()

# Hide the Turtle cursor and display the result
desert.hideturtle()
screen.exitonclick()