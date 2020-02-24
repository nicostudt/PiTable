from .mob import Mob
from .color import *
import math


class Player(Mob):

    def __init__(self, world, id, pos, color):
        Mob.__init__(self, world, pos, color)

        self.id = id
        self.bombs = 1
        self.bombRange = 1
        self.ready = False
        self.gray = [100, 100, 100]
        self.waitTimer = 0

    def update(self, dt):
        Mob.update(self, dt)
        self.waitTimer += dt

    def isReady(self):
        return self.ready

    def setReady(self, flag):
        self.ready = flag

    def addBomb(self):
        self.bombs += 1

    def addItem(self, item):
        if item.isPlusBomb():
            self.bombs += 1

        elif item.isPlusRange():
            self.bombRange += 1

        elif item.isPlusSpeed():
            self.moveMaxTime *= 0.95

    def subBomb(self):
        self.bombs -= 1

    def hasBomb(self):
        return self.bombs > 0

    def getBombRange(self):
        return self.bombRange

    def getColor(self):
        if self.ready:
            return self.color

        alpha = (math.cos(self.waitTimer * 6.28) + 1) / 2
        return interpolate(self.gray, [0, 0, 0], alpha)
