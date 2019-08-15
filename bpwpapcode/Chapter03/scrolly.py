background_image_filename = 'sushiplate.jpg'
SCREEN_SIZE = (1920, 1080)
# message = "   中文 This is a demonstration of the scrolly message script.   "
message = "在網上下載一箇中文字型檔案，將這個檔案與我們的程式放在同一個資料夾，如果是中文的檔名，將它改"

from sys import exit

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)

# font = pygame.font.SysFont("Arial", 80)
font = pygame.font.SysFont("yugothicyugothicuisemiboldyugothicuibold", 80)
text_surface = font.render(message, True, (0, 0, 255))

clock = pygame.time.Clock()  # 建立時間元件

x = 0
y = (SCREEN_SIZE[1] - text_surface.get_height()) / 2

background = pygame.image.load(background_image_filename).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    for i in range(3):
        for j in range(3):
            screen.blit(background, (i * 640, j * 480))

    fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
    screen.blit(fps, (50, 50))

    x -= 10
    if x < -text_surface.get_width():
        x = 0

    screen.blit(text_surface, (x, y))
    screen.blit(text_surface, (x + text_surface.get_width(), y))

    #  pygame.display.update()
    pygame.display.flip()

    #  clock.tick(30)  # 每秒 30 次
