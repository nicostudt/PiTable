from PIL import Image
from games.pacman.vector import Vector


class World:

    def __init__(self):
        self.wallColor = [2, 4, 126]
        self.door = Vector(8, 4)
        self.doorTimer = 5

        self.loadFromImage()

        # Add door
        self.walls[self.door.y][self.door.x] = True

    def loadFromImage(self):
        # Load world from image
        image = Image.open("games/pacman/world_data.png")
        pixels = image.load()

        self.walls = []
        for y in range(16):
            self.walls.append([])

            for x in range(16):
                # Is pixel black? -> Add wall
                if pixels[x, y] == (0, 0, 0):
                    self.walls[y].append(True)
                else:
                    self.walls[y].append(False)

    def update(self, dt):
        self.doorTimer -= dt

        # Remove door if timer smaller than 0
        if self.doorTimer <= 0:
            self.walls[self.door.y][self.door.x] = False

    def getSpaces(self):
        for y in range(16):
            for x in range(16):
                yield Vector(x, y)

    def getFreeSpaces(self):
        freeSpaces = []

        for pos in self.getSpaces():
            if not self.isWall(pos):
                freeSpaces.append(pos)

        return freeSpaces

    def isWall(self, pos):
        # Is wall at [x, y]?
        return self.walls[pos.y][pos.x]

    def render(self, screen):
        screen.fill([0, 0, 0])

        for pos in self.getSpaces():
            if self.isWall(pos):
                screen.setPixel(pos.x, pos.y, self.wallColor)


