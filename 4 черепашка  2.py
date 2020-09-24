import turtle
x=0.1
y=0.1
vx=20
vy=60
dt=0.01
ay=-20
for t in range(0,5000):
    x+=vx*dt
    y+=vy*dt+ 0.5*ay*dt**2
    vy+= ay*dt
    if y<=0:
        vy=-vy
    turtle.goto(x,y)