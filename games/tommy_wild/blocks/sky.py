import utils.colors as colors
from .block import Block


class Sky(Block):

    COLOR = colors.getColor("material_blue")

    def __init__(self):
        Block.__init__(self)

    def getType(self):
        return "sky"

    def getColor(self):
        return Sky.COLOR
