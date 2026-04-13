# Imports all of the turtle library
from turtle import *
import random
# Creates a window for our game
window = Screen()
window.bgcolor("teal")

t = Turtle()
t.setheading(180+45)
# code
t.right(90)
t.forward(100)
t.penup()
t.setheading(45)

window.mainloop()