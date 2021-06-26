class Item:

    def __init__(self, pos):
        self.pos = pos
        self.color = [0, 255, 0]

    def render(self, screen):
        screen.setPixel(self.pos.x, self.pos.y, self.color)
