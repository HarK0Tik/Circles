from math import sqrt

import pygame as pg

from misc import CollisionController
from misc import DEBUG
from objects import Circle


class Game:
    def __init__(self, size=(1200, 800), objects=None):
        self.FPS = 60
        self.size = self.width, self.height = size
        self.screen = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()
        self.game_over = False
        self.objects = []
        if objects is None:
            self.create_objects()
        else:
            for i in objects:
                self.objects.append(Circle(self, i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        self.create_collision_controllers()

    def create_objects(self):
        self.c1 = Circle(self, 60, 1, 7, -1, 200, 400, pg.Color(255, 0, 0))
        self.c2 = Circle(self, 30, 1, -9, 3, 1000, 500, pg.Color(0, 255, 0))
        self.c3 = Circle(self, 50, 10, -1, 3, 500, 700, pg.Color(0, 0, 255))
        self.objects.append(self.c1)
        self.objects.append(self.c2)
        self.objects.append(self.c3)

    def create_collision_controllers(self):
        self.collision_controllers = []
        for i in range(len(self.objects)-1):
            for j in range(len(self.objects)-i-1):
                self.collision_controllers.append(CollisionController(self, self.objects[i], self.objects[i+j+1]))

    def main_loop(self):
        while not self.game_over:
            self.process_all_events()
            self.process_all_logic()
            self.process_all_draw()
            self.clock.tick(self.FPS)
        pg.quit()

    def process_all_draw(self):
        self.screen.fill(pg.Color(128, 128, 128))
        for i in self.objects:
            i.process_draw()
        pg.display.flip()

    def process_all_logic(self):
        for i in self.collision_controllers:
            i.process_logic()
        for i in self.objects:
            i.process_logic()

    def process_all_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_over = True
