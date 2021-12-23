#!/usr/bin/python

import pygame
from .display import Display
import os

class PygamePixelDisplay(Display):

    def __init__(self, caption="Default", width=600, height=600,
                 gridSize=[16, 16], space=4):

        Display.__init__(self)

        self.caption = caption
        self.width = width
        self.height = height
        self.gridSize = gridSize
        self.space = float(space)

    def init(self):
        # Create window to draw on
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.window = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(self.caption)

        self.dSize = [(self.width - self.space * (self.gridSize[0] + 1))
                      / self.gridSize[0],
                      (self.height - self.space * (self.gridSize[1] + 1))
                      / self.gridSize[1]]

        self.dw = [self.dSize[i] + self.space for i in [0, 1]]

    def clear(self):
        self.window.fill([0, 0, 0])

    def fill(self, color):
        color = self.colorWithBrightness(color)
        self.window.fill(color)

    def setPixel(self, x, y, color):
        color = self.colorWithBrightness(color)

        dx = self.space + x * self.dw[0]
        dy = self.space + y * self.dw[1]

        rect = [dx, dy, self.dSize[0], self.dSize[1]]

        pygame.draw.rect(self.window, color, rect)

    def show(self):
        pygame.display.flip()
