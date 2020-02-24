from .entity import Entity
from ..vec import Vec


class Mob(Entity):

    def __init__(self, world, pos, color):
        Entity.__init__(self, pos, color)

        self.world = world
        self.movement = Vec()
        self.moveMaxTime = 0.15
        self.moveTimer = 0

    def update(self, dt):
        self.moveTimer -= dt
        if self.moveTimer <= 0:
            self.move()

    def move(self):
        if self.movement.isZero():
            return

        nextPos = self.pos.add(self.movement)

        if self.world.isFree(nextPos):
            self.pos = nextPos
            self.moveTimer = self.moveMaxTime

    def setMovement(self, movement):
        self.movement = movement
