import random
import time
from .colors import *
import utils.colors as cc
from .pos import Pos
import games.lab.field as field
from .tree import Tree


class Labyrinth:

    def __init__(self, size, start, goal):
        self.size = size
        self.start = start
        self.goal = goal
        self.resetGeneration()


    def resetGeneration(self):
        self.state = "generate"
        self.startTime = time.time()
        self.typeProb = random.random()
        self.maxDist = 0
        print("Type prob", self.typeProb)
        self.clearTree()


    def clearTree(self):
        self.tree = Tree()

        for x in range(self.size[0]):
            for y in range(self.size[1]):
                pos = Pos(x, y)
                self.tree.createNode(pos)

        for node in self.tree.nodes.values():
            for neightPos in field.getNeights(node.pos, self.size):
                node.neighbors.append(self.tree.getNode(neightPos))

        self.tree.setRoot(Pos(0, 0))


    def update(self, dt):
        self.step()

        return self.state == "none"


    def step(self):
        if self.state == "generate":
            self.appendWay()
        else:
            self.resetGeneration()


    def appendWay(self):
        # Choose next node
        if random.random() < self.typeProb:
            currentIdx = random.randint(0, len(self.tree.leafs)-1)
        else:
            currentIdx = -1

        currentNode = self.tree.leafs[currentIdx]

        neights = currentNode.getUnvisitedNeights()
        if not neights:
            del self.tree.leafs[currentIdx]

            if not self.tree.leafs:
                self.state = "none"
            else:
                self.appendWay()

            return

        nextNode = random.choice(neights)
        self.tree.appendTo(currentNode, nextNode)
        self.maxDist = max(self.maxDist, nextNode.rootDist)

    def render(self, display):
        self.renderNodes(display)
        self.renderLeafs(display)


    def renderNodes(self, display):
        for node in self.tree.nodes.values():
            if node.rootDist == -1:
                continue

            display.setPixel(node.pos.x, node.pos.y, [100, 100, 100])


    def renderLeafs(self, display):
        if self.tree.leafs:
            currentNode = self.tree.leafs[-1]
            pos = currentNode.pos
            display.setPixel(pos.x, pos.y, [200, 200, 200])


    def getWayColor(self, percent):
        return  cc.interpolateBetween([
            [cc.getColor("material_red"), 0.0],
            [cc.getColor("material_darkpurple"), 1],
            [cc.getColor("material_blue"), 2],
            [cc.getColor("material_blue"), 4],
            [cc.getColor("material_black"), 5]], percent)