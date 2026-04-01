# Imports all of the turtle library
from turtle import *
import random
# Creates a window for our game
window = Screen()
window.bgcolor("teal")

turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color("white")
turtle1.speed(255)
# r = random.randint(0, 255)
# g = random.randint(0, 255)
# b = random.randint(0, 255)

for step in range(100):
    # r = random.randint(0, 255)
    # g = random.randint(0, 255)
    # b = random.randint(0, 255)
    # turtle1.color(r,g,b)
    turtle1.speed(255)
    turtle1.forward(75)
    turtle1.right(90)
    turtle1.forward(75)
    turtle1.right(90)
    turtle1.forward(25)
    turtle1.left(90)
    turtle1.forward(25)
    turtle1.backward(75)
    turtle1.left(90)
    turtle1.forward(25)
    turtle1.left(90)
    turtle1.forward(75)
    turtle1.right(90)
    




window.mainloop()