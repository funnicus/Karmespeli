"""
    Apple -luokka, jonka avulla piirrämme omenoita peliin. Luokka pitää huolen myös
    omenoihin liittyvistä laskutoimituksista.

    Attributes
    =========

    width : int
    height : int
    x : int
    y : int
    location : coordinate
    apple : Rect
    img : png

    Params
    ======

    width : int
    height : int

    Methods
    =======

    newApple : void
    drawApple : void
    appleLocation : coordinate

"""

import pygame
import random

class Apple:

    def __init__(self, width, height):
        self.height = height
        self.width = width
    # Luodaan uusi omena. Parametrina gridSize, jonka avulla metodi tietää, minkä kokoinen
    # omena on.
    def newApple(self, gridSize):
        self.x = random.randint(0, self.width-1)
        self.y = random.randint(4, self.height-1)
        self.location = (self.x, self.y)
        self.apple = pygame.Rect(self.x * gridSize, self.y * gridSize, gridSize, gridSize)
        self.img = pygame.image.load('pictures/Matopeli_omena.png')
        self.img = pygame.transform.scale(self.img, (gridSize, gridSize))

    # Nimensä mukaisesti piirtää omenan ruudulle
    def drawApple(self):
        pygame.display.get_surface().blit(self.img, self.apple)
        #pygame.draw.rect(pygame.display.get_surface(), (200, 0, 0), self.apple, 0)

    # Palauttaa omenan sijainnin ruudukolla
    def appleLocation(self):
        return self.location