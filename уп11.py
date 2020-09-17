import turtle
turtle.speed(0)
def O(x):
 for i in range(360):
  turtle.forward(x)
  turtle.right(1)
 for i in range(360):
  turtle.forward(x)
  turtle.left(1)
x=0.5
for i in range(10):
 O(x)
 x+=0.2