import turtle
turtle.shape('turtle')
def K(n,start,step):
    x=start
    for i in range(n):
        turtle.forward(x)
        turtle.right(90)
        turtle.forward(x)
        turtle.right(90)
        turtle.forward(x)
        turtle.right(90)
        turtle.forward(x)
        turtle.right(90)
        turtle.penup()
        turtle.backward(step/2)
        turtle.left(90)
        turtle.forward(step/2)
        turtle.right(90)
        x+=step
        turtle.pendown()
K(20,10,20)