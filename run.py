import sys
import pygame as pg
from game import Game
from input_variables import input_variables
import os


def main():
    program_exit = False
    while not program_exit:
        os.system('cls')

        print('Вы хотите начать симуляцию? y/n')
        ans = input()
        if ans == 'y':
            pg.display.set_caption('Кружочки')
            ico = pg.transform.scale(pg.image.load('icon.ico'), (256, 256))
            pg.display.set_icon(ico)
            objects, size = input_variables()
            pg.display.init()
            pg.font.init()
            pg.mixer.init()
            game = Game(size, objects)
            game.main_loop()
        else:
            program_exit = True
    sys.exit()


if __name__ == '__main__':
    main()
