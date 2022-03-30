from math import sqrt
import pygame as pg


class Circle:
    def __init__(self, game, r: float, m: float, vx: float, vy: float, x: float, y: float, color: pg.Color):
        self.r = r
        self.m = m
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
        self.game = game
        self.color = color
        self.flag = False

    @property
    def top(self):
        return self.y - self.r

    @property
    def bottom(self):
        return self.y + self.r

    @property
    def right(self):
        return self.x + self.r

    @property
    def left(self):
        return self.x - self.r

    @property
    def v(self):
        return sqrt(self.vx**2 + self.vy**2)

    @property
    def e(self):
        return self.m*self.v**2/2

    @property
    def px(self):
        return self.m*self.vx

    @property
    def py(self):
        return self.m * self.vy

    def print_variables(self):
        print('Радиус: ', self.r)
        print('Масса: ', self.m)
        print('Скорость: ', self.v)
        print('Координаты центра: (', self.x, ', ', self.y, ')', sep='')

    def process_draw(self):
        pg.draw.circle(self.game.screen, self.color, (self.x, self.y), self.r)

    def process_logic(self):
        self.process_collision()
        if not self.flag:
            self.x += self.vx
            self.y += self.vy
        self.flag = False

    def process_collision(self):
        if self.left <= 0:
            self.vx *= -1
            self.x = self.x + self.vx
        if self.top <= 0:
            self.vy *= -1
            self.y = self.y + self.vy
        if self.right >= self.game.width:
            self.vx *= -1
            self.x = self.x + self.vx
        if self.bottom >= self.game.height:
            self.vy *= -1
            self.y = self.y + self.vy