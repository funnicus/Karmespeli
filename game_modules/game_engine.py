import pygame, sys
import math
import random
from enum import Enum
from typing import Tuple
from pygame.locals import *
from game_modules.Snake import Snake
from game_modules.Apple import Apple
from game_modules.Obstacle import Obstacle

#################################
# MENU LUOKKA
#################################

class Menu:
    # Kun peli käynnistetään, tällä enum -luokalla tiedetään
    # mikä vaikeustaso on.
    class Difficulties(Enum):
        Easy = 0
        Normal = 1
        Hard = 2

    # Kun peli käynnistetään, tällä enum -luokalla tiedetään
    # mikä vaikeustaso on.
    class Gamemodes(Enum):
        Solo = 1
        Duel = 2

    menuWidth = 800
    menuHeight = 600
    menuResolution = (menuWidth, menuHeight)
    clock = pygame.time.Clock()
    menu_screen = pygame.display.set_mode(menuResolution)

    #Määritellään valmiiksi värejä RGB arvojen avulla
    black = (10, 10, 10)
    white = (255, 255, 255)
    green = (150, 185, 150)
    light_green = (150, 255, 150)
    red = (185, 150, 150)
    light_red = (255, 150, 150)
    gray = (150, 150, 150)
    light_gray = (200, 200, 200)
    light_yellow = (255, 255, 102)
    yellow = (255, 255, 204)

    def __init__(self):
        self.running = True

    def drawText(self, text, font, textColor, location):
        textSurface, textRectangle = self.text_object(text, font, textColor)
        textRectangle.center = location
        self.menu_screen.blit(textSurface, textRectangle)

    def text_object(self, text, font, colour):
        textSurface = font.render(text, True, colour)
        return textSurface, textSurface.get_rect()


    # ic = inactive colour eli väri joka on käytössä kun hiiri ei ole napin päällä
    # ac = active colour eli väri joka tulee käyttöön kun hiirellä mennään napin päälle
    def button(self, message, x, y, width, height, ic, ac, action=None, fontsize=None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Näppäimen luominen
        #Kun hiiri on näppäimen päällä
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.menu_screen, ac, (x, y, width, height))
            #Tapahtuma kun hiirellä klikkaa
            if click[0] == 1 and action != None:
                # Päävalikon toiminnot
                if action == "playsp":
                    self.sp_select()
                if action == "playmp":
                    self.duel_select()
                elif action == "quit":
                    pygame.quit()
                    quit()
                elif action == "credits":
                    self.credits()
                elif action == "menu":
                    self.main_menu()
                # Vaikeustason valintavalikon toiminnot
                #1 pelaaja
                elif action == "easy":
                    Peli = Game(self.Difficulties.Easy, self.Gamemodes.Solo)
                    Peli.start_game(400, 400)
                elif action == "normal":
                    Peli = Game(self.Difficulties.Normal, self.Gamemodes.Solo)
                    Peli.start_game(600, 600)
                elif action == "hard":
                    Peli = Game(self.Difficulties.Hard, self.Gamemodes.Solo)
                    Peli.start_game(800, 600)
                #2 pelaajaa
                elif action == "easy_duel":
                    Peli = Game(self.Difficulties.Easy, self.Gamemodes.Duel)
                    Peli.start_game(400, 400)
                elif action == "normal_duel":
                    Peli = Game(self.Difficulties.Normal, self.Gamemodes.Duel)
                    Peli.start_game(600, 600)
                elif action == "hard_duel":
                    Peli = Game(self.Difficulties.Hard, self.Gamemodes.Duel)
                    Peli.start_game(800, 600)

        #Kun hiiri ei ole näppäimen päällä
        else:
            pygame.draw.rect(self.menu_screen, ic, (x, y, width, height))

        # Teksti
        if fontsize != None:
            font = pygame.font.Font('fonts/OpenSans-Regular.ttf', fontsize)
            self.drawText(message, font, self.black, ((x + width / 2), y + 35))
        else:
            font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 40)
            self.drawText(message, font, self.black, ((x + width/2), y + 35))

    # Aloitus valikko pelille
    def main_menu(self):

        self.menuWidth = 800
        self.menuHeight = 600
        self.menuResolution = (self.menuWidth, self.menuHeight)
        self.menu_screen = pygame.display.set_mode(self.menuResolution)

        pygame.init()
        icon = pygame.image.load('pictures/icon.png')
        pygame.display.set_caption("Kärmespeli")
        pygame.display.set_icon(icon)
        menu = True

        # Valikko looppi
        while menu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

            # Main menu otsikko ja tausta
            self.menu_screen.fill(self.black)
            text = "KÄRMESPELI"
            font = pygame.font.Font('fonts/OpenSans-Bold.ttf', 100)
            self.drawText(text, font, self.white,(math.floor((self.menuWidth / 2)), 100))

            # Nappien luonti
            self.button("YKSINPELI", 160, 200, 500, 75, self.green, self.light_green, "playsp")
            self.button("KAKSINPELI", 160, 300, 500, 75, self.green, self.light_green, "playmp")
            self.button("TEKIJÄT", 160, 400, 500, 75, self.gray, self.light_gray, "credits")
            self.button("SULJE PELI", 160, 500, 500, 75, self.red, self.light_red, "quit")

            pygame.display.update()
            self.clock.tick(15)

    # Tekijä valikko
    def credits(self):

        credits = True
        while credits:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

            self.menu_screen.fill((10, 10, 10))

            text = "Juhana Kuparinen"
            font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 50)
            self.drawText(text, font, self.white, (400, 200))

            text = "Juho Ollila"
            font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 50)
            self.drawText(text, font, self.white, (400, 300))

            text = "Johanna Seulu"
            font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 50)
            self.drawText(text, font, self.white, (400, 400))

            pygame.display.update()
            pygame.time.wait(5000)
            self.main_menu()

    # Tason valinta valikko
    def sp_select(self):
        pygame.init()

        self.menuWidth = 800
        self.menuHeight = 600
        self.menuResolution = (self.menuWidth, self.menuHeight)
        self.menu_screen = pygame.display.set_mode(self.menuResolution)
        level = True
        while level:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
            self.menu_screen.fill(self.black)
            self.button("HELPPO", 160, 200, 500, 75, self.green, self.light_green, "easy")
            self.button("NORMAALI", 160, 300, 500, 75, self.yellow, self.light_yellow, "normal")
            self.button("VAIKEA", 160, 400, 500, 75, self.red, self.light_red, "hard")
            pygame.display.update()
            self.clock.tick(15)

    def duel_select(self):
        pygame.init()

        self.menuWidth = 800
        self.menuHeight = 600
        self.menuResolution = (self.menuWidth, self.menuHeight)
        self.menu_screen = pygame.display.set_mode(self.menuResolution)
        level = True
        while level:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
            self.menu_screen.fill(self.black)
            self.button("HELPPO", 160, 200, 500, 75, self.green, self.light_green, "easy_duel")
            self.button("NORMAALI", 160, 300, 500, 75, self.yellow, self.light_yellow, "normal_duel")
            self.button("VAIKEA", 160, 400, 500, 75, self.red, self.light_red, "hard_duel")
            pygame.display.update()
            self.clock.tick(15)


