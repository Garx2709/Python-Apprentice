"""
# 20_Crazy_Spiral.py

Make your own crazy spiral with a pattern like
in 10_Flaming_Ninja_Star.py, but use what you've learned about loops

uid: zfzMbyH7
name: Crazy Spiral
"""

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.width(2)
t.speed(0)

# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.

def make_a_shape(t):
    
    t.pencolor('green')                  # Set the pen color to green
    t.forward(200)
    t.right(90)

num_shapes = 22

for i in range(100):
    make_a_shape(t)
    t.right(num_shapes)

turtle.exitonclick()                    # Close the window when we click on it