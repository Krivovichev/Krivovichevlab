import turtle
turtle.speed(0)
def O(r):
 for i in range(360):
  turtle.forward(r*6.28/360)
  turtle.right(1)
def O1(r):
 for i in range(180):
  turtle.forward(r*6.28/360)
  turtle.right(1)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.begin_fill()
O(100)
turtle.color('yellow')
turtle.end_fill()
turtle.color('black')

turtle.penup()
turtle.goto(45, 55)
turtle.pendown()
turtle.begin_fill()
O(15)
turtle.color('blue')
turtle.end_fill()
turtle.color('black')

turtle.penup()
turtle.goto(-45, 55)
turtle.pendown()
turtle.begin_fill()
O(15)
turtle.color('blue')
turtle.end_fill()
turtle.color('black')

turtle.penup()
turtle.goto(0, 25)
turtle.pendown()
turtle.right(90)
turtle.width(8)
turtle.goto(0, -10)

turtle.penup()
turtle.goto(50, -25)
turtle.pendown()
turtle.color('red')
O1(50)
