from engine.game import Game
from .player import Player
import math
import random

font = {
    0: [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
    1: [[1, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]],
    2: [[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
    3: [[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]]
}

counterColor = [200, 200, 200]


class Tron(Game):

    WASD = ["w", "a", "s", "d"]
    GROW_SECONDS = 4

    def __init__(self):
        Game.__init__(self, "Tron", [16, 16])
        self.fps = 20
        self.frameCounter = 0

        self.players = [
            Player([33, 150, 243], [int(self.size[0] * 1 / 5.0),
                                    int(self.size[1] / 2.0)], "RIGHT"),
            Player([76, 175, 80], [int(self.size[0] * 4 / 5.0),
                                   int(self.size[1] / 2.0)], "LEFT")]
        self.counter = self.fps * Tron.GROW_SECONDS

    def initialize(self):
        self.changeState("startCheck")

    def onAxisMotion(self, playerId, axis, value):
        if axis == "x" and value == -1:
            newDir = "LEFT"
        elif axis == "x" and value == 1:
            newDir = "RIGHT"
        elif axis == "y" and value == -1:
            newDir = "UP"
        elif axis == "y" and value == 1:
            newDir = "DOWN"
        else:
            return

        player = self.players[playerId]
        nextPos = self.getNext(player.getHead(), newDir)

        if nextPos != player.body[1]:
            player.direction = newDir

    def onButtonDown(self, playerId, button):
        if self.state == "startCheck":
            if button == "START":
                player = self.players[playerId]
                player.setReady(True)

                if self.allReady():
                    self.changeState("COUNTDOWN")

        elif self.state == "DEAD":
            if button == "START":
                self.changeState("startCheck")

    def allReady(self):
        for player in self.players:
            if not player.isReady():
                return False

        return True

    def update(self, dt):
        if self.state == "COUNTDOWN":
            self.countdown -= dt

            if self.countdown <= 0:
                self.changeState("GAME")

        elif self.state == "GAME":
            if self.frameCounter % 3 == 0:
                self.grow()
                self.move()
                self.eatApple()
                self.checkDeath()

            if self.oneDead():
                self.changeState("DEAD")

            self.frameCounter += 1

        elif self.state == "DEAD":
            self.deadTimer -= dt

            if self.deadTimer <= 0:
                self.changeState("startCheck")

        # if not self.started or self.oneDead():
            # return

    def render(self, screen):
        screen.fill([0, 0, 0])

        if self.state == "COUNTDOWN":
            self.drawCounter(screen)

        if self.state == "GAME":
            # Draw apple
            screen.setPixel(self.apple[0], self.apple[1], [255, 0, 0])

        self.drawPlayer(screen)

        if self.oneDead():
            for i, player in enumerate(self.players):
                if player.isDead():
                    color = self.players[(i + 1) % 2].getColor()

            for x in range(self.size[0]):
                for y in range(self.size[1]):
                    if x == 0 or x == self.size[0] - 1 \
                            or y == 0 or y == self.size[1] - 1:
                        screen.setPixel(x, y, color)

        screen.show()

    def drawCounter(self, screen):
        upCount = math.ceil(self.countdown)

        alpha = (1 - (upCount - self.countdown) / 1.0) ** 0.2
        color = [alpha * counterColor[i] for i in range(3)]
        letter = font[upCount]

        for dy, row in enumerate(letter):
            for dx, value in enumerate(row):
                if value == 0:
                    continue

                screen.setPixel(7 + dx, 6 + dy, color)

    def drawPlayer(self, screen):
        # Draw dead player over other
        playerList = self.players

        if self.players[0].isDead():
            playerList = reversed(playerList)

        for player in playerList:
            length = float(len(player.body))

            for i, part in enumerate(reversed(player.body)):
                alpha = 0.5 + i / (length - 1) * 0.5
                color = [alpha * player.getColor()[i] for i in range(3)]

                screen.setPixel(part[0], part[1], color)

    def changeState(self, state):
        self.state = state

        if self.state == "startCheck":
            for player in self.players:
                player.initialize()

        elif self.state == "COUNTDOWN":
            self.countdown = 3

        elif self.state == "GAME":
            self.spawnApple()

        elif self.state == "DEAD":
            self.deadTimer = 2

    def grow(self):
        self.counter -= 1

        if self.counter == 0:
            self.counter = self.fps * Tron.GROW_SECONDS

            for player in self.players:
                player.grow()

    def eatApple(self):
        for player in self.players:
            if player.getHead() == self.apple:
                player.grow()
                self.spawnApple()

    def oneDead(self):
        for player in self.players:
            if player.isDead():
                return True

        return False

    def move(self):
        for player in self.players:
            # Add next position
            next = self.getNext(player.getHead(), player.direction)
            player.body.insert(0, next)
            del player.body[-1]

    def spawnApple(self):
        self.apple = [random.randint(0, 15), random.randint(0, 15)]

    def checkDeath(self):
        for player in self.players:
            for other in self.players:
                if player.hit(other):
                    player.death = True
                    break

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

    def getLooped(self, pos):
        return [(pos[0] + self.size[0]) % self.size[0],
                (pos[1] + self.size[1]) % self.size[1]]
