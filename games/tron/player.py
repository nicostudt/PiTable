class Player():

    DIRS = ["UP", "LEFT", "DOWN", "RIGHT"]

    def __init__(self, color, startPos, startDir):
        self.startPos = startPos
        self.startDir = startDir
        self.color = color
        self.gray = [100, 100, 100]

    def initialize(self):
        self.body = []
        self.death = False
        self.ready = False

        # Prepare Tron
        head = self.startPos

        for i in range(4):
            self.body.append(head)

        self.direction = self.startDir

    def isReady(self):
        return self.ready

    def setReady(self, flag):
        self.ready = flag

    def getColor(self):
        return self.color if self.ready else self.gray

    def grow(self):
        print("Ich growe")
        self.body.append(self.body[-1])

    def getOppositDir(self, dir):
        idx = Player.DIRS.index(dir)
        return Player.DIRS[(idx - 2) % 4]

    def getHead(self):
        return self.body[0]

    def hit(self, other):
        start = 3 if self == other else 0
        return self.getHead() in other.body[start:]

    def isDead(self):
        return self.death
