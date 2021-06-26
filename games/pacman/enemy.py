import random
from games.pacman.vector import Vector


class Enemy:

    def __init__(self, game, pos, color):
        self.color = color
        self.game = game
        self.pos = pos
        self.lastPos = self.pos.copy()
        self.vel = Vector(0, 0)
        self.speed = 1
        self.moveTimer = 0.2

    def move(self, dt):
        self.moveTimer -= dt
        if self.moveTimer > 0:
            return

        self.moveTimer = 0.2

        # Save lastPos for later
        self.lastPos = self.pos.copy()

        self.changeDirection()

        self.pos += self.vel
        self.pos.wrapAround(self.game.size)
        self.checkWall()

    def changeDirection(self):
        # Check free space
        freeDirections = []

        for dPos in [Vector(-1, 0), Vector(1, 0), Vector(0, -1), Vector(0, 1)]:
            nextPos = self.pos + dPos

            if self.checkFree(nextPos):
                # Remove way back
                if dPos == self.vel.negative():
                    continue

                freeDirections.append(dPos)

        # Do we even have a choice?
        if len(freeDirections) == 0:
            self.vel = self.vel.negative()
            nextPos = self.pos + self.vel

            if not self.checkFree(nextPos):
                self.vel.set(0, 0)

        else:
            # Choose random
            randomDirection = random.choice(freeDirections)
            self.vel = randomDirection

    def checkFree(self, nextPos):
        nextPos.wrapAround(self.game.size)

        if self.game.world.isWall(nextPos):
            return False

        if self.isEnemy(nextPos):
            return False

        return True

    def isEnemy(self, checkPos):
        for enemy in self.game.enemies:
            if enemy.pos == checkPos:
                return True

        return False

    def checkWall(self):
        # Stand on wall? -> Reset position
        if self.game.world.isWall(self.pos):
            # Reset to last pos
            self.pos = self.lastPos.copy()

    def render(self, screen):
        screen.setPixel(self.pos.x, self.pos.y, self.color)
