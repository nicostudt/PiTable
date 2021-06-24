class Player:

    def __init__(self, game):
        self.color = [205, 207, 2]
        self.game = game
        self.posX = 5
        self.posY = 5
        self.lastPosX = self.posX
        self.lastPosY = self.posY
        self.speed = 1

    def move(self, axis, value):
        # Save lastPos for later
        self.lastPosX = self.posX
        self.lastPosY = self.posY

        # Move if axis pressed
        if axis == "x" and value == 1:  # To the right
            self.posX += self.speed
        if axis == "x" and value == -1:  # To the left
            self.posX -= self.speed
        if axis == "y" and value == 1:  # To the bottom
            self.posY += self.speed
        if axis == "y" and value == -1:  # To the top
            self.posY -= self.speed

        # Check edge cases
        self.wrapAround(self.game.size)
        self.checkWall()

    def wrapAround(self, size):
        # Left/right
        if self.posX < 0:
            self.posX += size[0]
        elif self.posX >= size[0]:
            self.posX -= size[0]

        # top/bottom
        if self.posY < 0:
            self.posY += size[1]
        elif self.posY >= size[1]:
            self.posY -= size[1]

    def checkWall(self):
        # Stand on wall? -> Reset position
        if self.game.world.isWall(self.posX, self.posY):
            # Reset to last pos
            self.posX = self.lastPosX
            self.posY = self.lastPosY

    def render(self, screen):
        screen.setPixel(self.posX, self.posY, self.color)
