from .. import colors
from .block import Block


class BedRock(Block):

    COLOR = colors.getColor("material_darkgray")

    def __init__(self):
        Block.__init__(self)

    def getType(self):
        return "bedrock"

    def getColor(self):
        return BedRock.COLOR
