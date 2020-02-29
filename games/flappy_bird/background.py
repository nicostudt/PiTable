import utils.simplexnoise.noise as snoise


class Background():

    LIGHT = 0.65


    def __init__(self, height, y, dx):
        self.height = height
        self.y = y

        self.noise = snoise.SimplexNoise(2, 1, 2)
        self.lastX = 0
        self.x = 0
        self.dx = dx
        self.drawX = 0
        self.colors = [[[0,0,0] for i in range(16)]
                        for j in range(height)]


    def update(self, dt):
        self.x += self.dx * dt
        self.move(int(self.x) - int(self.lastX))
        self.lastX = self.x


    def move(self, amount):
        if amount == 0:
            return

        for i in range(amount):
            self.drawX += 1

            for j, row in enumerate(self.colors):
                del row[0]
                row.append(self.calcColor(self.drawX, j))


    def calcColor(self, x, y):
        return [0, 0, 0]


    def draw(self, screen):
        for j, row in enumerate(self.colors):
            y = self.y + j
            for i, color in enumerate(row):
                screen.setPixel(i, y, color)
