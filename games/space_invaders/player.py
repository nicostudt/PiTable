from .bullet import Bullet
from .shooter import Shooter


class Player(Shooter):
    SHOOT_TIME = 0.5

    def __init__(self, startPos):
        Shooter.__init__(self, startPos,
                         [[-1, 0], [0, 0], [1, 0], [0, -1]],
                         [255, 255, 255])
        self.velX = 0
        self.shootTimer = 0

    def update(self, dt):
        self.shootTimer -= dt
        self.move()

    def shoot(self):
        if self.shootTimer > 0:
            return False

        self.shootTimer = Player.SHOOT_TIME

        return True

    def createBullet(self):
        pos = [self.pos[0], self.pos[1] - 1]
        return Bullet(pos, [0, -1], self.color)

    def setVel(self, velX):
        self.velX = velX

    def move(self):
        self.pos[0] = max(0, min(15, self.pos[0] + self.velX))