#################################
# GAME LUOKKA
#################################

class Game:
    windowWidth = 800
    windowHeight = 600
    screenResolution = (windowWidth, windowHeight)
    clock = pygame.time.Clock()
    snake = 0
    score1 = 0
    score2 = 0

    # Pythonissa luokan konstruktori on __init__.
    # Luokan sisällä olevien funktioiden ensimmäinen argumentti on aina
    # olioon itseensä viittaavan muuttujan nimi (Javan this -avainsana).
    # Pythonissa on tapana nimittää tätä muuttujaa nimellä self,
    # mutta ohjelmoija voi halutessaan käyttää myös jotain muuta nimitystä tälle.
    def __init__(self, difficulty, gamemode):
        self.running = True
        self.last = pygame.time.get_ticks()
        self.last2 = pygame.time.get_ticks()
        self.cooldown = 100
        self.difficulty = difficulty
        self.gamemode = gamemode
        self.obstacles = []
        self.pause = False
        self.game_over = False

    def game_loop(self):
        # Peli looppi
        self.apple.newApple(self.gridSize)
        # Jos vaikeustaso on "Hard", generoidaan esteitä
        if (self.difficulty.name == "Hard"):
            for i in range(random.randint(7, 15)):
                self.obstacles.append(Obstacle(self.windowWidth / self.gridSize, self.windowHeight / self.gridSize))
                self.obstacles[i].newObstacle(self.gridSize)

        while self.running:

            # Tapahtuma looppi
            for event in pygame.event.get():
                # Ensimmäinen if lause käsittelee pelistä poistumisen
                if event.type == QUIT:
                    pygame.quit()
                    quit()

                elif event.type == KEYDOWN:
                    now = pygame.time.get_ticks()
                    now2 = pygame.time.get_ticks()
                    if event.key == K_ESCAPE:
                        menu = Menu()
                        menu.main_menu()

                    if event.key == K_SPACE:
                        self.pause = not self.pause

                    # Cooldowneilla estetään nappien spämmäys
                    # Pelaaja 1
                    if event.key == K_RIGHT and now - self.last >= self.cooldown:
                        self.last = now
                        self.snake.moveRight()

                    if event.key == K_LEFT and now - self.last >= self.cooldown:
                        self.last = now
                        self.snake.moveLeft()

                    if event.key == K_UP and now - self.last >= self.cooldown:
                        self.last = now
                        self.snake.moveUp()

                    if event.key == K_DOWN and now - self.last >= self.cooldown:
                        self.last = now
                        self.snake.moveDown()
                    # Pelaaja 2
                    if event.key == K_d and now2 - self.last2 >= self.cooldown:
                        self.last2 = now2
                        self.other_snake.moveRight()

                    if event.key == K_a and now2 - self.last2 >= self.cooldown:
                        self.last2 = now2
                        self.other_snake.moveLeft()

                    if event.key == K_w and now2 - self.last2 >= self.cooldown:
                        self.last2 = now2
                        self.other_snake.moveUp()

                    if event.key == K_s and now2 - self.last2 >= self.cooldown:
                        self.last2 = now2
                        self.other_snake.moveDown()

            # Onko peli pysäytetty?
            if not self.pause and not self.game_over:
                # Varmistetaan että peli ei mene yli 10 fps:n (kärmes kulkee valonnopeudella muuten...)
                self.clock.tick(10)
                self.display_screen.fill((10, 10, 10))
                self.drawGrid()
                self.apple.drawApple()

                for i in range(len(self.obstacles)):
                    self.obstacles[i].drawObstacle()
                    if self.obstacles[i].obstacleLocation() == self.apple.appleLocation():
                        self.apple.newApple(self.gridSize)

                self.snake.update(self.gridSize)
                if self.gamemode.name == "Duel":
                    self.other_snake.update(self.gridSize)

                # Pisteiden näyttäminen ruudulla
                if self.gamemode.name == "Solo":
                    font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 20)
                    self.drawText("Pisteet: " + str(self.score1), font, (255, 255, 255), (math.floor((self.windowWidth / 2)), 20))
                else:
                    # Pelaaja 1
                    font1 = pygame.font.Font('fonts/OpenSans-Regular.ttf', 20)
                    self.drawText("Pelaaja 1: " + str(self.score1), font1, (255, 255, 255), (math.floor((self.windowWidth / 2)), 20))

                    # Pelaaaja 2
                    font2 = pygame.font.Font('fonts/OpenSans-Regular.ttf', 20)
                    self.drawText("Pelaaja 2: " + str(self.score2), font2, (255, 255, 255), (math.floor((self.windowWidth / 2)), 60))

                # Törmäysten tunnistus
                if not self.snake.isOnScreen(int(self.windowWidth / self.gridSize), int(self.windowHeight / self.gridSize))\
                        or self.snake.collideWithSelf():
                    # Tarkistetaan että peli ei ole jo loppunut
                    if not self.game_over:
                        self.game_over = not self.game_over

                if self.gamemode.name == "Duel":
                    if not self.other_snake.isOnScreen(int(self.windowWidth / self.gridSize), int(self.windowHeight / self.gridSize)) or self.other_snake.collideWithSelf():
                        # Tarkistetaan että peli ei ole jo loppunut
                        if not self.game_over:
                            self.game_over = not self.game_over

                    if self.snake.collideWithOther(self.other_snake.snakeLocation()) or self.other_snake.collideWithOther(self.snake.snakeLocation()):
                        if not self.game_over:
                            self.game_over = not self.game_over

                if self.snake.snakeLocation() == self.apple.appleLocation():
                    self.apple.newApple(self.gridSize)
                    self.snake.growSnake()
                    self.score1 += 1

                if self.other_snake.snakeLocation() == self.apple.appleLocation():
                    self.apple.newApple(self.gridSize)
                    self.other_snake.growSnake()
                    self.score2 += 1

                if self.snake.isOnApple(self.apple.appleLocation()) or self.other_snake.isOnApple(self.apple.appleLocation()):
                    self.apple.newApple(self.gridSize)

                for i in range(len(self.obstacles)):

                    if self.obstacles[i].obstacleLocation() == self.snake.snakeLocation()\
                            or self.obstacles[i].obstacleLocation() == self.other_snake.snakeLocation():
                        self.game_over = not self.game_over
            #Pause ruutu
            if self.pause:
                self.display_screen.fill((10, 10, 10))
                font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 60)
                self.drawText("Pysäytetty...", font, (255, 255, 255), (math.floor((self.windowWidth / 2)), self.windowHeight / 2))

            #Pelin lopetusruutu
            if self.game_over:
                menu = Menu()
                restart = ""
                text = "PELI PÄÄTTYI"
                font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 60)
                self.drawText(text, font, (255, 255, 255), (math.floor((self.windowWidth / 2)), self.windowHeight / 3))
                pygame.draw.rect(self.display_screen, (10, 10, 10), (math.floor(self.windowWidth / 2.6), 10, 150, 50))

                if self.gamemode.name == "Solo":
                    text = "Pisteet: " + str(self.score1)
                    font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 25)
                    self.drawText(text, font, (255, 255, 255), (math.floor((self.windowWidth / 2)), math.floor((self.windowHeight / 2))))
                else:
                    pygame.draw.rect(self.display_screen, (10, 10, 10), (math.floor(self.windowWidth / 2.6), 25, 150, 50))
                    # Pelaaja 1
                    text = "Pelaaja 1 pisteet: " + str(self.score1)
                    font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 25)
                    self.drawText(text, font, (255, 255, 255), (math.floor((self.windowWidth / 2)), math.floor((self.windowHeight / 2))))

                    # Pelaaaja 2
                    text = "Pelaaja 2 pisteet: " + str(self.score2)
                    font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 25)
                    self.drawText(text, font, (255, 255, 255), (math.floor((self.windowWidth / 2)), math.floor((self.windowHeight / 1.7))))
                    #Katsotaan kumpi pelaaja voitti
                    if self.score1 > self.score2:
                        text = "Pelaaja 1 voitti pelin!"
                        font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 40)
                        self.drawText(text, font, (255, 255, 255), (math.floor((self.windowWidth / 2)), math.floor((self.windowHeight / 2.4))))
                    elif self.score2 > self.score1:
                        text = "Pelaaja 2 voitti pelin!"
                        font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 40)
                        self.drawText(text, font, (255, 255, 255), (math.floor((self.windowWidth / 2)), math.floor((self.windowHeight / 2.4))))
                #Nappien arvojen määrittäminen eri vaikeustasoille
                if self.difficulty.name == "Easy" and self.gamemode.name == "Solo":
                    fontsize = 30
                    x = 60
                    y = 220
                    width = 280
                    height = 75
                    restart = "easy"
                elif self.difficulty.name == "Easy" and self.gamemode.name == "Duel":
                    fontsize = 25
                    x = 60
                    y = 250
                    width = 280
                    height = 50
                    restart = "easy_duel"
                elif self.difficulty.name == "Normal" and self.gamemode.name == "Solo":
                    fontsize = 40
                    x = 100
                    y = 400
                    width = 400
                    height = 75
                    restart = "normal"
                elif self.difficulty.name == "Normal" and self.gamemode.name == "Duel":
                    fontsize = 40
                    x = 100
                    y = 400
                    width = 400
                    height = 75
                    restart = "normal_duel"
                elif self.difficulty.name == "Hard" and self.gamemode.name == "Solo":
                    fontsize = 40
                    x = 200
                    y = 400
                    width = 400
                    height = 75
                    restart = "hard"
                elif self.difficulty.name == "Hard" and self.gamemode.name == "Duel":
                    fontsize = 40
                    x = 200
                    y = 400
                    width = 400
                    height = 75
                    restart = "hard_duel"
                #Napin luonti
                menu = Menu()
                menu.button("PELAA UUDELLEEN", x, y, width, height, (150, 185, 150), (150, 255, 150), restart, fontsize)
                menu.button("PÄÄVALIKKOON", x, y+90, width, height, (150, 150, 150), (200, 200, 200), "menu", fontsize)


            # Metodia update() kutsutaan, jotta näyttö päivittyy...
            pygame.display.update()

        print("Your score was: " + str(self.score))

    # Funktio jolla aloitetaan peli
    def start_game(self, width, height):
        # pygame.init() -metodia täytyy kutsua, jotta pelimoottori
        # käynnistyy.
        pygame.init()

        self.windowWidth = width
        self.windowHeight = height

        self.screenResolution = (self.windowWidth, self.windowHeight)

        # Määritellään näytön ominaisuuksia kuten resoluutio...
        self.display_screen = pygame.display.set_mode(self.screenResolution)
        self.gridSize = 20
        self.snake = Snake(self.windowWidth / self.gridSize, self.windowHeight / self.gridSize, (255, 0, 0))
        if self.gamemode.name == "Duel":
            self.other_snake = Snake(self.windowWidth / self.gridSize, (self.windowHeight / self.gridSize)+10, (0, 0, 255))
        else:
            # Jos emme pelaa duel modia, sijoitetaan p2 ulos kentältä jota se ei häiritse peliä
            self.other_snake = Snake(self.windowWidth / self.gridSize, self.windowHeight + 10, (0, 0, 255))
        self.apple = Apple(self.windowWidth / self.gridSize, self.windowHeight / self.gridSize)

        # ja title sekä ikoni...
        icon = pygame.image.load('pictures/icon.png')
        pygame.display.set_caption("Kärmespeli")
        pygame.display.set_icon(icon)

        # Käynnistetään itse peli...
        self.game_loop()

    # drawGrid() -metodi piirtää Kärmespeliin ruudukon
    def drawGrid(self):
        for i in range(math.floor(self.windowWidth / (self.gridSize))):
            for j in range(4, math.floor(self.windowHeight / (self.gridSize))):
                rect = pygame.Rect(i * self.gridSize, j * self.gridSize, self.gridSize, self.gridSize)
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

    def drawText(self, text, font, textColor, location):
        textSurface, textRectangle = self.text_object(text, font, textColor)
        textRectangle.center = location
        self.display_screen.blit(textSurface, textRectangle)

    def text_object(self, text, font, colour):
        textSurface = font.render(text, True, colour)
        return textSurface, textSurface.get_rect()
