from .. import colors
from .block import Block


class Stone(Block):

    COLOR = colors.getColor("material_gray")

    def __init__(self):
        Block.__init__(self)

    def getMaxLife(self):
        return 20

    def getType(self):
        return "stone"

    def getBaseColor(self):
        return Stone.COLOR
