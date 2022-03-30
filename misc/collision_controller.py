from math import sqrt, fabs
from misc.constants import EPS, DEBUG


class CollisionController:
    def __init__(self, game, c1, c2):
        self.game = game
        self.c1 = c1
        self.c2 = c2
        self.hyp = c1.r+c2.r
        self.collision = False
        self.v1x = self.c1.vx
        self.v2x = self.c2.vx
        self.v1y = self.c1.vy
        self.v2y = self.c2.vy
        self.count = 0

    @property
    def dx(self):
        return self.c1.x - self.c2.x

    @property
    def dy(self):
        return self.c1.y - self.c2.y

    @property
    def d(self):
        return sqrt(self.dx ** 2 + self.dy ** 2)

    def process_logic(self):
        if self.d < self.hyp:
            distance = sqrt((self.c1.x - self.c2.x) ** 2 + (self.c1.y - self.c2.y) ** 2)
            desDistance = self.c1.r + self.c2.r

            distanceVectorX = self.c1.x - self.c2.x
            distanceVectorY = self.c1.y - self.c2.y

            # нормализуем вектор
            distanceVectorX = distanceVectorX / distance
            distanceVectorY = distanceVectorY / distance

            shiftValue = (desDistance - distance) / 2

            self.c1.x += shiftValue * distanceVectorX
            self.c1.y += shiftValue * distanceVectorY
            self.c2.x += -1 * shiftValue * distanceVectorX
            self.c2.y += -1 * shiftValue * distanceVectorY

            if DEBUG:
                sumE = self.c1.e + self.c2.e
                print('Суммарная механическая энергия: ', sumE)
                print('Суммарный импульс: ', what_is_p([self.c1, self.c2]))

            sina = self.dy / self.hyp
            cosa = self.dx / self.hyp

            v1xn = self.c1.vx * cosa + self.c1.vy * sina
            v1yn = -1*self.c1.vx * sina + self.c1.vy * cosa
            v2xn = self.c2.vx * cosa + self.c2.vy * sina
            v2yn = -1*self.c2.vx * sina + self.c2.vy * cosa

            u1xn = (2 * self.c2.m * v2xn + v1xn * (self.c1.m - self.c2.m)) / (self.c1.m + self.c2.m)
            u2xn = (2 * self.c1.m * v1xn + v2xn * (self.c2.m - self.c1.m)) / (self.c1.m + self.c2.m)

            self.c1.vx = u1xn * cosa - v1yn * sina
            self.c1.vy = v1yn * cosa + u1xn * sina
            self.c2.vx = u2xn * cosa - v2yn * sina
            self.c2.vy = v2yn * cosa + u2xn * sina
            if DEBUG:
                sumE = self.c1.e + self.c2.e
                print('Суммарная механическая энергия: ', sumE)
                print('Суммарный импульс: ', what_is_p([self.c1, self.c2]))
                print(self.c1.vx, self.c2.vx)

def what_is_p(arr):
    px = 0
    py = 0
    for circle in arr:
        px += circle.px
        py += circle.py
    p = sqrt(px**2 + py**2)
    return p