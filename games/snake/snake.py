#!/usr/bin/python

from engine.game import Game
import random


class Snake(Game):

    DIRS = ["UP", "LEFT", "DOWN", "RIGHT"]

    def __init__(self):
        Game.__init__(self, "Snake", [16, 16])
        self.fps = 4
        self.color = [33, 150, 243]  # [76, 175, 80]
        self.counter = 4

    def initialize(self):
        self.fps = 4
        self.started = False
        self.body = []
        self.death = False

        # Prepare Snake
        head = [self.size[0] // 2, self.size[1] // 2]
        self.body.append(head)
        self.body.append(head)
        self.direction = "UP"

        self.blocks = []

        while len(self.blocks) < 3:
            x = random.randint(0, self.size[0] - 1)
            y = random.randint(0, self.size[1] - 1)

            dist = abs(head[0] - x) + abs(head[1] - y)

            if dist < 3:
                continue

            self.blocks.append([x, y])

        # Add apple
        self.spawnApple()

    def onButtonDown(self, player, button):
        if player != 0:
            return

        if button == "START":
            if not self.started:
                self.started = True
            elif self.death:
                self.initialize()

    def onAxisMotion(self, player, axis, value):
        if player != 0:
            return

        newDir = None

        if axis == "x" and value == 1:
            newDir = "RIGHT"
        elif axis == "x" and value == -1:
            newDir = "LEFT"

        elif axis == "y" and value == -1:
            newDir = "UP"
        elif axis == "y" and value == 1:
            newDir = "DOWN"

        if newDir:
            nextPos = self.getNext(self.getHead(), newDir)

            if nextPos != self.body[1]:
                self.direction = newDir

    def update(self, dt):
        if not self.started or self.death:
            return

        self.move()
        self.eat()
        self.checkDeath()

    def render(self, display):
        display.fill([0, 0, 0])

        length = float(len(self.body))

        for block in self.blocks:
            display.setPixel(block[0], block[1], [0, 255, 0])

        for i, part in enumerate(reversed(self.body)):
            alpha = 0.5 + i / (length - 1) * 0.5
            color = [int(alpha * self.color[i]) for i in [0, 1, 2]]

            display.setPixel(part[0], part[1], color)

        display.setPixel(self.apple[0], self.apple[1], [255, 0, 0])

        display.show()

    def spawnApple(self):
        # Try to spawn apple on a random free field
        while True:
            x = random.randint(0, self.size[0] - 1)
            y = random.randint(0, self.size[1] - 1)

            if [x, y] in self.blocks:
                break

            if not self.hit([x, y]):
                self.apple = [x, y]
                break

        # make game harder / increase fps
        self.counter -= 1
        if self.counter == 0:
            self.counter = 3
            self.fps = self.fps * 1.07

    def hit(self, pos):
        return pos in self.body

    def move(self):
        # Add next position
        next = self.getNext(self.getHead(), self.direction)
        self.body.insert(0, next)

        # Delete last
        del self.body[-1]

    def eat(self):
        if self.getHead() == self.apple:
            # Insert Apple at head pos
            #self.body.insert(0, self.apple)

            # Insert Apple at tail
            self.body.append(self.body[-1])

            self.spawnApple()

    def checkDeath(self):
        if self.getHead() in self.body[1:] or self.getHead() in self.blocks:
            # Death detected
            self.death = True

    def getHead(self):
        return self.body[0]

    def getNext(self, pos, direction):
        if direction == "UP":
            next = [pos[0], pos[1] - 1]
        elif direction == "DOWN":
            next = [pos[0], pos[1] + 1]
        elif direction == "LEFT":
            next = [pos[0] - 1, pos[1]]
        elif direction == "RIGHT":
            next = [pos[0] + 1, pos[1]]
        else:
            return None

        return self.getLooped(next)

    def getOppositDir(self, dir):
        idx = Snake.DIRS.index(dir)
        return Snake.DIRS[(idx - 2) % 4]

    def getLooped(self, pos):
        return [(pos[0] + self.size[0]) % self.size[0],
                (pos[1] + self.size[1]) % self.size[1]]
