from .pos import Pos


class Camera():

    def __init__(self, size):
        self.width = size[0]
        self.height = size[1]
        self.width2 = self.width // 2
        self.height2 = self.height // 2
        self.offset = Pos()
        self.hookRange = 2

    def setOffset(self, pos):
        self.offset = pos.clone()

    def updateOffset(self, pos):
        diff = Pos.sub(pos, self.offset)

        if diff.x > self.hookRange:
            self.offset.add(1, 0)
        elif diff.x < -self.hookRange - 1:
            self.offset.add(-1, 0)

        if diff.y > self.hookRange:
            self.offset.add(0, 1)
        elif diff.y < -self.hookRange - 1:
            self.offset.add(0, -1)

    def translate(self, x, y):
        return Pos(x + self.offset.x - self.width // 2,
                   y + self.offset.y - self.height // 2)

    def translateToPx(self, pos):
        return [pos.x - self.offset.x + self.width // 2,
                pos.y - self.offset.y + self.height // 2]

    def getRenderPositions(self):
        sx = self.offset.x - self.width // 2
        ex = self.offset.x + self.width // 2
        sy = self.offset.y - self.height // 2
        ey = self.offset.y + self.height // 2

        return [Pos(x, y) for x in range(sx, ex) for y in range(sy, ey)]
