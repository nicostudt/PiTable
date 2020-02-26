
class Obstacle():

    HOLE_WIDTH = 5

    def __init__(self, x, hole):
        self.x = x
        self.hole = hole

        self.body = []
        for i in range(16):
            if i < self.hole or i >= self.hole + Obstacle.HOLE_WIDTH:
                self.body.append(i)


    def addPos(self, dx):
        self.x += dx

    def getBody(self):
        x = int(self.x)
        return [[x, y] for y in self.body]
