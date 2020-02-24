from engine.game import Game
from .spritesheet import Spritesheet
import pygame
import os
import random


class Anim(Game):

    def __init__(self):
        Game.__init__(self, "Test", [16, 16])
        self.fps = 7

        try:
            import RPi.GPIO as gpio
            pygame.display.set_mode([16, 16])
            self.ref = "/home/pi/Documents/pixelGames/games/anim/gifs"

        except ImportError:
            script_path = os.path.dirname(os.path.realpath(__file__))
            self.ref = os.path.join(script_path, "gifs")

        self.switchTime = 20
        self.sheets = []

    def load_sheets(self):
        self.sheets = []

        for filename in os.listdir(self.ref):
            sheet = Spritesheet(os.path.join(self.ref, filename))

            if sheet.height == 16:
                self.sheets.append(sheet)
                print("Loaded " + filename)

    def initialize(self):
        if len(self.sheets) == 0:
            self.load_sheets()

        self.counter = 0
        self.timer = 0
        self.updateGifIdx()

    def updateGifIdx(self):
        self.gifIdx = random.randint(0, len(self.sheets) - 1)

    def update(self, dt):
        self.timer += dt

        if self.timer > self.switchTime:
            self.timer -= self.switchTime
            self.updateGifIdx()

    def render(self, screen):
        screen.fill([0, 0, 0])

        sheet = self.sheets[self.gifIdx]
        self.counter = (self.counter + 1) % sheet.length
        frame = sheet.getImage(self.counter)

        for y in range(16):
            for x in range(16):
                color = frame.get_at((x, y))[:3]
                screen.setPixel(x, y, color)

        """
        self.counter += 1

        if self.counter % 2 == 0:
            for y in range(16):
                for x in range(16):
                    r = random.randint(0, 255)
                    g = random.randint(0, 255)
                    b = random.randint(0, 255)
                    screen.setPixel(x, y, [r, g, b])
        """
        screen.show()
