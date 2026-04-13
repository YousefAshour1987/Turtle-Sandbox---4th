# Imports all of the turtle library
from turtle import *
import random
# Creates a window for our game
window = Screen()
window.bgcolor("teal")

t = Turtle()
# t.setheading(180+45)
# t.speed(1)
t.pensize(40)
# code
for i in range(4):
    t.left(90)
    t.backward(100)
    t.left(90)
    t.backward(100)
    t.penup()
    t.left(90)
    t.setposition(0,0)
    t.pendown()
t.penup()
t.setposition(0, -200)
t.pendown()
t.color("black", "white")  # (outline, fill)
# Start filling
t.begin_fill()
t.circle(200)  # Draw circle with given radius
t.end_fill()

window.mainloop()