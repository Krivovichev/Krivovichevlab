import turtle
a=360
turtle.speed(0)
def S(a):
   x=0.4
   for i in range(360 * 5):
      x = x + a/(61.87787106982682/0.003)
      turtle.forward(x)
      turtle.right(1)
S(50)

