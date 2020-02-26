class GameEntry():

    def __init__(self, fontMatrix, image):
        self.fontMatrix = fontMatrix
        self.image = image
        self.pixelWidth = len(fontMatrix[0])
        self.pixelHeight = len(fontMatrix)
        self.brightness = 0
        self.runIndex = 0
        self.showing = False
        self.startPos = -self.pixelHeight * 2 -1
        self.endPos = 1
        self.diff = self.endPos - float(self.startPos)
        self.dy = -self.pixelHeight
        self.counter = 0

        self.resetX()

    def update(self):
        pass

        self.counter += 1

        self.brightness = (self.dy - self.startPos) / float(self.diff) # abs(self.dy + 3) / 6.0
        if self.dy < -3:
            self.brightness = 0

        if self.showing:
            if self.dy < self.endPos:
                self.dy += 1
            elif self.counter % 2 == 0 and self.pixelWidth > 16:
                self.dx -= 1

        else:
            if self.dy > self.startPos:
                self.dy -= 1
            else:
                self.resetX()

        if self.dx < -self.pixelWidth:
            self.dx = 16

    def resetX(self):
        if self.pixelWidth > 16:
            self.dx = 3
        else:
            self.dx = 8 -self.pixelWidth/2

    def show(self, flag):
        self.showing = flag

    def getMatrix(self):
        return self.fontMatrix

    def getImage(self):
        if self.brightness == 0:
            return None

        return [[[self.brightness * self.image[y][x][i] for i in range(3)]
                 for x in range(4)] for y in range(4)]
