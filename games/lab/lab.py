#!/usr/bin/python

import random
from engine.game import Game
from games.lab.algorithms.bfs import BFS
from games.lab.algorithms.dfs import DFS
from games.lab.colors import *
from games.lab.labyrinth import Labyrinth
from games.lab.pos import Pos
import utils.colors as cc


class Lab(Game):

    STATE_LAB, STATE_ALGO, STATE_NOME = range(3)


    def __init__(self):
        Game.__init__(self, "Snake", [16, 16])
        self.fps = 30
        self.start = Pos(0, 0)
        self.goal = Pos(*[x - 1 for x in self.size])

        self.labyrinth = None
        self.algorithm = None

        self.setState(self.STATE_LAB)


    def setState(self, newState):
        self.state = newState

        if newState == self.STATE_LAB:
            self.labyrinth = Labyrinth(self.size, self.start, self.goal)

        elif newState == self.STATE_ALGO:
            self.initAlgorithm()


    def initAlgorithm(self):
        if random.random() < 0.5:
            self.algorithm = BFS()
        else:
            self.algorithm = DFS()

        self.algorithm.create(self.labyrinth.tree, self.goal)


    def onButtonDown(self, player, button):
        if button == "START":
            self.step(1)


    def onAxisMotion(self, player, axis, value):
        if axis == "x":
            if value == -1:
                self.fps = max(1, self.fps - 5)

            if value == 1:
                self.fps = min(56, self.fps + 5)

            print(self.fps)



    def update(self, dt):
        self.step(dt)

    def step(self, dt):
        if self.state == self.STATE_LAB:
            #if self.labyrinth.update(dt):
            while not self.labyrinth.update(dt):
                self.setState(self.STATE_ALGO)

        else:
            if self.algorithm.update(dt):
                self.setState(self.STATE_LAB)

    def render(self, display):
        display.fill(cc.getColor("material_black"))

        if self.state == self.STATE_LAB:
            self.labyrinth.render(display)

        else:
            #self.labyrinth.renderNodes(display)

            for node, time in self.algorithm.usedNodes:
                alpha = time #node.rootDist / self.algorithm.maxDist

                color = cc.interpolateBetween([
                    [cc.getColor("material_white"), 0.0],
                    [cc.getColor("material_lightblue"), 1],
                    [cc.getColor("material_blue"), 2],
                    [cc.getColor("material_black"), 4]],
                    alpha)
                """
                color = cc.interpolateBetween([
                    [cc.getColor("material_yellow"), 0.0],
                    [cc.getColor("material_orange"), 20.0/self.fps],
                    [cc.getColor("material_red"), 30.0/self.fps],
                    [cc.getColor("material_black"), 80.0/self.fps]],
                    alpha)
                """
                display.setPixel(node.pos.x, node.pos.y, color)

        display.show()