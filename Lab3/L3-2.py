import pygame
from pygame.draw import *

pygame.init()
FPS = 30
sc = pygame.display.set_mode((1200, 900))

WHITE = (255, 255, 255)
RED=(255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (154, 218, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
T= (255, 223, 196)

sc.fill(LIGHT_BLUE)

def boy(x):
    ellipse(sc, (167, 147, 172),(140+x, 390, 120, 240))
    line(sc, BLACK, [160+x, 600], [120+x, 750])
    line(sc, BLACK, [120+x, 750], [90+x, 750])
    line(sc, BLACK, [239+x, 600], [259+x, 750])
    line(sc, BLACK, [259+x, 750], [289+x, 750])
    circle(sc, T, (200+x, 360), 50)
    line(sc, BLACK, [160+x, 420], [80+x, 520])
    line(sc, BLACK, [240+x, 420], [320+x, 520])
    
def ice(x,y):
    polygon(sc, YELLOW, [[x, 235+y], [-62+x, y+200], [-62+x, 270+y], [x, y+235]])
    circle(sc, (255, 0, 0), (x-40, y+203),18)
    circle(sc, (85, 0, 0), (x-13, y+217),18)
    circle(sc, (255, 255, 255), (x-17, y+190),18)
    
def girl(x):
    polygon(sc, PINK, [[440+x, 370], [515+x, 630], [365+x, 630], [440+x, 370]])
    circle(sc, T, (440+x, 360), 50)
    line(sc, BLACK, [410+x, 630], [410+x, 750])
    line(sc, BLACK, [380+x, 750], [410+x, 750])
    line(sc, BLACK, [470+x, 630], [470+x, 750])
    line(sc, BLACK, [500+x, 752], [470+x, 750])

def ice2(x,y):
    polygon(sc, YELLOW, [[x, y+200], [x-70, y-121+200], [70+x, y-121+200], [x, y+200]])
    line(sc, BLACK, [x, y+200], [x-10, 380+y])
    circle(sc, (255, 0, 0), (x-30, y+200-135),32)
    circle(sc, (85, 0, 0), (x+30, y+200-135),32)
    circle(sc, (255, 255, 255), (x, y+31),32)
def ball(x,y):
    line(sc, BLACK, [-590+x, 330+y], [-560+x, 470+y])
    polygon(sc, RED, [[-590+x, 330+y], [-590+x, 260+y], [-590-62+x, 330-35+y], [-590+x, 330+y]])
    circle(sc, RED, (x-590-22, 263-5+y), 24)
    circle(sc, RED, (x-590-56, 275+y), 24)

rect(sc, GREEN, (0,500, 1400, 300))    
boy(30)
girl(30)
ball(675, 77)
girl(290)
boy(770)
ice(1150,255)
ice2(610,75)
x=30
line(sc, BLACK, [318+x,517], [424+x, 430])
line(sc, BLACK, [508+x, 480], [454+x, 430])
line(sc, BLACK, [508+x, 480], [570+x, 455])
x=1170
line(sc, BLACK, [-318+x,517], [-424+x, 430])
line(sc, BLACK, [-508+x, 480], [-454+x, 430])
line(sc, BLACK, [-508+x, 480], [-570+x, 455])


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
