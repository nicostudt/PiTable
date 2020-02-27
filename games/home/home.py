#!/usr/bin/python

from engine.game import Game
import games
from .gameEntry import GameEntry
import utils.font5x3 as font


class Home(Game):

    GAMES = [
        ["Bomberman", [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0]],
            [[0, 0, 0], [200, 180, 20], [230, 200, 50], [0, 0, 0]],
            [[190, 190, 190], [210, 210, 210], [0, 0, 0], [0, 0, 0]],
            [[180, 180, 180], [200, 200, 200], [0, 0, 0], [0, 0, 0]]]],
        ["Bird", [
            [[6, 35, 80], [6, 35, 80], [6, 35, 80], [41, 182, 101]],
            [[231, 76, 60], [26, 32, 85], [26, 32, 85], [26, 32, 85]],
            [[231, 76, 60], [41, 182, 101], [57, 31, 84], [57, 31, 84]],
            [[116, 60, 18], [41, 182, 101], [116, 60, 18], [41, 182, 101]]]],
        ["Game of Life", [
            [[0, 0, 0], [46, 204, 113], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [46, 204, 113], [0, 0, 0]],
            [[46, 204, 113], [46, 204, 113], [46, 204, 113], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]],
        ["Dino", [
            [[0, 0, 0], [231, 76, 60], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [231, 76, 60], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
            [[42, 190, 105], [41, 182, 101], [30, 136, 75], [20, 89, 49]]]],
        ["Matrix", [
            [[0, 150, 0], [0, 100, 0], [0, 255, 0], [0, 200, 0]],
            [[0, 200, 0], [0, 150, 0], [0, 0, 0], [0, 255, 0]],
            [[0, 255, 0], [0, 200, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 255, 0], [0, 0, 0], [0, 0, 0]]]],
        ["Pyhero", [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0]],
            [[0, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 255, 0], [255, 255, 0], [0, 0, 255], [255, 0, 0]]]],
        ["Simon Says", [
            [[0, 0, 255], [0, 0, 255], [255, 0, 0], [255, 0, 0]],
            [[0, 0, 255], [0, 0, 0], [0, 0, 0], [255, 0, 0]],
            [[0, 255, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0]],
            [[0, 255, 0], [0, 255, 0], [255, 255, 0], [255, 255, 0]]]],
        ["Snake", [
            [[0, 0, 0], [33, 150, 243], [33, 150, 243], [33, 150, 243]],
            [[33, 150, 243], [33, 150, 243], [0, 0, 0], [33, 150, 243]],
            [[33, 150, 243], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[33, 150, 243], [0, 0, 0], [0, 0, 0], [255, 0, 0]]]],
        ["Anim", [
            [[183, 231, 113], [57, 35, 107], [242, 115, 66], [235, 8, 115]],
            [[80, 188, 144], [51, 104, 124], [210, 127, 160], [28, 96, 214]],
            [[245, 152, 71], [183, 216, 41], [71, 56, 197], [164, 136, 138]],
            [[228, 84, 114], [108, 39, 124], [103, 17, 152], [199, 183, 203]]]],
        ["Tommy Wild", [
            [[52, 152, 219], [52, 152, 219], [52, 152, 219], [52, 152, 219]],
            [[52, 152, 219], [52, 152, 219], [255, 0, 0], [52, 152, 219]],
            [[46, 204, 113], [46, 204, 113], [46, 204, 113], [46, 204, 113]],
            [[121, 85, 72], [127, 140, 141], [121, 85, 72], [121, 85, 72]]]],
        ["Tron", [
            [[52, 152, 219], [52, 152, 219], [52, 152, 219], [52, 152, 219]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [52, 152, 219]],
            [[231, 76, 60], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[231, 76, 60], [231, 76, 60], [231, 76, 60], [231, 76, 60]]]]
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
            matrix = font.getTextMatrix(name)
            self.gameEntries.append(GameEntry(matrix, image))

        self.gameEntries[self.idx].show(True)
        self.gameEntries[self.idx].dy = -self.gameEntries[self.idx].pixelHeight
        self.gameEntries[self.idx].brightness = 1


    def setEngine(self, engine):
        self.engine = engine


    def update(self, dt):
        for gameEntry in self.gameEntries:
            gameEntry.update()


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
        game = game.lower()

        if game == "bomberman":
            self.engine.setGame(games.Bomberman())
        if game == "bird":
            self.engine.setGame(games.BirdGame())
        if game == "game of life":
            self.engine.setGame(games.GameOfLife())
        elif game == "dino":
            self.engine.setGame(games.Dino())
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


    def render(self, screen):
        screen.fill([0, 0, 0])

        for gameEntry in self.gameEntries:
            self.displayFont(screen, gameEntry)

            # display image
            image = gameEntry.getImage()

            if image is not None:
                self.displayImage(6, 8, image, screen)

        screen.show()


    def displayImage(self, dx, dy, image, screen):
        for y, row in enumerate(image):
            for x, color in enumerate(row):
                screen.setPixel(x + dx, y + dy, color)


    def displayFont(self, screen, entry):
        dx = entry.dx
        dy = entry.dy
        matrix = entry.getMatrix()
        c = int(entry.brightness * 200)
        color = [c, c, c]

        if dy + len(matrix) < 0:
            return

        for y, row in enumerate(matrix):
            for x, value in enumerate(row):
                if value == 0 or not self.onScreen(x + dx, y + dy):
                    continue

                screen.setPixel(x + dx, y + dy, color)
