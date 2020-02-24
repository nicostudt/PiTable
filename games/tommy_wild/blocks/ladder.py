from .. import colors
from .block import Block


class Ladder(Block):

    COLOR = colors.getColor("woodbrown")

    def __init__(self):
        Block.__init__(self)

    def isClimbable(self):
        return True

    def getType(self):
        return "ladder"

    def getColor(self):
        return Ladder.COLOR
