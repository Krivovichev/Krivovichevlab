import turtle
turtle.shape('turtle')
def K(n,leng):
    for i in range(n):
        turtle.forward(leng)
        turtle.stamp()
        turtle.backward(leng)
        turtle.right(360/n)
K(12,90)