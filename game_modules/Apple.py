import pygame
import random

class Apple:

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def newApple(self, gridSize):
        self.x = random.randint(0, self.width-1)
        self.y = random.randint(4, self.height-1)
        self.location = (self.x, self.y)
        self.apple = pygame.Rect(self.x * gridSize, self.y * gridSize, gridSize, gridSize)
        self.img = pygame.image.load('pictures/Matopeli_omena.png')
        self.img = pygame.transform.scale(self.img, (20, 20))

    def drawApple(self):
        pygame.display.get_surface().blit(self.img, self.apple)
        #pygame.draw.rect(pygame.display.get_surface(), (200, 0, 0), self.apple, 0)

    def appleLocation(self):
        return self.location