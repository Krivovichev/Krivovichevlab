import pygame
from pygame.draw import *

pygame.init()

FPS = 30
sc = pygame.display.set_mode((600, 600))

WHITE = (255, 255, 255)
RED=(255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
sc.fill(WHITE)

circle(sc, YELLOW, (250, 250), 150)
circle(sc, BLACK, (250, 250), 151, 1)
rect(sc, BLACK, (175, 325, 150, 25))
polygon(sc, BLACK, [[220, 210], [228, 200], [118, 130], [110, 140]])
circle(sc, RED, (180,212), 22)
circle(sc, BLACK, (180,212), 23, 1)
circle(sc, BLACK, (180,212), 12)
polygon(sc, BLACK, [[298, 210], [290, 200], [390, 140], [398, 150]])
circle(sc, RED, (330,210), 16)
circle(sc, BLACK, (330,210), 16, 1)
circle(sc, BLACK, (330,210), 8)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
