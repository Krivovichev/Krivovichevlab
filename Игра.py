import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

font = pygame.font.Font(None, 35)


surf = pygame.Surface((200, 100))
text = font.render("Score: "+str(0),True, (255, 255, 255))
surf.blit(text, [0,0])
screen.blit(surf, (1000, 150))
pygame.display.update()

def click(event, x1, y1, r, x, y, score):
    R = (x - x1) * (x - x1) + (y - y1) * (y - y1)
    if R < r * r:
        score +=1
    return score
def click1(event, x1, y1, R1, X1, Y1, score):
    if x1 > X1 and x1 < X1 + R1:
        if y1 > Y1 and y1 < Y1 + R1:
            score += 2
    return score

fps = 4
N=4
M=2

pygame.display.update()
clock = pygame.time.Clock()
finished = False
clock1 = pygame.time.Clock()

T= 19

X=[0] * N
Y=[0] * N
VX=[0] * N
VY=[0] * N
R=[0] * N

score = 0

R1 = [0] * M
X1 = [0] * M
Y1 = [0] * M
VY1 = [0] * M

while not finished:
    clock.tick(FPS* fps)
    T+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1 , y1 = event.pos
            
            for i in range(N):
                click(event, x1, y1, R[i], X[i], Y[i], score)
                score = click(event, x1, y1, R[i], X[i], Y[i], score)
            text = font.render("Score: "+str(score),True, (255, 255, 255))
            surf.fill((0,0,0))
            surf.blit(text, [0,0])
            
            for k in range(M):
                click1(event, x1 , y1 , R1[k], X1[k], Y1[k], score)
                score = click1(event, x1 , y1 , R1[k], X1[k], Y1[k], score)
            text = font.render("Score: "+str(score),True, (255, 255, 255))
            surf.fill((0,0,0))
            surf.blit(text, [0,0])


                
    screen.blit(surf, (1000, 150))


    if T % 20 == 0:
        color = COLORS[randint(0, 5)]
        for k in range(M):
            X1[k] = randint(100, 1000)
            Y1[k]= randint(0,100)
            R1[k] = randint(30,50)
            VY1[k] = randint (30, 50)
    for k in range(M):
        Y1[k] = Y1[k] + int(VY1[k])
        VY1[k] = VY1[k] * 1.05
        rect(screen, color, (X1[k], Y1[k] , R1[k],R1[k] ))

    if T % 20 == 0:
        color = COLORS[randint(0, 5)]
        for i in range(N):
            X[i] = randint(100,700)
            Y[i]= randint(100,500)
            R[i] = randint(30,50)
            VY[i] = randint (-40, 40)
            VX[i]= randint (-40, 40)
    for i in range(N):
        X[i] = X[i] + VX[i]
        Y[i] = Y[i] + VY[i]
        if X[i] - R[i] < 0 or X[i] + R[i] > 1200:
            VX[i] = - VX[i]
        if Y[i] - R[i] < 0 or Y[i] + R[i] > 800:
            VY[i] = - VY[i]
        circle(screen, color, (X[i], Y[i]), R[i])
    
    pygame.display.update()
        
    screen.fill(BLACK)

pygame.quit()
