class Block():

    def __init__(self, x, y, color):
        self.xPos = x
        self.yPos = y
        self.color = color

    def copy(self):
        newBlock = Block(self.xPos, self.yPos, self.color)
        return newBlock

    def collide_with(self, otherBlock):
        if self.xPos == otherBlock.xPos and self.yPos == otherBlock.yPos:
            return True
        else:
            return False

    def render_to(self, display):
        display.setPixel(self.xPos, self.yPos, self.color)
