from .. import colors
from .block import Block


class Dirt(Block, object):

    COLOR = colors.getColor("material_brown")

    def __init__(self):
        Block.__init__(self)

    def getMaxLife(self):
        return 4

    def getType(self):
        return "dirt"

    def getBaseColor(self):
        return Dirt.COLOR
