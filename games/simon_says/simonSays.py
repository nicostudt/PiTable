from engine.game import Game
import math
from .ring import Ring
import random


class SimonSays(Game):

    def __init__(self):
        Game.__init__(self, "SimonSays", [16, 16])
        self.fps = 30
        self.colors = [[0, 0, 255], [255, 0, 0], [255, 255, 0], [0, 255, 0]]
        self.rings = []

        self.showTimerMax = 1

    def initialize(self):
        self.simon = []
        self.switchState("show")

    def onButtonDown(self, player, button):
        if self.state == "repeat" and button in "XABY":
            value = "XABY".index(button)

            if self.askSimon(self.repeatIdx, value):
                self.addRing(value)
                self.repeatIdx += 1

                if self.repeatIdx >= len(self.simon):
                    self.switchState("show")
            else:
                self.switchState("lose")

        if self.state == "lose" and button == "START":
            self.initialize()

    def update(self, dt):
        for ring in self.rings:
            ring.update(dt)

            if ring.isDead():
                self.rings.remove(ring)

        if self.state == "show":
            self.showTimer += dt

            if self.showTimer >= self.showTimerMax:

                if self.showIndex >= len(self.simon):
                    self.switchState("repeat")
                else:
                    self.addRing(self.simon[self.showIndex])

                self.showTimer -= self.showTimerMax
                self.showIndex += 1

        elif self.state == "lose":
            self.loseTimer += dt

            if self.loseTimer >= 2:
                self.initialize()

    def render(self, screen):
        screen.fill([0, 0, 0])

        self.drawRings(screen)

        if self.state == "lose":
            self.drawLose(screen)

        screen.show()

    def drawLose(self, screen):
        alpha = -((self.loseTimer * 3 - 1)**2) + 1

        if alpha <= 0:
            return

        red = [255, 0, 0]

        for y in range(16):
            for x in range(16):
                dist = min(x, 15 - x, y, 15 - y)

                if dist > 3:
                    continue

                color = [(1 - (dist) / 3.0) * alpha * red[i]
                         for i in range(3)]
                screen.setPixel(x, y, color)

    def drawRings(self, screen):
        if len(self.rings) == 0:
            return

        for y in range(16):
            for x in range(16):
                minDist = 16
                color = None

                for ring in self.rings:
                    dist = abs(ring.animRadius - self.distToMiddle(x, y))

                    if dist < minDist:
                        minDist = dist
                        color = ring.color

                if not color:
                    continue

                alpha = -(minDist / 1.5) ** 2 + 1
                if alpha < 0:
                    continue

                c = [alpha * color[i] for i in range(3)]
                screen.setPixel(x, y, c)

    def addRing(self, idx):
        ring = Ring(self.colors[idx])
        self.rings.append(ring)

    def switchState(self, state):
        if state == "show":
            self.showTimer = -self.showTimerMax
            self.showIndex = 0
            self.addSimon()

        elif state == "repeat":
            self.repeatIdx = 0

        elif state == "lose":
            self.loseTimer = 0

        self.state = state

    def askSimon(self, idx, value):
        return self.simon[idx] == value

    def addSimon(self):
        self.simon.append(random.randint(0, len(self.colors) - 1))

    def distToMiddle(self, x, y):
        dx = x - 7.5
        dy = y - 7.5

        return math.sqrt(dx**2 + dy**2)
