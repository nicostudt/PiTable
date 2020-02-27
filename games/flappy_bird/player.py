from utils.colors import *

class Player():

    HEIGHT = 2

    def __init__(self, colorCode):
        self.color = getColor(colorCode)
        self.reset()

    def reset(self):
        self.x = 2
        self.y = 7
        self.dy = 0
        self.dead = False

    def update(self, dt):
        self.dy -= 80 * dt
        self.y += self.dy * dt

        if self.y < 0:
            self.y = 0
            self.dy = 0
            self.jumpCount = 0

        elif self.y +Player.HEIGHT > 16:
            self.y = 16 -Player.HEIGHT

    def jump(self):
        self.dy = 25

    def getBody(self):
        points = []
        x = int(self.x)
        y = int(self.y)

        for j in range(Player.HEIGHT):
            points.append([x, y + j])

        return points
