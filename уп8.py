import turtle
def K(n,step):
    x=step
    for i in range(4*n):
        turtle.forward(x)
        turtle.left(90)
        x+=step
    turtle.forward(x)
K(10,5)
        