import pygame
import math
import random
from enum import Enum

# Snake luokka joka perii Sprite luokan
class Snake(pygame.sprite.Sprite):

    # Luodaan enum luokka, joka määrittelee käärmeen suunnat
    class Directions(Enum):
        Stop = 0
        Right = 1
        Left = 2
        Up = 3
        Down = 4

    direction = Directions.Right

    def __init__(self, width, height, color):
        self.headImg = pygame.image.load('pictures/Matopeli_mato_paa.png')
        self.bodyImg = pygame.image.load('pictures/Matopeli_mato_paa.png')
        self.tailImg = pygame.image.load('pictures/Matopeli_mato_paa.png')

        self.headImg = pygame.transform.scale(self.headImg, (20, 20))
        self.bodyImg = pygame.transform.scale(self.headImg, (20, 20))
        self.tailImg = pygame.transform.scale(self.headImg, (20, 20))

        self.gridWidth = width
        self.gridHeight = height
        self.snake = [
                    (int(self.gridWidth/2), int(self.gridHeight/2)),
                    (int(self.gridWidth/2)-1, int(self.gridHeight/2)),
                    (int(self.gridWidth/2)-2, int(self.gridHeight/2)),
                    (int(self.gridWidth/2)-3, int(self.gridHeight/2)),
                    (int(self.gridWidth/2)-4, int(self.gridHeight/2))
                      ]
        self.snakeHead = self.snake[0]
        self.color = color

    # update() metodilla liikutamme käärmettä.
    def update(self, gridSize):
        if self.direction == self.Directions.Right:
            newSnake = []
            x, y = self.snake[0]
            newSnake.append((x+1, y))
            for i in range(1, len(self.snake)):
                newSnake.append(self.snake[i-1])
            self.snake = newSnake

        if self.direction == self.Directions.Left:
            newSnake = []
            x, y = self.snake[0]
            newSnake.append((x-1, y))
            for i in range(1, len(self.snake)):
                newSnake.append(self.snake[i-1])
            self.snake = newSnake

        if self.direction == self.Directions.Up:
            newSnake = []
            x, y = self.snake[0]
            newSnake.append((x, y-1))
            for i in range(1, len(self.snake)):
                newSnake.append(self.snake[i-1])
            self.snake = newSnake

        if self.direction == self.Directions.Down:
            newSnake = []
            x, y = self.snake[0]
            newSnake.append((x, y+1))
            for i in range(1, len(self.snake)):
                newSnake.append(self.snake[i-1])
            self.snake = newSnake

        # Päivitetään pään sijainti
        self.snakeHead = self.snake[0]
        # Käärmeen piirtäminen
        for i in range(len(self.snake)):
            x, y = self.snake[i]
            rect = pygame.Rect(x * gridSize, y * gridSize, gridSize, gridSize)
            #imgrect = self.headImg.get_rect()
            pygame.display.get_surface().blit(self.headImg, rect)
            #pygame.draw.rect(pygame.display.get_surface(), self.color, rect, 0)
            '''# Gradientti kärmes
            if 255-(i*2) > 0:
                pygame.draw.rect(pygame.display.get_surface(), (255-(i*2), 0, 0), rect, 0)
            else:
                pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0), rect, 0)
            '''
    # Metodit, joilla vaihdetaan käärmeen suuntaa.
    def moveRight(self):
        if self.direction != self.Directions.Left:
            self.direction = self.Directions.Right

    def moveLeft(self):
        if self.direction != self.Directions.Right:
            self.direction = self.Directions.Left

    def moveUp(self):
        if self.direction != self.Directions.Down:
            self.direction = self.Directions.Up

    def moveDown(self):
        if self.direction != self.Directions.Up:
            self.direction = self.Directions.Down

    def snakeLocation(self):
        return self.snake[0]

    def growSnake(self):
        x, y = self.snake[len(self.snake)-1]
        if self.direction != 2:
            self.snake.append((x-1, y))
        else:
            self.snake.append((x+1, y))

    def isOnScreen(self, width, height):
        x, y = self.snake[0]
        if x >= width or y >= height or x < 0 or y < 4:
            return False
        return True

    def isOnApple(self, appleLocation):
        for i in range(len(self.snake)):
            if self.snake[i] == appleLocation:
                return True
        return False

    def collideWithSelf(self):
        for i in range(1, len(self.snake)):
            if self.snake[0] == self.snake[i]:
                return True
        return False

    def collideWithOther(self, other):
        for i in range(0, len(self.snake)):
            if other == self.snake[i]:
                return True
        return False