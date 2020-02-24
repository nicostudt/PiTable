#!/usr/bin/python

from engine.game import Game
import games
from .gameEntry import GameEntry
import games.home.font as font


class Home(Game):

    GAMES = [
        ["bomberman", [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0]],
            [[0, 0, 0], [200, 180, 20], [230, 200, 50], [0, 0, 0]],
            [[190, 190, 190], [210, 210, 210], [0, 0, 0], [0, 0, 0]],
            [[180, 180, 180], [200, 200, 200], [0, 0, 0], [0, 0, 0]]]],
        ["game of life", [
            [[0, 0, 0], [46, 204, 113], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [46, 204, 113], [0, 0, 0]],
            [[46, 204, 113], [46, 204, 113], [46, 204, 113], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]],
        ["matrix", [
            [[0, 150, 0], [0, 100, 0], [0, 255, 0], [0, 200, 0]],
            [[0, 200, 0], [0, 150, 0], [0, 0, 0], [0, 255, 0]],
            [[0, 255, 0], [0, 200, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0]]]],
        ["pyhero", [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0]],
            [[0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 255, 0], [255, 255, 0], [0, 0, 255], [255, 0, 0]]]],
        ["simon says", [
            [[0, 0, 255], [0, 0, 255], [255, 0, 0], [255, 0, 0]],
            [[0, 0, 255], [0, 0, 0], [0, 0, 0], [255, 0, 0]],
            [[0, 255, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0]],
            [[0, 255, 0], [0, 255, 0], [255, 255, 0], [255, 255, 0]]]],
        ["snake", [
            [[0, 0, 0], [33, 150, 243], [33, 150, 243], [33, 150, 243]],
            [[33, 150, 243], [33, 150, 243], [0, 0, 0], [33, 150, 243]],
            [[33, 150, 243], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[33, 150, 243], [0, 0, 0], [0, 0, 0], [255, 0, 0]]]],
        ["anim", [
            [[183, 231, 113], [57, 35, 107], [242, 115, 66], [235, 8, 115]],
            [[80, 188, 144], [51, 104, 124], [210, 127, 160], [28, 96, 214]],
            [[245, 152, 71], [183, 216, 41], [71, 56, 197], [164, 136, 138]],
            [[228, 84, 114], [108, 39, 124], [103, 17, 152], [199, 183, 203]]]],
        ["tommy wild", [
            [[52, 152, 219], [52, 152, 219], [52, 152, 219], [52, 152, 219]],
            [[52, 152, 219], [52, 152, 219], [255, 0, 0], [52, 152, 219]],
            [[46, 204, 113], [46, 204, 113], [46, 204, 113], [46, 204, 113]],
            [[121, 85, 72], [127, 140, 141], [121, 85, 72], [121, 85, 72]]]],
        ["tron", [
            [[52, 152, 219], [52, 152, 219], [52, 152, 219], [52, 152, 219]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [52, 152, 219]],
            [[231, 76, 60], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[231, 76, 60], [231, 76, 60], [231, 76, 60], [231, 76, 60]]]],
    ]

    """
        ["space invaders", [
            [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
            [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
            [[0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
            [[255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255]]]],

        ["anim", [
            [[183, 231, 113], [57, 35, 107], [242, 115, 66], [235, 8, 115]],
            [[80, 188, 144], [51, 104, 124], [210, 127, 160], [28, 96, 214]],
            [[245, 152, 71], [183, 216, 41], [71, 56, 197], [164, 136, 138]],
            [[228, 84, 114], [108, 39, 124], [103, 17, 152], [199, 183, 203]]]],
    """

    def __init__(self):
        Game.__init__(self, "Home", [16, 16])

    def initialize(self):
        self.fps = 20
        self.idx = 0
        self.gameEntries = []

        for name, image in Home.GAMES:
            self.gameEntries.append(GameEntry(name, image))

        self.gameEntries[self.idx].show(True)
        self.gameEntries[self.idx].dy = -3
        self.gameEntries[self.idx].brightness = 1

        self.runIndex = self.size[0]
        self.counter = 0

    def setEngine(self, engine):
        self.engine = engine

    def update(self, dt):
        for gameEntry in self.gameEntries:
            gameEntry.update()

        self.counter += 1

        if self.counter == 1:
            self.counter = 0
            self.runIndex -= 1

        if self.runIndex < -5 * 4:
            self.runIndex = self.size[0]

    def onButtonDown(self, player, button):
        if player != 0:
            return

        if button == "START":
            self.startGame()

    def onAxisMotion(self, player, axis, value):
        if player != 0:
            return

        if axis == "y" and value == -1:
            self.changeIdx(1)
        elif axis == "y" and value == 1:
            self.changeIdx(-1)

    def changeIdx(self, dx):
        self.gameEntries[self.idx].show(False)
        self.idx = (self.idx + dx) % len(self.gameEntries)
        self.gameEntries[self.idx].show(True)

    def startGame(self):
        game = Home.GAMES[self.idx][0]

        if game == "bomberman":
            self.engine.setGame(games.Bomberman())
        if game == "game of life":
            self.engine.setGame(games.GameOfLife())
        elif game == "matrix":
            self.engine.setGame(games.Matrix())
        elif game == "pyhero":
            self.engine.setGame(games.PyHero())
        elif game == "simon says":
            self.engine.setGame(games.SimonSays())
        elif game == "snake":
            self.engine.setGame(games.Snake())
        elif game == "space invaders":
            self.engine.setGame(games.SpaceInvaders())
        elif game == "screensaver":
            self.engine.setGame(games.Test())
        elif game == "tommy wild":
            self.engine.setGame(games.TommyWild())
        elif game == "tron":
            self.engine.setGame(games.Tron())

    def render(self, display):
        display.fill([0, 0, 0])

        for gameEntry in self.gameEntries:
            dy = gameEntry.dy

            for i, l in enumerate(gameEntry.name):
                dx = 4 * i + gameEntry.dx
                self.printLetter(dx, dy, l, display)

        for gameEntry in self.gameEntries:
            dy = gameEntry.dy

            for i, l in enumerate(gameEntry.name):
                dx = 4 * i + gameEntry.dx
                # self.printLetter(dx, dy, l, display)

            # display image
            image = gameEntry.getImage()

            if image is not None:
                self.displayImage(6, 10, image, display)

        display.show()

    def displayImage(self, dx, dy, image, display):
        for y, row in enumerate(image):
            for x, color in enumerate(row):
                display.setPixel(x + dx, y + dy, color)

    def printLetter(self, dx, dy, letter, display):
        letterMatrix = font.getLetter(letter)

        for y, row in enumerate(letterMatrix):
            if y + dx >= self.size[1]:
                break

            for x, value in enumerate(row):
                if 0 > x + dx <= self.size[0] or value == 0:
                    continue

                display.setPixel(x + dx, y + dy, [255, 255, 255])
