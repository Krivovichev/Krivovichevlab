import turtle
from random import randint
pool=[turtle.Turtle(shape='circle') for i in range(15)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200,200), randint(-200,200))
for unit in pool:
    unit.left(randint(-180,180))
for i in range(300):
    for unit in pool:
        unit.forward(5)
        x,y= unit.position()
        if x > 350 or x < -350:
                n = unit.heading()
                unit.setheading(180-n)
        if y > 300 or y < -300:
                n = unit.heading()
                unit.setheading(-n)
 

