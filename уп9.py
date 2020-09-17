import turtle
import math
turtle.speed(0)
def K(n,R,step):
    leng=2*R*math.sin(math.pi/n)
    turtle.right(90*(n-2)/n)
    for i in range(n):
        turtle.forward(leng)
        turtle.left(360/n)
    turtle.right(180-90*(n-2)/n)
    turtle.penup()
    turtle.forward(step)
    turtle.pendown() 
    turtle.left(180)
n=11
R=50
step=30
turtle.left(180)
for i in range(3,n+3):
    K(i,R,step)
    R+=step
    
