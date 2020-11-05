import numpy as np
import pygame as pg
from random import randint

pg.init()
pg.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_SIZE = (800, 600)

def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

class Ball:
    '''
    Задаёт выстрел, отвечает за его движение.
    '''
    def __init__(self, coord, vel, rad=20, color=None):
        self.coord = coord
        self.vel = vel
        if color == None:
            color = rand_color()
        self.color = color
        self.rad = rad
        self.is_alive = True
        
    def draw(self, screen):
      '''
      Рисует выстрел
      '''
      pg.draw.circle(screen, self.color, self.coord, self.rad)
        
    def move(self, time=1, grav=0):
        '''
       Движение под действием гравитации
        '''
        self.vel[1] += grav
        for i in range(2):
            self.coord[i] += time * self.vel[i]
        self.check_corners()
        if self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
            self.is_alive = False

    def check_corners(self, refl_ort=0.8, refl_par=0.9):
        '''
        Неупругое отражение от границ экрана
        '''
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)

class Target:
    '''
    Задаёт мишени.
    '''
    def __init__(self, coord=None, color=None, rad=30, speed = None):
        if coord == None:
            coord = [randint(rad, SCREEN_SIZE[0] - rad), randint(rad, SCREEN_SIZE[1] - rad)]
        self.coord = coord
        self.rad = rad

        if color == None:
            color = rand_color()
        self.color = color
        
        if speed == None:
            speed = [randint(5, 10) , randint(5, 10)]
        self.speed = speed
        
    def run(self):
        '''
        Отвечает за перемещение и отражение от стен мишени
        '''
        for i in range(2):
            self.coord[i] += self.speed[i]
        if self.coord[0] + self.rad > 800 or self.coord[0] - self.rad < 0:
            self.speed[0] = -self.speed[0]
        if self.coord[1] - self.rad < 0 or self.coord[1] + self.rad > 600:
            self.speed[1] = -self.speed[1]
               
    def check_collision(self, ball):
        '''
        Фиксирует попадание.
        '''
        dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
        min_dist = self.rad + ball.rad
        return dist <= min_dist

    def draw(self, screen):
        '''
        Рисует мишень
        '''
        pg.draw.circle(screen, self.color, self.coord, self.rad)

