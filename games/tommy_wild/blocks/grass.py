import utils.colors as colors
from .block import Block


class Grass(Block):

    COLOR = colors.getColor("material_green")

    def __init__(self):
        Block.__init__(self)

    def getMaxLife(self):
        return 3

    def getType(self):
        return "grass"

    def getBaseColor(self):
        return Grass.COLOR
