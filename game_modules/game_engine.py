import pygame, sys
import math
import random
from enum import Enum
from pygame.locals import *
from game_modules.Snake import Snake
from game_modules.Apple import Apple
from game_modules.Obstacle import Obstacle


#################################
# MENU LUOKKA
#################################

"""
Menu -luokka, jossa luodaan kaikki eri valikot ja valikkoihin liittyvät ominaisuudet peliin.

Attributes
==========

menuWidth : int
menuHeight : int
menuResolution : tuple

clock : Clock

volume : Surface
volume_mute : Surface
arrow_keys : Surface
wasd_keys : Surface
esc_key : Surface

black : tuple
white : tuple
green : tuple
light_green : tuple
red : tuple
light_red : tuple
gray : tuple
light_gray : tuple
yellow : tuple
light_yellow : tuple


Methods
=======

drawText : void
text_object : surface, rect
button : void
main_menu : void
credits : void
sp_select : void
duel_select : void
"""

class Menu:
    # Kun peli käynnistetään, tällä enum -luokalla tiedetään
    # mikä vaikeustaso on.
    class Difficulties(Enum):
        Easy = 0
        Normal = 1
        Hard = 2

    # Kun peli käynnistetään, tällä enum -luokalla tiedetään
    # mikä pelimuoto on.
    class Gamemodes(Enum):
        Solo = 1
        Duel = 2

    menuWidth = 800
    menuHeight = 600
    menuResolution = (menuWidth, menuHeight)
    clock = pygame.time.Clock()
    menu_screen = pygame.display.set_mode(menuResolution)

    #Määritetään kuvia
    volume = pygame.image.load('pictures/Volume_icon.png')
    volume_mute = pygame.image.load('pictures/Volume_mute.png')
    arrow_keys = pygame.image.load('pictures/Arrow_keys.png')
    wasd_keys = pygame.image.load('pictures/WASD.png')
    esc_key = pygame.image.load('pictures/Esc_key.png')

    #Määritellään valmiiksi värejä RGB arvojen avulla
    black = (10, 10, 10)
    white = (255, 255, 255)
    green = (150, 185, 150)
    light_green = (150, 255, 150)
    red = (185, 150, 150)
    light_red = (255, 150, 150)
    gray = (150, 150, 150)
    light_gray = (200, 200, 200)
    yellow = (255, 255, 204)
    light_yellow = (255, 255, 102)

    def __init__(self):
        self.running = True

    def drawText(self, text, font, textColor, location):
        textSurface, textRectangle = self.text_object(text, font, textColor)
        textRectangle.center = location
        self.menu_screen.blit(textSurface, textRectangle)

    # Metodi palauttaa textikenttien luomiseen tarvittavat Surface ja Rect objektit
    def text_object(self, text, font, colour):
        textSurface = font.render(text, True, colour)
        return textSurface, textSurface.get_rect()

    """
    Button -metodi. Luo kaikki interaktiiviset napit kaikkiin pelin eri valikkoihin.
    Napin luonnissa annetaan useita eri parametreja joilla määritellään napin
    eri ominaisuudet ja toiminnot
    
    Attributes
    ==========
    
    game : Game
    mouse : tuple
    click : int
    
    Params
    ======
    message : string
    x : int
    y : int
    width : int
    height : int
    ac : tuple
    ic : tuple
    action : None/string
    fontsize : None/int
    """

    # ic = inactive colour eli väri joka on käytössä kun hiiri ei ole napin päällä
    # ac = active colour eli väri joka tulee käyttöön kun hiirellä mennään napin päälle
    def button(self, message, x, y, width, height, ic, ac, action=None, fontsize=None):

        game = Game()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Näppäimen luominen
        #Kun hiiri on näppäimen päällä
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.menu_screen, ac, (x, y, width, height))
            #Tapahtuma kun hiirellä klikkaa
            if click[0] == 1 and action != None:
                
                pygame.mixer.Sound.play(game.click_sound)

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
                elif action == "continue":
                    game.pause = False
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

    """
    Main_menu -metodi, jonka avulla luodaan päävalikko pelille, jossa on neljä eri näppäintä.
    Ensimmäinen avaa yksinpelin tason valinnan, toinen avaa kaksinpelin tason valinnan,
    kolmas avaa tekijät valikon ja neljäs poistuu pelistä.
    """
    def main_menu(self):

        pygame.mixer.music.stop()

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

    """
    credits -metodi. Luo nimensä mukaan ruudun jossa näkyy pelin tekijöiden nimet
    """
    def credits(self):
        cooldown = 5000
        last = pygame.time.get_ticks()
        credits = True
        while credits:
            now = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == QUIT or now - last >= cooldown:
                    last = now
                    credits = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        menu = Menu()
                        menu.main_menu()

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

        self.main_menu()

    """
    sp_select -metodi. Luo tason valinta valikon yksinpelille. Tason valinnassa voi valita kolmesta eri 
    vaikeustasosta jotka vaihtavat pelikentän kokoa ja vaikeimmalla tasolla lisätään esteitä.
    """
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
            # Näppäin ohjeet
            # Pelaaja
            self.menu_screen.blit(self.arrow_keys, (200, 75))
            font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 25)
            self.drawText("Pelaaja 1", font, self.white, (255, 150))
            # Äänet
            self.menu_screen.blit(self.volume, (575, 90))
            self.menu_screen.blit(self.volume_mute, (525, 92))
            font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 25)
            self.drawText("M", font, self.white, (575, 150))
            # Pause
            self.menu_screen.blit(self.esc_key, (400, 90))
            font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 25)
            self.drawText("Pysäytys", font, self.white, (418, 150))

            pygame.display.update()
            self.clock.tick(15)

    """
    duel_select -metodi. Luo tason valinta valikon kaksinpelille. Vaikeustasot ovat samat kuin
    yksinpelissä, mutta kaksinpelissä lisätään toinen käärme jota toinen pelaaja ohjaa.
    """
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
            # Näppäin ohjeet
            # Pelaaja 1
            self.menu_screen.blit(self.arrow_keys, (100+75, 75))
            font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 25)
            self.drawText("Pelaaja 1:", font, self.white, (155+75, 150))
            # Pelaaja 2
            self.menu_screen.blit(self.wasd_keys, (225+85, 75))
            font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 25)
            self.drawText("Pelaaja 2:", font, self.white, (280+85, 150))
            # Äänet
            self.menu_screen.blit(self.volume, (550+60, 90))
            self.menu_screen.blit(self.volume_mute, (500+60, 92))
            font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 25)
            self.drawText("M", font, self.white, (550+60, 150))
            # Pause
            self.menu_screen.blit(self.esc_key, (400+75, 90))
            font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 25)
            self.drawText("Pysäytys", font, self.white, (418+75, 150))

            pygame.display.update()
            self.clock.tick(15)


