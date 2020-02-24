from engine.game import Game
from .drop import Drop
import random


class Matrix(Game):

    def __init__(self):
        Game.__init__(self, "Matrix", [16, 16])
        self.fps = 10

    def initialize(self):
        self.drops = []

        for i in range(int(self.size[0] * 1.5)):
            drop = Drop(self.size[0], self.size[1])
            drop.pos[1] = random.randint(0, self.size[1])
            self.drops.append(drop)

    def update(self, dt):
        for i in range(len(self.drops) - 1, -1, -1):
            drop = self.drops[i]
            drop.fall()

            if drop.checkDeath(self.size[1]):
                self.drops.remove(drop)
                self.drops.append(Drop(self.size[0], self.size[1]))

    def render(self, screen):
        screen.fill([0, 0, 0])

        for drop in self.drops:
            drop.draw(screen)

        screen.show()
