from engine.game import Game
from games.pacman.player import Player
from games.pacman.world import World
import random


class Pacman(Game):

    def __init__(self):
        Game.__init__(self, "pacman", [16, 16])
        self.fps = 30

    def initialize(self):
        self.world = World()
        self.player = Player(self)

    def onAxisMotion(self, playerId, axis, value):
        self.player.move(axis, value)

    def update(self, dt):
        pass

    def render(self, screen):
        self.world.render(screen)
        self.player.render(screen)
        screen.show()