#################################
# GAME LUOKKA
#################################

"""
    Game -luokka, jonka avulla luomme itse peliympäristön.

    Attributes
    =========

    windowWidth : int
    windowHeight : int
    screenResolution : tuple
    clock : Clock
    snake : Snake
    other_snake : Snake
    score1 : int
    score2 : int

    volume : Surface
    volume_mute : Surface
    arrow_keys : Surface
    wasd_keys : Surface
    
    mouse : tuple
    click : boolean
    
    bite_sound : Sound
    fail_sound : Sound
    click_sound : Sound
    
    running : boolean
    last : int
    last2 : int
    cooldown : int
    difficulty : Difficulty(enum)
    gamemode : Gamemode(enum)
    obstacles : Array
    pause : boolean
    game_over : boolean
    sound : boolean

    Params
    ======

    difficulty : Difficulty(enum)
    gamemode : Gamemode(enum)

    Methods
    =======

    gameLoop : void
    startGame : void
    drawGrid : void
    drawText : void
    text_object : Surface, Rect

"""

class Game:
    windowWidth = 800
    windowHeight = 600
    screenResolution = (windowWidth, windowHeight)
    clock = pygame.time.Clock()
    snake = 0
    score1 = 0
    score2 = 0

    volume = pygame.image.load('pictures/Volume_icon.png')
    volume_mute = pygame.image.load('pictures/Volume_mute.png')
    arrow_keys = pygame.image.load('pictures/Arrow_keys.png')
    wasd_keys = pygame.image.load('pictures/WASD.png')

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #Äänet, ääniefektit ladattu osoitteesta https://www.zapslat.com
    pygame.mixer.init()
    bite_sound = pygame.mixer.Sound('sounds/bite_sound.wav')
    fail_sound = pygame.mixer.Sound('sounds/fail_sound.wav')
    click_sound = pygame.mixer.Sound('sounds/click_sound.wav')
    pygame.mixer.music.load('sounds/Komiku_-_03_-_Mushrooms.mp3')
    click_sound.set_volume(0.5)

    '''
         Pythonissa luokan konstruktori on __init__.
         Luokan sisällä olevien funktioiden ensimmäinen argumentti on aina
         olioon itseensä viittaavan muuttujan nimi (Javan this -avainsana).
         Pythonissa on tapana nimittää tätä muuttujaa nimellä self,
         mutta ohjelmoija voi halutessaan käyttää myös jotain muuta nimitystä tälle.
    '''

    def __init__(self, difficulty=None, gamemode=None):
        self.running = True
        self.last = pygame.time.get_ticks()
        self.last2 = pygame.time.get_ticks()
        self.cooldown = 100
        self.difficulty = difficulty
        self.gamemode = gamemode
        self.obstacles = []
        self.pause = False
        self.game_over = False
        self.sound = True

    """
    game_loop -metodi. Nimensä mukaisesti tämä metodi luo pelin pääasiallisen loopin.
    Loopin sisällä huolehditaan myös suurimmaksi osaksi peliin liittyvästä logiikasta.
    Itse peli loopin siällä (while -loop) on myös ns. event loop (for loop), joka huolehtii
    loopin aikaisista tapahtumista kuten nappien painalluksista.
    """
    def game_loop(self):
        # Peli looppi
        self.apple.newApple(self.gridSize)
        # Musiikki
        pygame.mixer.music.play(-1)
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
                    #Pelin pysäyttävät näppäimet
                    if event.key == K_ESCAPE:
                        self.pause = not self.pause
                    if event.key == K_SPACE:
                        self.pause = not self.pause
                    if event.key == K_p:
                        self.pause = not self.pause

                    if event.key == K_m:
                        self.sound = not self.sound

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
                # Varmistetaan että peli ei mene yli 8 fps:n (kärmes kulkee valonnopeudella muuten...)
                self.clock.tick(8)
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

                    #self.display_screen.blit(self.arrow_keys, (10,10))
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
                        pygame.mixer.Sound.play(self.fail_sound)
                        pygame.mixer.music.stop()

                if self.gamemode.name == "Duel":
                    if not self.other_snake.isOnScreen(int(self.windowWidth / self.gridSize), int(self.windowHeight / self.gridSize)) or self.other_snake.collideWithSelf():
                        # Tarkistetaan että peli ei ole jo loppunut
                        if not self.game_over:
                            self.game_over = not self.game_over
                            pygame.mixer.Sound.play(self.fail_sound)
                            pygame.mixer.music.stop()

                    if self.snake.collideWithOther(self.other_snake.snakeLocation()) or self.other_snake.collideWithOther(self.snake.snakeLocation()):
                        if not self.game_over:
                            self.game_over = not self.game_over
                            pygame.mixer.Sound.play(self.fail_sound)
                            pygame.mixer.music.stop()

                if self.snake.snakeLocation() == self.apple.appleLocation():
                    self.apple.newApple(self.gridSize)
                    self.snake.growSnake()
                    self.score1 += 1
                    pygame.mixer.Sound.play(self.bite_sound)

                if self.other_snake.snakeLocation() == self.apple.appleLocation():
                    self.apple.newApple(self.gridSize)
                    self.other_snake.growSnake()
                    self.score2 += 1
                    pygame.mixer.Sound.play(self.bite_sound)

                if self.snake.isOnApple(self.apple.appleLocation()) or self.other_snake.isOnApple(self.apple.appleLocation()):
                    self.apple.newApple(self.gridSize)

                for i in range(len(self.obstacles)):

                    if self.obstacles[i].obstacleLocation() == self.snake.snakeLocation()\
                            or self.obstacles[i].obstacleLocation() == self.other_snake.snakeLocation():
                        self.game_over = not self.game_over
                        pygame.mixer.Sound.play(self.fail_sound)
                        pygame.mixer.music.stop()

            #Pause ruutu
            if self.pause and not self.game_over:
                x = None
                y = None
                width = None
                height = None
                fontsize = None
                menu = Menu()
                self.display_screen.fill((10, 10, 10))
                font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 60)
                self.drawText("Pysäytetty...", font, (255, 255, 255), (math.floor((self.windowWidth / 2)), self.windowHeight / 3))
                if self.difficulty.name == "Easy":
                    fontsize = 30
                    x = 60
                    y = 220
                    width = 280
                    height = 75
                elif self.difficulty.name == "Normal":
                    fontsize = 40
                    x = 100
                    y = 300
                    width = 400
                    height = 75
                elif self.difficulty.name == "Hard":
                    fontsize = 40
                    x = 200
                    y = 300
                    width = 400
                    height = 75
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                # Näppäimen luominen
                # Kun hiiri on näppäimen päällä

                if x + width > mouse[0] > x and y + height > mouse[1] > y:
                    pygame.draw.rect(self.display_screen, (150, 255, 150), (x, y, width, height))
                    # Tapahtuma kun hiirellä klikkaa
                    if click[0] == 1:
                        pygame.mixer.Sound.play(self.click_sound)
                        self.pause = not self.pause
                else:
                    pygame.draw.rect(self.display_screen, (150, 185, 150), (x, y, width, height))

                font = pygame.font.Font('fonts/OpenSans-Regular.ttf', fontsize)
                self.drawText("JATKA PELIÄ", font, (10, 10, 10), ((x + width / 2), y + 35))
                menu.button("PÄÄVALIKKOON", x, y+90, width, height, (150, 150, 150), (200, 200, 200), "menu", fontsize)

            #Pelin lopetusruutu
            if self.game_over:
                menu = Menu()
                restart = ""
                text = "PELI PÄÄTTYI"
                font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 60)
                self.drawText(text, font, (255, 255, 255), (math.floor((self.windowWidth / 2)), self.windowHeight / 3))
                pygame.draw.rect(self.display_screen, (10, 10, 10), (0, 0, math.floor(self.windowWidth), 75))

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
                menu.button("PELAA UUDELLEEN", x, y, width, height, (150, 185, 150), (150, 255, 150), restart, fontsize)
                menu.button("PÄÄVALIKKOON", x, y+90, width, height, (150, 150, 150), (200, 200, 200), "menu", fontsize)

            #Äänet pois päältä
            if not self.sound:
                self.bite_sound.set_volume(0.0)
                self.fail_sound.set_volume(0.0)
                self.click_sound.set_volume(0.0)
                pygame.mixer.music.set_volume(0.0)
                self.display_screen.blit(self.volume_mute, (math.floor((self.windowWidth / 1.15)), 13))
            #Äänet päälle
            if self.sound:
                self.bite_sound.set_volume(0.8)
                self.fail_sound.set_volume(0.5)
                self.click_sound.set_volume(0.5)
                pygame.mixer.music.set_volume(0.5)
                self.display_screen.blit(self.volume, (math.floor((self.windowWidth / 1.15)), 10))

            # Metodia update() kutsutaan, jotta näyttö päivittyy...
            pygame.display.update()

    """
    start_game -metodi toimii pelin aloittavana metodina. Se huolehtii itse peli -looppia ennen
    tehtävien toimintojen suorittamisesta. Metodi lataa esimerkiksi ikonin peli-ikkunalle ja määrittelee
    tälle myös dimensiot. 
    """
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
        self.snake = Snake(self.windowWidth / self.gridSize, self.windowHeight / self.gridSize, "1")
        if self.gamemode.name == "Duel":
            self.other_snake = Snake(self.windowWidth / self.gridSize, (self.windowHeight / self.gridSize)+10, "2")
        else:
            # Jos emme pelaa duel modia, sijoitetaan p2 ulos kentältä jota se ei häiritse peliä
            self.other_snake = Snake(self.windowWidth / self.gridSize, self.windowHeight + 10, "2")
        self.apple = Apple(self.windowWidth / self.gridSize, self.windowHeight / self.gridSize)

        # ja title sekä ikoni...
        icon = pygame.image.load('pictures/icon.png')
        pygame.display.set_caption("Kärmespeli")
        pygame.display.set_icon(icon)

        # Käynnistetään itse peli...
        self.game_loop()

    """ 
    drawGrid -metodi piirtää Kärmespeliin ruudukon. Ruudukkona toimii joukko Rect -objekteja.
    """
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

    # Metodi palauttaa textikenttien luomiseen tarvittavat Surface ja Rect objektit.
    def text_object(self, text, font, colour):
        textSurface = font.render(text, True, colour)
        return textSurface, textSurface.get_rect()