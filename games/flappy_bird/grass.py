from background import Background
from utils.colors import *


class Grass(Background):

    def __init__(self, dx):
        Background.__init__(self, 3, 13, dx)

        self.darkGreen = getColor("material_darkgreen")
        self.lightGreen = getColor("material_darklime")

    def calcColor(self, x, y):
        r = self.noise.noise(x * 0.3, y * 0.3, mul=2)
        a = (y+2) / float(self.height +1)
        color = interpolateColor(self.darkGreen, self.lightGreen, r)

        return [int(k * a * Background.LIGHT) for k in color]
