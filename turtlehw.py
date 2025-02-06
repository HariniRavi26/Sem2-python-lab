 import turtle

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

# Function to draw a triangle
def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)
 
# Function to draw a circle
def draw_circle(radius):
    turtle.circle(radius)

# Set up the turtle
turtle.speed(2)  # Set the speed of drawing
turtle.color("blue")

# Draw a square
turtle.penup()
turtle.goto(-150, 0)  # Move to a starting position
turtle.pendown()
draw_square(100)

# Draw a triangle
turtle.penup()
turtle.goto(0, 0)  # Move to a new position
turtle.pendown()
turtle.color("green")  # Change color for triangle
draw_triangle(100)

# Draw a circle
turtle.penup()
turtle.goto(150, 0)  # Move to a new position
turtle.pendown()
turtle.color("red")  # Change color for circle
draw_circle(50)

# Finish drawing
turtle.hideturtle()  # Hide the turtle
turtle.done()  # Finish the turtle graphics
