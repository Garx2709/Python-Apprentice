"""
# 20_Color_Lines.py

Finish the program to make Tina draw a square with each side being a different color.
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)            # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Move at a moderate speed, not too fast.

colors = [ 'red', 'blue', 'black', 'orange']    # define a list of colors

for color in colors:                            # loop through the colors
    tina.pencolor(color)
    tina.forward(200)                       # Move tina forward by the forward distance
    tina.right(-90)                         # Turn tina right by 90 degrees

turtle.exitonclick()                     # Close the window when we click on it