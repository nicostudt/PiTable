from .entity import Entity
from .color import *
import math


class Bomb(Entity):

    def __init__(self, playerId, color, radius, pos):
        c = interpolate(color, [255, 255, 255], 0.5)
        Entity.__init__(self, pos, c)

        self.playerId = playerId
        self.radius = radius
        self.countdown = 3

    def update(self, dt):
        self.countdown -= dt

    def timeover(self):
        return self.countdown <= 0

    def getColor(self):
        x = (3 - self.countdown)
        alpha = (math.cos(x**2 * 6.28 * 1.0) + 1) / 2
        return interpolate(self.color, [255, 255, 255], alpha)
