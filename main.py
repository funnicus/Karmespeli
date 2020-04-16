# Kärmespeli
# Soveltava projekti 2020
# Johanna Seulu, Juhana Kuparinen, Juho Ollila

VERSION = 0.2

import pygame, sys
import math
from pygame.locals import *


# Snake luokka joka perii Sprite luokan
class Snake(pygame.sprite.Sprite):
    snake = [(20, 20), (19, 20), (18, 20), (17, 20), (16, 20)]
    direction = "left"

    def __init__(self):
        self.image = pygame.image.load('blocksnake.png')

    def update(self, gridSize):

        if self.direction == "right":
            newSnake = []
            x, y = self.snake[0]
            newSnake.append((x+1, y))
            for i in range(1, len(self.snake)):
                newSnake.append(self.snake[i-1])
            self.snake = newSnake

        if self.direction == "left":
            newSnake = []
            x, y = self.snake[0]
            newSnake.append((x-1, y))
            for i in range(1, len(self.snake)):
                newSnake.append(self.snake[i-1])
            self.snake = newSnake

        if self.direction == "up":
            newSnake = []
            x, y = self.snake[0]
            newSnake.append((x, y-1))
            for i in range(1, len(self.snake)):
                newSnake.append(self.snake[i-1])
            self.snake = newSnake

        if self.direction == "down":
            newSnake = []
            x, y = self.snake[0]
            newSnake.append((x, y+1))
            for i in range(1, len(self.snake)):
                newSnake.append(self.snake[i-1])
            self.snake = newSnake

        # Pään koordinaatit
        for i in range(len(self.snake)):
            x, y = self.snake[i]
            rect = pygame.Rect(x * gridSize, y * gridSize, gridSize, gridSize)
            pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), rect, 0)

    def moveUp(self):
        self.direction = "up"

    def moveRight(self):
        self.direction = "right"

    def moveDown(self):
        self.direction = "down"

    def moveLeft(self):
        self.direction = "left"


class Game:
    windowWidth = 800
    windowHeight = 800
    screenResolution = (windowWidth, windowHeight)
    clock = pygame.time.Clock()
    snake = 0

    # Pythonissa luokan konstruktori on __init__.
    # Luokan sisällä olevien funktioiden ensimmäinen argumentti on aina
    # olioon itseensä viittaavan muuttujan nimi (Javan this -avainsana).
    # Pythonissa on tapana nimittää tätä muuttujaa nimellä self,
    # mutta ohjelmoija voi halutessaan käyttää myös jotain muuta nimitystä tälle.
    def __init__(self):
        self.running = True

    def game_loop(self):
        # Peli looppi
        while self.running:
            # Varmistetaan että peli ei mene yli 10 fps:n (kärmes lentäisi valonnopeudella muuten...)
            self.clock.tick(10)
            self.drawGrid()
            self.snake.update(self.gridSize)
            # Tapahtuma looppi
            for event in pygame.event.get():
                # Kaksi ensimmäistä if lausetta käsittelevät pelistä poistumisen
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        self.running = False

                    if event.key == K_RIGHT:
                        self.snake.moveRight()

                    if event.key == K_LEFT:
                        self.snake.moveLeft()

                    if event.key == K_UP:
                        self.snake.moveUp()

                    if event.key == K_DOWN:
                        self.snake.moveDown()

            # blit() metodilla piirretään näytölle
            #self.display_screen.blit(self.background, (0, 0))
            #self.display_screen.blit(self.snake.image, self.snake.pos)
            # Metodia flip kutsutaan jotta näyttö päivittyy
            # pygame.display.flip()
            pygame.display.update()

    # Funktio jolla aloitetaan peli
    def start_game(self):
        # pygame.init() -metodia täytyy kutsua, jotta pelimootroi
        # käynnistyy.
        pygame.init()

        # Määritellään näytön ominaisuuksia kuten resoluutio...
        self.display_screen = pygame.display.set_mode(self.screenResolution)
        self.gridSize = 20
        self.snake = Snake()
        icon = pygame.image.load('icon.png')
        pygame.display.set_caption("Kärmespeli")
        pygame.display.set_icon(icon)

        # Käynnistetään itse peli...
        self.game_loop()

    # drawGrid() -metodi piirtää Kärmespeliin ruudukon
    def drawGrid(self):
        for i in range(math.floor(self.windowWidth / (self.gridSize))):
            for j in range(math.floor(self.windowHeight / (self.gridSize))):
                rect = pygame.Rect(i*self.gridSize, j*self.gridSize, self.gridSize, self.gridSize)
                # Piirretään ruudukko. If else lauseilla tarkistetaan minkä värinen
                # ruutu tulee olemaan.
                if i % 2 == 0:
                    if j % 2 == 0:
                        pygame.draw.rect(self.display_screen, (0, 255, 0), rect, 0)
                    else:
                        pygame.draw.rect(self.display_screen, (0, 230, 0), rect, 0)
                else:
                    if j % 2 == 0:
                        pygame.draw.rect(self.display_screen, (0, 230, 0), rect, 0)
                    else:
                        pygame.draw.rect(self.display_screen, (0, 255, 0), rect, 0)

if __name__ == "__main__":
    App = Game()
    App.start_game()
