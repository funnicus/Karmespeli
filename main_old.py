# Tämä on vanha tiedosto jonka voi jättää huomioimatta

import pygame, sys

#framerate
clock = pygame.time.Clock()

# Pelimoottorin käynnistys
from pygame.locals import *
pygame.init()



# Luodaan pelin-ruutu
WINDOWWIDTH = 1500
WINDOWHEIGHT = 800
WINDOW_SIZE = (WINDOWWIDTH, WINDOWHEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Nimi ja ikoni
icon = pygame.image.load('icon.png')
pygame.display.set_caption("Kärmespeli")
pygame.display.set_icon(icon)

# Peli looppi
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            print('exit...')
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.display.update()
    # 60 fps
    clock.tick(60)