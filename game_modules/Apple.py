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

    def drawApple(self):
        pygame.draw.rect(pygame.display.get_surface(), (200, 0, 0), self.apple, 0)

    def appleLocation(self):
        return self.location