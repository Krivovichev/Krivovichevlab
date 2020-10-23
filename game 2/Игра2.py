import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 20 # Скорость игры
screen = pygame.display.set_mode((1200, 800))

hscore=[]
out = open('score.txt', 'r')
for a in range (0, 5):
     hscore.append(int(out.readline()))
out.close()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

font = pygame.font.Font(None, 35)
surf = pygame.Surface((200, 50))
text = font.render("Score: "+str(0),True, (255, 255, 255))
surf.blit(text, [0,0])
screen.blit(surf, (1000, 150))
pygame.display.update()

N=4 # кол-во кружков
M=2 # кол-во квадратиков

pygame.display.update()
clock = pygame.time.Clock()
finished = False

x1, y1 = -30, -30
T= 39
score = 0
A=[0]*N
B=[0]*M

class Ball:
'''
Класс Ball описывает мишень - шарик
x,y - координаты центра
vx, vy - скорость шарика по осям x и y соответственно
r - радиус шарика
color - цвет шарика
screen - экран на котором создаётся шарик 
'''
     def __init__( self, x, y, vx, vy, r, color, screen):
          self.x = x
          self.y = y
          self.vx = vx
          self.vy = vy
          self.r = r
          self.color = color
          self.screen = screen
          
     def run(self):
     '''
     Метод run отвечает за перемещение шарика с течением времени и его отражение от стенок
     '''
          self.x = self.x + self.vx
          self.y = self.y + self.vy
          if self.x + self.r > 1200 or self.x - self.r < 0:
               self.vx = -self.vx
          if self.y - self.r < 0 or self.y + self.r > 800:
               self.vy = -self.vy
          circle(self.screen, self.color, (self.x, self.y), self.r)
          
     def click(self, x1, y1, score):
     '''
     Метод click отвечает за фиксацию попадания нажатия мыши по шарику, его удаление и начисление очков
     x1, y1, score - входные данные
     x1, y1 - координаты нажатия мышью
     score - текущее кол-во очков
     '''
          R = (self.x - x1) * (self.x - x1) + (self.y - y1) * (self.y - y1)
          if R < self.r * self.r:
               self.x = -200
               self.y = -200
               self.vx = 0
               self.vy = 0
               score = score + 2
          return(score)

class Squ:
'''
Класс Squ описывает мишень - квадрат
x,y - координаты левого верхнего угла квадрата
vy - скорость по вертикали
color - цвет квадрата
screen - экран на котором создаётся квадрат
'''
     def __init__( self, x, y, vy, r, color, screen):
          self.x = x
          self.y = y
          self.vy = vy
          self.r = r
          self.color = color
          self.screen = screen

     def run(self):
     '''
     Метод run отвечает за перемещение квадрата с течением времени
     '''
          self.y = self.y + self.vy
          self.vy +=1
          rect(self.screen, self.color, (self.x, self.y, self.r, self.r))

     def click(self, x1, y1, score):
     '''
     Метод click отвечает за фиксацию попадания нажатия мышью по квадрату, его удаление и начисление очков
     x1, y1 - координаты нажатия мышью
     score - текущее кол-во очков 
     '''
          if x1 > self.x and x1 < self.x + self.r:
             if y1 > self.y and y1 < self.y + self.r:
                 score += 3
                 self.x = -100
          return(score)

   
while not finished:
     
     clock.tick(FPS)
     T+=1
     
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1 , y1 = event.pos
            score -=1
            text = font.render("Score: "+str(score),True, (255, 255, 255))
            surf.fill((0,0,0))
            surf.blit(text, [0,0])
            screen.blit(surf, (1000, 150))
          
     if T % 40 == 0:
          for i in range(N):
               A[i] = Ball(randint(100,700), randint(100,500), randint(-20,20), randint(-20, 20), randint(30,50), COLORS[randint(0,5)], screen)
          for i in range(M):
               B[i] = Squ(randint(100,1000), randint(0,100), randint(15, 25), randint(30,50), COLORS[randint(0,5)], screen)
               
     for i in range(N):
          score = A[i].click(x1, y1, score)
          A[i].click(x1, y1, score)
          A[i].run()
     for i in range(M):
          score = B[i].click(x1, y1, score)
          B[i].click(x1, y1, score)
          B[i].run()
          
     x1, y1 = -30, -30
     
     text = font.render("Score: "+str(score),True, (255, 255, 255))
     surf.fill((0,0,0))
     surf.blit(text, [0,0])
     screen.blit(surf, (1000, 150))
                
     pygame.display.update()
     screen.fill(BLACK)

if score > hscore[4]: 
    hscore[4] = score
hscore.sort(reverse = True)
inp = open('score.txt', 'w')
inp.flush()
for i in range(0, 5):
    inp.write(str(hscore[i]) + '\n')
inp.close()

pygame.quit()