class Gun:
    '''
    Класс задаёт пушку
    '''
    def __init__(self, coord=[30, SCREEN_SIZE[1]//2], angle=0, max_pow=70, min_pow=10, color=BLACK):
        self.coord = coord
        self.angle = angle
        self.max_pow = max_pow
        self.min_pow = min_pow
        self.color = color
        self.active = False
        self.pow = min_pow
        
    def strike(self):
        '''
        Создаёт снаряд, задаёт его скорость.
        '''
        vel = self.pow
        angle = self.angle
        ball = Ball(list(self.coord), [int(vel*np.cos(angle)), int(vel*np.sin(angle))])
        self.pow = self.min_pow
        self.active = False
        return ball
    
    def activate(self):
        '''
        Активация пушки.
        '''
        self.active = True

    def gain(self, inc=2):
        '''
       Увеличение мощности.
        '''
        if self.active and self.pow < self.max_pow:
            self.pow += inc
      
    def set_angle(self, target_pos):
        '''
        Изменяет направление пушки.
        '''
        self.angle = np.arctan2(target_pos[1] - self.coord[1], target_pos[0] - self.coord[0])

    def move(self, inc):
        '''
        Длина пушки.
        '''
        if (self.coord[1] > 30 or inc > 0) and (self.coord[1] < SCREEN_SIZE[1] - 30 or inc < 0):
            self.coord[1] += inc

    def draw(self, screen):
        '''
        Рисует пушку.
        '''
        gun_shape = []
        vec_1 = np.array([int(5*np.cos(self.angle - np.pi/2)), int(5*np.sin(self.angle - np.pi/2))])
        vec_2 = np.array([int(self.pow*np.cos(self.angle)), int(self.pow*np.sin(self.angle))])
        gun_pos = np.array(self.coord)
        gun_shape.append((gun_pos + vec_1).tolist())
        gun_shape.append((gun_pos + vec_1 + vec_2).tolist())
        gun_shape.append((gun_pos + vec_2 - vec_1).tolist())
        gun_shape.append((gun_pos - vec_1).tolist())
        pg.draw.polygon(screen, self.color, gun_shape)

class ScoreTable:
    '''
    Таблица очков.
    '''
    def draw(self, screen):
        '''
        Рисует таблицу очков
        '''
        s = self.font.render(format(self.score()), True, BLACK)
        screen.blit(s, [10, 10 + 30])
        
    def __init__(self, t_destr=0,):
        self.t_destr = t_destr
        self.font = pg.font.SysFont("dejavusansmono", 25)

    def score(self):
        '''
        Возвращает число очков.
        '''
        return self.t_destr

class Exit:
    '''
    Задаёт кнопку выход
    '''
    def __init__ (self):
        self.font = pg.font.SysFont("dejavusansmono", 25)
        
    def draw(self, screen):
        '''
        Рисует кнопку
        '''
        s = self.font.render("Выход" , True, BLACK)
        screen.blit(s, [30, 540])
        
    def check(self, x, y):
        '''
        Проверяет нажатие на кнопку
        '''
        check = False
        if x > 30 and x < 90:
            if y < 560 and y > 530:
                check = True
        return check
    
class Retry:
    '''
    Задаёт кнопку заново
    '''
    
    def __init__ (self):
        self.font = pg.font.SysFont("dejavusansmono", 25)
        
    def draw(self, screen):
        '''
        Рисует кнопку
        '''
        s = self.font.render("Заново" , True, BLACK)
        screen.blit(s, [30, 570])    

    def check(self, x, y):
        '''
        Проверяет нажатие
        '''
        retr = False
        if x > 30 and x < 90:
            if y < 590 and y > 560:
                retr = True
        return retr
    
class Manager:
    '''
    Класс управляющий обработкой событий, движением, столкновениями, созданием мишеней
    '''
    def __init__(self, n_targets=1):
        self.balls = []
        self.gun = Gun()
        self.targets = []
        self.score_t = ScoreTable()
        self.n_targets = n_targets
        self.new_mission()
        self.exit = Exit()
        self.retry = Retry()
        
    def collide(self):
        '''
        Проверяет столкновения выстрелов с мишенями, удаляет сбитые.
        '''
        collisions = []
        targets_c = []
        for i, ball in enumerate(self.balls):
            for j, target in enumerate(self.targets):
                if target.check_collision(ball):
                    collisions.append([i, j])
                    targets_c.append(j)
        targets_c.sort()
        for j in reversed(targets_c):
             self.score_t.t_destr += 1
             self.targets.pop(j)
             
    def process(self, events, screen):
        '''
        Использует все необходимые методы для обеспечения работы, создаёт новые мишени.
        '''
        done, retr = self.handle_events(events)
        
        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
        
        self.move()
        self.collide()
        self.draw(screen)
        
        if retr == True:
             self.targets = []
             self.balls = []
             self.score_t.t_destr =0
             
        if len(self.targets) == 0 and len(self.balls) == 0:
            self.new_mission()
        score = self.score_t.t_destr
        return done, score

    def handle_events(self, events):
        '''
        Обработка событий с мыши, клавиатуры
        '''
        done, retr = False, False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.gun.move(-5)
                elif event.key == pg.K_DOWN:
                    self.gun.move(5)
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if done == False:
                    done = self.exit.check(x,y)
                retr = self.retry.check(x, y)  
                if event.button == 1:
                    if not((x < 90 and x > 30) and (y < 590 and y > 560)):
                        self.gun.activate()
            elif event.type == pg.MOUSEBUTTONUP:
                x, y = event.pos
                if event.button == 1:
                    if not((x < 90 and x > 30) and (y < 590 and y > 560)):
                        self.balls.append(self.gun.strike())
                        self.score_t.t_destr -=1
        return done, retr

    def draw(self, screen):
        '''
        Отображение мишеней, выстрелов, пушки, счёта. Перемещение мишеней
        '''
        for ball in self.balls:
            ball.draw(screen)
        for target in self.targets:
            target.run()
            target.draw(screen)
        self.gun.draw(screen)
        self.score_t.draw(screen)
        self.exit.draw(screen)
        self.retry.draw(screen)
        
    def move(self):
        '''
        Перемещение выстрелов под действием гравитации, удаление выстрелов.
        '''
        dead_balls = []
        for i, ball in enumerate(self.balls):
            ball.move(grav=2)
            if not ball.is_alive:
                dead_balls.append(i)
        for i in reversed(dead_balls):
            self.balls.pop(i)
        self.gun.gain()
            
    def new_mission(self):
        '''
        Создаёт новые мишени.
        '''
        for i in range(self.n_targets):
            self.targets.append(Target(rad=randint(max(1, 30 - 2*max(0, self.score_t.score())), 
                30 - max(0, self.score_t.score()))))

screen = pg.display.set_mode(SCREEN_SIZE)

done = False
clock = pg.time.Clock()

manager = Manager(n_targets=4)

while not done:
    clock.tick(15)
    screen.fill(WHITE)
    done, score = manager.process(pg.event.get(), screen)
    pg.display.flip()

pg.quit()

