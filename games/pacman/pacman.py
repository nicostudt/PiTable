from engine.game import Game
from games.pacman.player import Player
from games.pacman.world import World
from games.pacman.enemy import Enemy
from games.pacman.item import Item
from games.pacman.vector import Vector
import random

class Pacman(Game):

    def __init__(self):
        Game.__init__(self, "pacman", [16, 16])
        self.fps = 30

    def initialize(self):
        self.world = World()
        self.player = Player(self)
        self.enemies = [
            Enemy(self, Vector(8, 5), [237, 173, 73]),
            Enemy(self, Vector(8, 6), [0, 255, 255]),
            Enemy(self, Vector(9, 5), [188, 0, 0]),
            Enemy(self, Vector(9, 6), [254, 184, 255])
        ]

        freeSpaces = random.sample(self.world.getFreeSpaces(), 3)

        self.items = []
        for pos in freeSpaces:
            self.items.append(Item(pos))

    def onAxisMotion(self, playerId, axis, value):
        self.player.move(axis, value)

    def update(self, dt):
        self.world.update(dt)
        self.player.update(dt)

        for enemy in self.enemies:
            enemy.move(dt)
        self.player.snack()

    def render(self, screen):
        self.world.render(screen)

        for item in self.items:
            item.render(screen)

        self.player.render(screen)

        for enemy in self.enemies:
            enemy.render(screen)

        screen.show()
