class Block():

    def __init__(self, x, y, color):
        self.xPos = x
        self.yPos = y
        self.color = color

    def collision(self, otherBlock):
        if self.xPos == otherBlock.xPos and self.yPos == otherBlock.yPos:
            return True
        else:
            return False

    def check_wall(self):
        # Check right
        if self.xPos > 15:
            return True

        # Check left
        if self.xPos < 0:
            return True

        # Check bottom
        if self.yPos > 15:
            return True

        # Check top
        if self.yPos < 0:
            return True

        return False

    def loop(self):
        # Check right
        if self.xPos > 15:
            self.xPos = 0

        # Check left
        if self.xPos < 0:
            self.xPos = 15

        # Check bottom
        if self.yPos > 15:
            self.yPos = 0

        # Check top
        if self.yPos < 0:
            self.yPos = 15
