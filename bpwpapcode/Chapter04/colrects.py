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

    screen.lock()
    for count in range(10):
        random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
        random_pos = (randint(0, 639), randint(0, 479))
        random_size = (639 - randint(random_pos[0], 639), 479 - randint(random_pos[1], 479))
        pygame.draw.rect(screen, random_color, (random_pos, random_size))
    screen.unlock()

    pygame.display.update()
