# Kärmespeli
# Soveltava projekti 2020
# Johanna Seulu, Juhana Kuparinen, Juho Ollila

VERSION = 1.3

'''
Versiosta 0.6 eteenpäin, kaikki käyttämämme luokat sijaitsevat game_modules -kansiossa omissa moduuleissaan
(lukuunottamatta Menu ja Game luokkia, jotka ovat game_engine.py moduulissa). Tästä eteenpäin myös uudet tekemämme
luokat olisi hyvä tehdä omiin moduuleihinsa (eli omaan .py tiedostoon) game_modules kansiossa.
'''

"""
main -metodilla käynnistämme pelin. Metodi luo ensin Menu -olion ja 
luo menu ruudun olion metodilla main_menu.

main -metodi tulostaa konsoliin myös pienen tervehdyksen ja pelin version.
"""

from game_modules.game_engine import Menu

def main():
    print("Tervetuloa Kärmespeliin!")
    print("Pelaatte versiolla: " + str(VERSION))
    menu = Menu()
    menu.main_menu()

if __name__ == "__main__":
    main()

