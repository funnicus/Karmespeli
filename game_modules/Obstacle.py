import pygame
import random

class Obstacle:

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def newObstacle(self, gridSize):
        self.x = random.randint(0, self.width-1)
        self.y = random.randint(4, self.height-1)
        self.location = (self.x, self.y)
        self.obstacle = pygame.Rect(self.x * gridSize, self.y * gridSize, gridSize, gridSize)

    def drawObstacle(self):
        pygame.draw.rect(pygame.display.get_surface(), (200, 0, 200), self.obstacle, 0)

    def obstacleLocation(self):
        return self.location