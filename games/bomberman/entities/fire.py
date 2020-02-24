from .entity import Entity
import random
from .color import *
from ..simplexnoise.noise import SimplexNoise, normalize


class Fire(Entity):

    def __init__(self, pos):
        Entity.__init__(self, pos, [255, 160, 0])

        self.countdown = 0.5
        self.alpha = random.random()

    def update(self, dt):
        self.countdown -= dt

    def timeover(self):
        return self.countdown <= 0

    def getColor(self):
        self.alpha += ((random.random() * 2) - 1) * 0.15

        if self.alpha < 0:
            self.alpha = -self.alpha
        elif self.alpha > 1:
            self.alpha = 2 - self.alpha

        # alpha = random.random()
        return interpolate([253, 216, 53], [239, 108, 0], self.alpha)
