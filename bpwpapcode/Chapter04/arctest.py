#!/usr/bin/env python

from sys import exit

import pygame
from math import pi
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    x, y = pygame.mouse.get_pos()
    angle = (x / 639.) * pi * 2.
    screen.fill((255, 255, 255))
    pygame.draw.arc(screen, (0, 0, 0), (0, 0, 639, 479), 0, angle)

    pygame.display.update()
