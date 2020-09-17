import turtle
import math
turtle.speed(5)
def S(n):
    if n % 2 ==1:
        for i in range(n):
            turtle.forward(250)
            turtle.right(180-180/n)
    if n % 4 ==0:
        for i in range(n):
            turtle.forward(250)
            turtle.right(180-2*180/n) 
    if n%2== 0 and not( n%4== 0):
        for i in range(n//2):
            turtle.forward(250)
            turtle.right(180-360/n)
        turtle.penup()
        turtle.right(90)
        turtle.forward(250*math.sin(math.pi/n))
        turtle.left(90)
        turtle.pendown()        
        for i in range(n//2):
            turtle.forward(250)
            turtle.left(180-360/n)        

S(11)