import games.tommy_wild.colors as colors
from games.tommy_wild.pos import Pos
from games.tommy_wild.blocks.block import Block


class Tommy(Block):

    COLOR = colors.getColor("red")
    FALL_COUNTDOWN = 0.2

    def __init__(self, world):
        Block.__init__(self)

        self.world = world
        self.movement = None
        self.sight = 2

    def update(self, dt):
        # Fall
        self.fallTimer -= dt

        if self.falling and self.fallTimer <= 0:
            self.fallCounter += 1
            self.movement = Pos(0, 1)

        currentBlock = self.world.getBlock(self.pos)
        nextBlock = self.world.getNext(self.pos, self.movement)

        # Move tommy and get action
        action = self.move(currentBlock, nextBlock)

        if action == "destroy":
            self.world.setEmpty(nextBlock.pos)

        # Check fall
        underBlock = self.world.getNext(self.pos, Pos(0, 1))
        currentBlock = self.world.getBlock(self.pos)

        if not self.falling and underBlock.getType() == "empty" \
                and not currentBlock.isClimbable():
            self.falling = True
            self.fallCounter = 0
            self.fallTimer = Tommy.FALL_COUNTDOWN

        elif self.falling and underBlock.getType() != "empty":
            self.falling = False
            dLife = max(0, self.fallCounter - 3)
            self.addLife(-dLife)

    def move(self, currentBlock, nextBlock):
        if nextBlock is None or self.movement is None:
            return "error"

        elif nextBlock.isWalkable():
            if self.movement.isKey("up") and not currentBlock.isClimbable():
                self.movement = None
                return "stuck"

            else:
                self.pos += self.movement
                #self.movement = None
                return "move"
        else:
            nextBlock.addLife(-1)

            if nextBlock.getLife() == 0:
                if self.movement.isKey("down"):
                    self.movement = None

                return "destroy"
            else:
                return "dig"

    def setSight(self, sight):
        self.sight = sight

    def getSight(self):
        return self.sight

    def setMovement(self, movement):
        self.movement = movement

    def getMaxLife(self):
        return 10

    def getType(self):
        return "tommy"

    def getColor(self):
        return Tommy.COLOR
