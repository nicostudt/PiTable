from engine.game import Game
from .world import World
from .vec import Vec


class Bomberman(Game):

    def __init__(self):
        Game.__init__(self, "Bomberman", [16, 16])
        self.fps = 30

    def initialize(self):
        self.world = World()
        self.state = "start"
        self.gameoverTimer = 0

    def onButtonDown(self, playerId, button):
        if self.state == "start":
            if button == "START":
                player = self.world.getPlayer(playerId)
                player.setReady(True)

                if self.world.allPlayersReady():
                    self.state = "game"

        elif self.state == "game":
            if button == "A":
                self.world.addBombOfPlayer(playerId)

        elif self.state == "gameover":
            if button == "START":
                self.initialize()

    def onAxisMotion(self, playerId, axis, value):
        if self.state != "game":
            return

        value = int(value)

        if axis == "x":
            movement = Vec(value, 0)
        elif axis == "y":
            movement = Vec(0, value)
        else:
            return

        player = self.world.getPlayer(playerId)
        if player is None:
            return

        player.setMovement(movement)

    def update(self, dt):
        if not self.state == "gameover":
            self.world.update(dt)

            if self.world.gameIsOver():
                self.state = "gameover"
        else:
            self.gameoverTimer += dt

            if self.gameoverTimer >= 3:
                self.initialize()

    def render(self, screen):
        screen.fill([0, 0, 0])

        for entity in self.world.getAllEntities():
            pos = entity.getPos()
            color = entity.getColor()
            screen.setPixel(pos.x, pos.y, color)

        if self.state == "gameover":
            winner = self.world.getWinner()
            color = winner.getColor() if winner else [255, 255, 255]

            for x in range(self.size[0]):
                for y in range(self.size[1]):
                    if x == 0 or x == self.size[0] - 1 \
                            or y == 0 or y == self.size[1] - 1:
                        screen.setPixel(x, y, color)

        screen.show()
