#!/usr/bin/env python

from random import *
from sys import exit

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    random_pos = (randint(0, 639), randint(0, 479))
    random_radius = randint(1, 200)
    pygame.draw.circle(screen, random_color, random_pos, random_radius)

    pygame.display.update()
