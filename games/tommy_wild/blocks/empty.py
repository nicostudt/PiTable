from .. import colors
from .block import Block


class Empty(Block):

    COLOR = colors.getColor("material_darkbrown")

    def __init__(self):
        Block.__init__(self)

    def getType(self):
        return "empty"

    def getColor(self):
        return Empty.COLOR
