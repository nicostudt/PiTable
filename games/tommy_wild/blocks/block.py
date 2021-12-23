import utils.colors as colors


class Block():
    emptyColor = colors.getColor("material_darkbrown")

    def __init__(self):
        self.pos = None
        self.life = self.getMaxLife()
        self.fallTimer = 0
        self.falling = False

    def setPos(self, pos):
        self.pos = pos

    def isWalkable(self):
        return self.life == 0

    def isClimbable(self):
        return False

    def addLife(self, dLife):
        self.life = max(0, self.life + dLife)

    def getLife(self):
        return self.life

    def getMaxLife(self):
        return 0

    def getDeath(self):
        return 1 - float(self.getLife()) / self.getMaxLife()

    def getColor(self):
        if self.life == self.getMaxLife():
            return self.getBaseColor()

        return colors.interpolateColor(
            Block.emptyColor, self.getBaseColor(),
            float(self.life) / self.getMaxLife())

    def getBaseColor(self):
        return [0, 0, 0]

    def getType(self):
        return "block"

    def __eq__(self, other):
        return self.pos == other.pos and self.getType() == other.getType()
