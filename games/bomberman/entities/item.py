from .entity import Entity


class Item(Entity):

    def __init__(self, type, pos, color):
        Entity.__init__(self, pos, color)

        self.type = type

    def isPlusBomb(self):
        return self.type == "plusBomb"

    def isPlusSpeed(self):
        return self.type == "plusSpeed"

    def isPlusRange(self):
        return self.type == "plusRange"

    @staticmethod
    def getPlusBomb(pos):
        return Item("plusBomb", pos, [255, 0, 255])  # magenta

    @staticmethod
    def getPlusSpeed(pos):
        return Item("plusSpeed", pos, [0, 255, 255])  # tuerkis

    @staticmethod
    def getPlusRange(pos):
        return Item("plusRange", pos, [255, 255, 0])  # yellow
