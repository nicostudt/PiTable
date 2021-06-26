from games.pacman.vector import Vector


class Player:

    def __init__(self, game):
        self.color = [205, 207, 2]
        self.game = game
        self.pos = Vector(4, 5)
        self.lastPos = self.pos.copy()
        self.speed = 1
        self.invincible = False
        self.invincibleTimer = 0
        self.invincibleColor = [255, 255, 255]

    def move(self, axis, value):
        # Save lastPos for later
        self.lastPos = self.pos.copy()

        # Move if axis pressed
        if axis == "x" and value == 1:  # To the right
            self.pos.addX(self.speed)
        if axis == "x" and value == -1:  # To the left
            self.pos.addX(-self.speed)
        if axis == "y" and value == 1:  # To the bottom
            self.pos.addY(self.speed)
        if axis == "y" and value == -1:  # To the top
            self.pos.addY(-self.speed)

        # Check edge cases
        self.pos.wrapAround(self.game.size)

        self.checkWall()
        self.collectItem()
        self.snack()

    def update(self, dt):
        self.invincibleTimer += dt

        if self.invincibleTimer >= 5:
            self.invincible = False

    def snack(self):
        # Check if collision with any enemy
        for index, enemy in enumerate(self.game.enemies):
            if enemy.pos == self.pos:
                if self.invincible:
                    del self.game.enemies[index]
                else:
                    self.game.initialize()

        # Win?
        if len(self.game.enemies) == 0:
            self.game.initialize()

    def checkWall(self):
        # Stand on wall? -> Reset position
        if self.game.world.isWall(self.pos):
            # Reset to last pos
            self.pos = self.lastPos.copy()

    def collectItem(self):
        # Check if player on item
        for index, item in enumerate(self.game.items):
            if item.pos == self.pos:
                del self.game.items[index]
                self.invincible = True
                self.invincibleTimer = 0

    def render(self, screen):
        if self.invincible:
            screen.setPixel(self.pos.x, self.pos.y, self.invincibleColor)
        else:
            screen.setPixel(self.pos.x, self.pos.y, self.color)
