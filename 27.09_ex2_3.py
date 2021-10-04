import pygame
import math
from pygame.draw import *

pygame.init()

FPS = 30
WINDOW_HEIGHT=300
WINDOW_WIDTH=700
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

WHITE=(0,0,0)
BLACK=(255,255,255)

GRASS_COLOR=(14, 147, 37)

SKY_COLOR=(161, 235, 245)
SKY_HEIGHT=65

SUN_PARTS_NUM=30
SUN_COLOR=(249, 194, 194)
SUN_RADIUS=50

NUMBER_OF_TREES=3
TREE_COLOR=(15, 83, 14)
TREES_X_COORDINATES=(300 , 600 ,100)
TREES_Y_COORDINATES=(60 , 50 , 75)
TREES_K=( 0.8 , 1.2 , 1)

HOUSE_WALL_COLOR=(147, 107, 14)
HOUSE_ROOF_COLOR=(235, 47, 68)
HOUSE_WINDOW_COLOR=(14, 147, 145)
HOUSE_WINDOW_FRAME_COLOR= (181, 98, 17)

SUN_POLYGON_COORDINATES = list()
big_n_polygon = list()
small_n_polygon = list()


def Parts_of_sun(big_parts, small_parts, x_center, y_center, radius):
    '''
    Zapisuvaet coordinati solnca

    big_parts - coordinati vipukluh uglov
    small_parts - coordinati vnutrennih uglov
    x_center,y_center - coordinati centra
    radius - radius solnca
    '''
    part_big = tuple()
    part_small = tuple()
    for i in range(SUN_PARTS_NUM):
        part_big = (x_center + radius * math.cos(2 * math.pi * i/SUN_PARTS_NUM)), (y_center + radius * math.sin(2 * math.pi * i/SUN_PARTS_NUM))
        part_small = (x_center + 0.9 * radius * math.cos(2 * math.pi / 40 + 2 * math.pi * i/SUN_PARTS_NUM)), (y_center + 0.9 * radius * math.sin(2 * math.pi / 40 + 2 * math.pi * i/SUN_PARTS_NUM))
        big_parts.append(part_big)
        small_parts.append(part_small)

def house(x, y, k):
    '''
    Risuet dom s uvelicheniem v k raz

    x,y - coodinati dereva
    k - coefficient uvelicheniya
    '''
    polygon(screen, WHITE, [(x - 2, y + 2), (x+110.0*k + 2, y + 2), (x + 110.0 * k + 2,y + 75.0 * k - 2), (x - 2, y + 75.0 * k - 2)])
    HOUSE_WIDTH = 110.0 * k
    HOUSE_HEIGHT = 75.0 * k
    polygon(screen, HOUSE_WALL_COLOR , [(x, y), (x + 110.0 * k, y), (x+110.0*k,y+75.0*k), (x, y+75.0*k)])
    polygon(screen, HOUSE_ROOF_COLOR , [(x + HOUSE_WIDTH, y), (x, y), (x + HOUSE_WIDTH/2, y - 0.5*HOUSE_HEIGHT )])
    polygon(screen, HOUSE_WINDOW_FRAME_COLOR, [(x + 38.0 * k, y + 40.0 * k), (x + 77.0 * k, y + 40.0 * k)], int(32 * k))
    polygon(screen, HOUSE_WINDOW_COLOR, [(x + 40.0 * k, y + 40.0 * k), (x + 75.0 * k, y + 40.0 * k)], int(30 * k))

def clouds(x, y, k):

    '''
    risuet oblaka s uvelicheniem v k raz

    x,y - coodinati dereva
    k - coefficient uvelicheniya
    '''

    for i in range(2):
        circle(screen, WHITE, (x + i * int(15 * k), y), int(14 * k) + 1)
        circle(screen, BLACK, (x + i * int(15 * k), y), int(14 * k))

    for i in range (4):
        circle(screen, WHITE, (x + i * int(15 * k) - 15, y + 15), int(14 * k) + 1)
        circle(screen, BLACK, (x + i * int(15 * k) - 15, y + 15), int(14 * k))

def tree(x, y, k):
    '''
    Risuet derevo s uvelicheniem

    x,y - coodinati dereva
    k - coefficient uvelicheniya
    '''

    polygon(screen, WHITE, [(x-5 * k, y), (x-5 * k, y + 50 * k), (x+5 * k, y + 50 * k), (x+5, y)])

    circle(screen, WHITE, (x - 15 * k, y - 5 * k), int(15 * k))
    circle(screen, TREE_COLOR, (x - 15 * k, y - 5 * k), int(14 * k))

    circle(screen, WHITE, (x - 15 * k, y - 20 * k), int(15 * k))
    circle(screen, TREE_COLOR, (x - 15 * k, y - 20 * k), int(14 * k))

    circle(screen, WHITE, (x, y - 13 * k), int(15 * k))
    circle(screen, TREE_COLOR, (x, y - 13 * k), int(14 * k))

    circle(screen, WHITE, (x, y - 28 * k), int(15 * k))
    circle(screen, TREE_COLOR, (x, y - 28 * k), int(14 * k))

    circle(screen, WHITE, (x + 20 * k, y - 5 * k), int(15 * k))
    circle(screen, TREE_COLOR, (x + 20 * k, y - 5 * k), int(14 * k))

    circle(screen, WHITE, (x + 20 * k, y - 20 * k), int(15 * k))
    circle(screen, TREE_COLOR, (x + 20 * k, y - 20 * k), int(14 * k))



polygon(screen, (SKY_COLOR), [(0, SKY_HEIGHT), (WINDOW_WIDTH, SKY_HEIGHT)], 150) #risuet nebo

polygon(screen, (GRASS_COLOR), [(0, WINDOW_HEIGHT-SKY_HEIGHT-20), (WINDOW_WIDTH, WINDOW_HEIGHT-SKY_HEIGHT-20)], 150) #risuet travy

tree(400, 140, 1) #risuet derevo

house(50, 145, 1)   #risuet dom

tree(200, 155, 0.8) #risuet derevo

house(500, 160, 0.8)    #risuet dom

for iter in range(NUMBER_OF_TREES):
    clouds(TREES_X_COORDINATES[iter], TREES_Y_COORDINATES[iter], TREES_K[iter])


Parts_of_sun(big_n_polygon, small_n_polygon, 500, 75, SUN_RADIUS)

for iter in range(SUN_PARTS_NUM):
    '''
    Zapisuvaet coordinati solnca v odin spisok

    SUN_PARTS_NUM - spisok dlya coordinat
    '''
    SUN_POLYGON_COORDINATES.append(big_n_polygon[iter])
    SUN_POLYGON_COORDINATES.append(small_n_polygon[iter])

polygon(screen , SUN_COLOR , SUN_POLYGON_COORDINATES) #risuet solnce



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
