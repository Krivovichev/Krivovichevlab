import pygame
from pygame.draw import *
import math

pygame.init()

BLACK = (0, 0, 0)
WHITE = (237, 237, 200)
GREEN = (128, 255, 38)
DARK_GREEN = (0, 129, 0)
YELLOW = (255, 255, 0)
RED = (255, 38, 37)
PINK = (234, 199, 177)
ORANGE = (255, 102, 0)
VIOLET = (213, 38, 255)
BLUE = (129, 180, 255)
BROWN = (121, 66, 27)
GRAY = (191, 201, 184)

sc = pygame.display.set_mode((1700, 1000))

########################################################################################################################
'''
Функция draw_a_boy рисует мальчика с плакатом. Входные данные: dx, dy, poster type, shirt_color, hair_color, M
(dx, dy) -координаты центра тела
poster type - тип надписи на плакате
shirt_color - цвет одежды
hair_color - цвет волос
M - масштаб, коэффициент на который умножаются изначальные линейные размеры 
'''
def draw_a_boy(dx, dy, poster_type, shirt_color, eye_color, hair_color, M):
    
    body = circle(sc, shirt_color, (dx, dy), int(200*M))
    face = circle(sc, PINK, (dx, dy - int(250*M)), int(150*M))

    eye_left = ellipse(sc, eye_color, (dx - int(80 * M), dy -  int(320 *M), int(70*M), int(50*M)), 0)
    eye_right = ellipse(sc, eye_color, (int(10 * M) + dx, dy - int(320 * M) , int(70*M), int(50*M)), 0)
    eye_left = ellipse(sc, BLACK, (dx - int(80* M), dy- int(320 * M), int(70*M), int(50*M)), 1)
    eye_right = ellipse(sc, BLACK, (int(10 * M) + dx, dy- int(320 * M), int(70*M), int(50*M)), 1)
    eye1_left = circle(sc, BLACK, (dx - int(50*M), dy - int(295 *M)), int(10 * M))
    eye1_right = circle(sc, BLACK, (int(50*M) + dx, dy - int(295 *M)), int(10 * M))

    nose = polygon(sc, BROWN, ((dx - int(20 * M), dy- int(250 * M)), (int(20 * M) + dx, dy- int(250 * M)), (dx, dy - int(230 *M))))
    mouth = polygon(sc, RED, ((dx - int(70* M), dy - int(210 * M)), (int(70 * M) + dx, dy - int(210 * M)), (dx, dy - int(170 * M))))
    nose = polygon(sc, BLACK, ((dx - int(20 * M), dy - int(250 * M)), (int(20 * M) + dx, dy - int(250 * M)), (dx, dy - int(230 * M))), 1)
    mouth = polygon(sc, BLACK, ((dx - int(70 * M), dy - int(210 * M)), (int(70 * M) + dx, dy - int(210 * M)), (dx, dy - int(170 * M))), 1)

    def regular_polygon(x0, y0, R, n):
        vertex_coord = []
        phi = (n - 2) / n * math.pi
        for i in range(n):
            xi = x0 + R * math.cos(phi + 2 * math.pi * i / n)
            yi = y0 + R * math.sin(phi + 2 * math.pi * i / n)
            vertex_coord.append((xi, yi))
        return vertex_coord

    def rotated_rectangle(a, b, x0, y0, alpha):
        beta = math.atan(b / a)
        d = math.sqrt((a * a) + (b * b))
        alpha = alpha / 180 * math.pi
        x1 = x0 + (d * math.cos(alpha + (math.pi - beta)) / 2)
        y1 = y0 + (d * math.sin(alpha + (math.pi - beta)) / 2)
        x2 = x0 + (d * math.cos(alpha + beta) / 2)
        y2 = y0 + (d * math.sin(alpha + beta) / 2)
        x3 = x0 + (d * math.cos(alpha - beta) / 2)
        y3 = y0 + (d * math.sin(alpha - beta) / 2)
        x4 = x0 + (d * math.cos(alpha - (math.pi - beta)) / 2)
        y4 = y0 + (d * math.sin(alpha - (math.pi - beta)) / 2)
        vert = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        return vert

    arm_left = polygon(sc, PINK, (rotated_rectangle(int(400 * M), int(30 * M), dx - int(300 * M) , dy - int(310 * M) , 70)))
    arm_right = polygon(sc, PINK, (rotated_rectangle(int(400 * M), int(30 * M), int(300 * M) + dx , dy - int(310 * M), 110)))
    surf1 = pygame.Surface((int(200*M), int(200*M)), pygame.SRCALPHA)
    shoulder_left = polygon(sc, shirt_color, (regular_polygon(dx - int(200 * M), dy - int(100 * M) , int(70 * M), 5)))
    shoulder_right = polygon(surf1, shirt_color, (regular_polygon(int(100 * M), int(100 * M), int(70*M), 5)))
    shoulder_right = polygon(surf1, BLACK, (regular_polygon(int(100*M), int(100*M), int(70*M), 5)), 1)
    surf2 = pygame.transform.rotate(surf1, -45)
    sc.blit(surf2, (int (60 * M) + dx, dy - int(240 * M)))
    shoulder_left = polygon(sc, BLACK, (regular_polygon(dx- int(200 * M), dy- int(100 * M), int(M * 70), 5)), 1)
    
    hand_left = ellipse(sc, PINK, [dx- int(400 * M), dy - int(600*M), int(60*M), int(120*M)])
    hand_right = ellipse(sc, PINK, [int(340 * M) + dx, dy- int(600*M), int(60*M), int(120*M)])
    hand_left = ellipse(sc, WHITE, [dx- int(400 * M), dy-int(600*M), int(60*M), int(120*M)], 1)
    hand_right = ellipse(sc, WHITE, [int(340*M) + dx, dy-int(600*M), int(60*M), int(120*M)], 1)

    # hair
    def stuck_polygons(angle, k, x0, y0, sign, R):
        for i in range(k):
            surf3 = pygame.Surface((int(M*50), int(M*50)), pygame.SRCALPHA)
            triangle = polygon(surf3, hair_color, ((0, int(M*50)), (int(M*50), int(M*50)), (int(M*25), 0)))
            triangle = polygon(surf3, BLACK, ((0, int(M*50)), (int(M*50), int(M*50)), (int(M*25), 0)), 1)
            surf4 = pygame.transform.rotate(surf3, 90 - angle * i)

            X = R * math.cos(angle * i / 180 * math.pi)
            sc.blit(surf4, (dx - int(30*M) - X , dy -int(290*M) - math.sqrt(R ** 2 - X ** 2)))

    stuck_polygons(16, 12, 470, 410, 1, int(170*M))

    rect(sc, GREEN, (dx - int(400*M), dy-int(600*M), int(800*M), int(100*M)))

    font = pygame.font.Font(None, int(64*M))
    if poster_type == 1:
        rect(sc, GREEN,(dx - int(400*M), dy-int(600*M), int(800*M), int(100*M)) )
        text = font.render("PYTHON is AMAZING", 1, BLACK)
        place = text.get_rect(center=(dx, dy-int(550*M)))
    else:
        rect(sc, GREEN,(dx - int(400*M), dy-int(600*M), int(800*M), int(100*M)) )
        text = font.render("PYTHON is REALLY AMAZING", 1, WHITE)
        place = text.get_rect(center=(dx, dy -int(550*M)))

    sc.blit(text, place)


draw_a_boy(1230, 700, 2, ORANGE, BLUE, VIOLET, 1)
draw_a_boy(500, 700,  2, DARK_GREEN, GRAY, YELLOW, 1)

pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    pygame.time.delay(20)
