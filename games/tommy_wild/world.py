from .pos import Pos
import random

from .blocks.sky import Sky
from .blocks.grass import Grass
from .blocks.stone import Stone
from .blocks.dirt import Dirt
from .blocks.ladder import Ladder
from .blocks.empty import Empty

class World():
    stoneProbs = 0.2

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.generate()

    def generate(self):

        self.blocks = []

        for y in range(self.height):
            row = []

            for x in range(self.width):
                # if y > 2 and (x in [0, self.width - 1])
                #  or y == self.height - 1:
                #    block = blocks.BedRock()

                if y < 10:
                    block = Sky()
                elif y == 10:
                    block = Grass()
                else:
                    r = random.random()

                    if r <= World.stoneProbs:
                        block = Stone()
                    else:
                        block = Dirt()

                pos = Pos(x, y)
                block.setPos(pos)

                row.append(block)

            self.blocks.append(row)

    def addLadder(self, pos):
        if self.getBlock(pos).getType() != "empty":
            return

        ladder = Ladder()
        ladder.setPos(pos)
        self.blocks[pos.y][pos.x] = ladder

    def setEmpty(self, pos):
        empty = Empty()
        empty.setPos(pos)
        self.blocks[pos.y][pos.x] = empty

    def inside(self, *args):
        if len(args) == 1:
            pos = args[0]
            return 0 <= pos.x < self.width and 0 <= pos.y < self.height

        elif len(args) == 2:
            return 0 <= args[0] < self.width and \
                   0 <= args[1] < self.height

        else:
            return False

    def getBlock(self, *args):
        if len(args) == 1:
            pos = args[0]
            if not self.inside(pos):
                return None

            return self.blocks[pos.y][pos.x]

        elif len(args) == 2:
            if not self.inside(args[0], args[1]):
                return None

            return self.blocks[args[1]][args[0]]

        else:
            return None

    def getNext(self, pos, movement):
        if movement is None:
            return None

        nextPos = pos + movement
        return self.getBlock(nextPos)
