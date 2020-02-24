#!/usr/bin/python


import pygame


class Screen(object):

    def __init__(self, gridSize, window, space=0):
        self.gridSize = gridSize
        self.space = float(space)
        self.window = window
        self.dSize = [(window.get_size()[i] - space *
                       (gridSize[i] + 1)) / gridSize[i] for i in [0, 1]]
        self.dw = [self.dSize[i] + self.space for i in [0, 1]]

        self.grid = []
        self.drawInstructions = []
        self.fillColor = [0, 0, 0]  # [55, 64, 70]  # [0, 0, 0]

    def clear(self):
        self.grid = [[0 for x in range(self.gridSize[0])]
                     for y in range(self.gridSize[1])]

    def render(self):
        self.window.fill(self.fillColor)

        for instruct in self.drawInstructions:
            dx = self.space + instruct[0] * self.dw[0]
            dy = self.space + instruct[1] * self.dw[1]

            rect = [dx, dy, self.dSize[0], self.dSize[1]]

            pygame.draw.rect(self.window, instruct[2], rect)

        self.drawInstructions = []

    def setPixel(self, x, y, color):
        self.drawInstructions.append([x, y, color])
