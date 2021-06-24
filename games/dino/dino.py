from engine.game import Game
import random
from games.dino.world import World


class Dino(Game):

    def __init__(self):
        Game.__init__(self, "Dino", [16, 16])
        self.fps = 30

    def initialize(self):
        self.world = World(1, "material_red")
        self.world2 = World(9, "material_blue")

    def update(self, dt):
        self.world.update(dt)
        self.world2.update(dt)

    def onButtonDown(self, player, button):
        if player == 0:
            world = self.world
        elif player == 1:
            world = self.world2

        if button == "START":
            self.world.start()
            self.world2.start()

        if button == "A":
            world.player.jump()

        elif button == "B":
            world.player.crouch(True)

    def onButtonUp(self, player, button):
        if player == 0:
            world = self.world
        elif player == 1:
            world = self.world2

        if button == "B":
            world.player.crouch(False)

    def render(self, screen):
        screen.fill([0, 0, 0])
        self.world.draw(screen)
        self.world2.draw(screen)
        screen.show()
