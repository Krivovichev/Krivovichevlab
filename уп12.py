import turtle
turtle.speed(0)
def O(x):
 for i in range(180):
  turtle.forward(x)
  turtle.right(1)
turtle.left(90)
for i in range(10):
 O(0.7)
 O(0.15)