import random
import time
from .colors import *
import utils.colors as cc
from .pos import Pos
import games.lab.field as field

class Labyrinth:

    def __init__(self, size):
        self.size = size
        self.start = Pos(0, 0)
        self.goal = Pos(*size)
        self.resetGeneration()

    def getStartPos(self):
        possibles = []
        possibles += [Pos(x, 0) for x in range(self.size[0])]
        possibles += [Pos(x, self.size[1]) for x in range(self.size[0])]
        possibles += [Pos(0, y) for y in range(self.size[1])]
        possibles += [Pos(self.size[0], y) for y in range(self.size[1])]

        return random.choice(possibles)


    def resetGeneration(self):
        self.state = "generate"
        self.startTime = time.time()
        self.ways = set()
        self.times = {}
        self.walls = set()
        self.stack = []

    def update(self, dt):
        if len(self.stack) > 0:
            head = self.stack[-1]
            self.times[hash(head)] = 0

        keys = list(self.times.keys())
        for key in keys:
            self.times[key] += dt

        self.step()

    def step(self):
        if self.state == "generate":
            #print("\nStep")
            self.appendWay()
        else:
            self.resetGeneration()

    def appendWay(self):
        if len(self.ways) == 0:
            nextPos = self.getStartPos()
            self.addWay(nextPos)
            return

        if len(self.stack) == 0:
            self.state = "none"
            return

        randPos = self.stack[-1]
        neights = self.getFreeNeights(randPos)

        if len(neights) == 0:
            del self.stack[-1]
            return

        if self.goal in neights:
            nextPos = self.goal.clone()
        else:
            nextPos = random.choice(neights)

        self.addWay(nextPos)

    def addWay(self, pos):
        if pos is None:
            return

        self.ways.add(pos)
        self.times[hash(pos)] = 0
        self.stack.append(pos)

        # Add walls
        for neight in field.getNeights(pos, self.size):
            count = sum([1 for x in field.getNeights(neight, self.size) if x in self.ways])
            if count > 1:
                self.walls.add(neight)

    def getFreeNeights(self, pos):
        free = []

        for neight in field.getNeights(pos, self.size):
            if not self.canSetAsWay(neight):
                continue

            free.append(neight)

        return free

    def canSetAsWay(self, pos):
        if pos in self.walls or pos in self.ways:
            return False

        for neight in field.getNeights(pos, self.size):
            if neight not in self.walls:
                continue

            # Count connected walls
            count = sum([1 for x in field.getNeights(neight, self.size) if x not in self.ways])
            if count < 1:
                return False

        return True

        #return pos not in self.ways and pos not in self.walls

    def render(self, display):
        display.fill(cc.getColor("material_black"))

        #for pos in self.ways:
        #    display.setPixel(pos.x, pos.y, WAY_COLOR)

        sinceStart = max(1.0, time.time() - self.startTime)
        print(sinceStart)
        n = float(len(self.stack))

        for i, pos in enumerate(self.ways):
            alpha = self.times[hash(pos)]
            #alpha = i/n

            display.setPixel(pos.x, pos.y, self.getWayColor(alpha))

        if len(self.stack) > 0:
            head = self.stack[-1]
            display.setPixel(head.x, head.y, cc.getColor("material_red"))

    def getWayColor(self, percent):
        return  cc.interpolateBetween([
            [cc.getColor("material_red"), 0.0],
            [cc.getColor("material_darkpurple"), 1],
            [cc.getColor("material_blue"), 2],
            [cc.getColor("material_blue"), 4],
            [cc.getColor("material_black"), 5]], percent)