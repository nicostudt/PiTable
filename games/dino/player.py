from utils.colors import *

class Player():

    def __init__(self, colorCode):
        self.color = getColor(colorCode)
        self.reset()

    def reset(self):
        self.x = 0
        self.y = 0
        self.dy = 0
        self.dx = 10
        self.jumpCount = 0
        self.isCrouching = False
        self.dead = False

    def update(self, dt):
        self.dy -= 80 * dt
        self.y += self.dy * dt
        self.x += self.dx * dt

        if self.y < 0:
            self.y = 0
            self.dy = 0
            self.jumpCount = 0

    def crouch(self, flag = True):
        self.isCrouching = flag

    def jump(self):
        if self.jumpCount >= 2:
            return

        self.dy = 25
        self.jumpCount += 1

    def getBody(self):
        points = []
        x = int(self.x)
        y = int(self.y)
        r = 2 if self.isCrouching else 3

        for j in range(r):
            points.append([x, y + j])

        return points
