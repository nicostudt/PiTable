from games.flappy_bird.background import Background
from utils.colors import *


class Sky(Background):

    def __init__(self, dx):
        Background.__init__(self, 13, 0, dx)

        self.blue = getColor("material_darkblue")
        self.purple = getColor("material_darkpurple")
        self.orange = getColor("material_darkorange")

    def calcColor(self, x, y):
        r = self.noise.noise(x * 0.1, y * 0.15, mul=2)
        a = (self.height-y) / float(self.height)

        color = interpolateBetween([[self.orange, 0.0],
                                    [self.purple, 0.4],
                                    [self.blue, 0.8]], a)

        if r > 0.6:
            c = (r-0.4)/0.6 *1 * a
            color = interpolateColor(color, [255, 255, 255], c)

        return [int(k * Background.LIGHT) for k in color]
