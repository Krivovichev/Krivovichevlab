import pygame
from pygame.draw import *

pygame.init()
FPS = 30
sc = pygame.display.set_mode((800, 600))

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
    ellipse(sc, (167, 147, 172),(140+x, 190, 120, 240))
    line(sc, BLACK, [160+x, 400], [120+x, 550])
    line(sc, BLACK, [120+x, 550], [90+x, 550])
    line(sc, BLACK, [239+x, 400], [259+x, 550])
    line(sc, BLACK, [259+x, 550], [289+x, 550])
    circle(sc, T, (200+x, 160), 50)
    line(sc, BLACK, [160+x, 220], [80+x, 350])
    line(sc, BLACK, [240+x, 220], [320+x, 320])
    
def ice(x,y):
    polygon(sc, YELLOW, [[x, 35+y], [62+x, y], [62+x, 70+y], [x, y+35]])
    circle(sc, (255, 0, 0), (x+40, y+3),18)
    circle(sc, (85, 0, 0), (x+13, y+17),18)
    circle(sc, (255, 255, 255), (x+17, y-10),18)
    
def girl(x):
    polygon(sc, PINK, [[440+x, 170], [515+x, 430], [365+x, 430], [440+x, 170]])
    circle(sc, T, (440+x, 160), 50)
    line(sc, BLACK, [410+x, 430], [410+x, 550])
    line(sc, BLACK, [380+x, 550], [410+x, 550])
    line(sc, BLACK, [470+x, 430], [470+x, 550])
    line(sc, BLACK, [500+x, 552], [470+x, 550])
    
def ball(x):
    line(sc, BLACK, [590+x, 130], [560+x, 270])
    polygon(sc, RED, [[590+x, 130], [590+x, 60], [590+62+x, 130-35], [590+x, 130]])
    circle(sc, RED, (x+590+22, 63-5), 24)
    circle(sc, RED, (x+590+56, 75), 24)

rect(sc, GREEN, (0,300, 800, 300))    
boy(30)
ice(55,283)
girl(30)
ball(40)

x=30
line(sc, BLACK, [318+x,317], [424+x, 230])
line(sc, BLACK, [508+x, 280], [454+x, 230])
line(sc, BLACK, [508+x, 280], [570+x, 255])

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
