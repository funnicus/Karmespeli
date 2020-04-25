import pygame
import random

class Obstacle:

    def __init__(self, width, height):
        self.height = height
        self.width = width

        self.stone = pygame.image.load('pictures/kivi.png')
        self.bush = pygame.image.load('pictures/pensas.png')
        self.corona = pygame.image.load('pictures/korona.png')

        self.stone = pygame.transform.scale(self.stone, (20, 20))
        self.bush = pygame.transform.scale(self.bush, (20, 20))
        self.corona = pygame.transform.scale(self.corona, (20, 20))

    def newObstacle(self, gridSize):
        self.randomObstacle = random.randint(0, 101)
        self.x = random.randint(0, self.width-1)
        self.y = random.randint(4, self.height-1)
        self.location = (self.x, self.y)
        self.obstacle = pygame.Rect(self.x * gridSize, self.y * gridSize, gridSize, gridSize)

    def drawObstacle(self):
        if self.randomObstacle > 98:
            pygame.display.get_surface().blit(self.corona, self.obstacle)
        elif self.randomObstacle < 50:
            pygame.display.get_surface().blit(self.bush, self.obstacle)
        else:
            pygame.display.get_surface().blit(self.stone, self.obstacle)

    def obstacleLocation(self):
        return self.location