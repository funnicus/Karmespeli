# Kärmespeli
# Soveltava projekti 2020
# Johanna Seulu, Juhana Kuparinen, Juho Ollila

VERSION = 0.2

import pygame, sys
from pygame.locals import *


# Snake luokka joka perii Sprite luokan
class Snake(pygame.sprite.Sprite):
    x = 0
    y = 200
    pos = (x, y)
    direction = "left"

    def __init__(self):
        self.x = 0
        self.image = pygame.image.load('blocksnake.png')

    def update(self):
        if self.direction == "right":
            self.x += 1

        if self.direction == "left":
            self.x -= 1

        if self.direction == "up":
            self.y -= 1

        if self.direction == "down":
            self.y += 1

        self.pos = (self.x, self.y)

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

    # Pythonissa luokan konstruktori on __init__.
    # Luokan sisällä olevien funktioiden ensimmäinen argumentti on aina
    # olioon itseensä viittaavan muuttujan nimi (Javan this -avainsana).
    # Pythonissa on tapana nimittää tätä muuttujaa nimellä self,
    # mutta ohjelmoija voi halutessaan käyttää myös jotain muuta nimitystä tälle.
    def __init__(self):
        self.running = True
        self.snake = Snake()

    def game_loop(self):
        # Peli looppi
        self.display_screen.fill((0, 0, 0))
        while self.running:
            # Varmistetaan että peli ei mene yli 60 fps:n
            self.clock.tick(60)
            self.drawGrid()
            self.snake.update()
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
        icon = pygame.image.load('icon.png')
        pygame.display.set_caption("Kärmespeli")
        pygame.display.set_icon(icon)

        # Käynnistetään itse peli...
        self.game_loop()

    # drawGrid() -metodi piirtää Kärmespeliin ruudukon
    def drawGrid(self):
        gridSize = 20
        for i in range(self.windowWidth):
            for j in range(self.windowHeight):
                rect = pygame.Rect(i*gridSize, j*gridSize, gridSize, gridSize)
                pygame.draw.rect(self.display_screen, (255, 255, 255), rect, 1)


if __name__ == "__main__":
    App = Game()
    App.start_game()
