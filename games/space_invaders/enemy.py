from .bullet import Bullet
from .shooter import Shooter


class Enemy(Shooter):

    def __init__(self, startPos):
        Shooter.__init__(self, startPos, [
                         [-1, 0], [-1, 1], [0, 0], [1, 0], [1, 1]],
                         [255, 0, 0])
        self.setMoveState("right")

    def move(self):

        if self.moveState == "right":
            self.addPos(1, 0)

            if self.moveCounter >= 3:
                self.setMoveState("down")

        elif self.moveState == "left":
            self.addPos(-1, 0)

            if self.moveCounter >= 3:
                self.setMoveState("right")

        elif self.moveState == "down":
            self.addPos(0, 1)

            if self.moveCounter == 1:
                self.setMoveState("left")

    def setMoveState(self, state):
        self.moveState = state
        self.moveCounter = 0

    def addPos(self, dx, dy):
        self.pos = [self.pos[0] + dx, self.pos[1] + dy]
        self.moveCounter += 1

    def createBullet(self):
        pos = [self.pos[0], self.pos[1] + 1]
        return Bullet(pos, [0, 1], self.color)

    def destroy(self, pos):
        pos = [pos[i] - self.pos[i] for i in range(2)]
        self.body.remove(pos)
