class GameEntry():

    def __init__(self, name, image):
        self.name = name
        self.image = image

        self.brightness = 0
        self.pixelLength = len(name) * 4
        self.runIndex = 0
        self.showing = False
        self.dy = -9

        self.dx = 0

        self.counter = 0

    def update(self):
        self.counter += 1

        self.brightness = abs(self.dy + 3) / 6.0
        if self.dy < -3:
            self.brightness = 0

        if self.showing:
            if self.dy < 3:
                self.dy += 1
            elif self.counter % 2 == 0 and self.pixelLength > 16:
                self.dx -= 1

        else:
            if self.dy > -9:
                self.dy -= 1
            else:
                self.dx = 0

        if self.dx < -self.pixelLength:
            self.dx = 16

    def show(self, flag):
        self.showing = flag

    def getImage(self):
        if self.brightness == 0:
            return None

        return [[[self.brightness * self.image[y][x][i] for i in range(3)]
                 for x in range(4)] for y in range(4)]
