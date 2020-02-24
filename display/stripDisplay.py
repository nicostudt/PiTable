#!/usr/bin/python

from display import Display

import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI


class StripDisplay(Display):

    CORRECTION = [
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,
        1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,
        2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
        5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
        10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
        17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
        25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
        37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
        51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
        69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
        90, 92, 93, 95, 96, 98, 99, 101, 102, 104, 105, 107, 109, 110, 112,
        114, 115, 117, 119, 120, 122, 124, 126, 127, 129, 131, 133, 135, 137,
        138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164,
        167, 169, 171, 173, 175, 177, 180, 182, 184, 186, 189, 191, 193, 196,
        198, 200, 203, 205, 208, 210, 213, 215, 218, 220, 223, 225, 228, 231,
        233, 236, 239, 241, 244, 247, 249, 252, 255]

    def __init__(self, width=16, height=16):
        Display.__init__(self)

        self.width = width
        self.height = height
        self.pixelCount = width * height

    def init(self):
        SPI_PORT = 0
        SPI_DEVICE = 0

        self.pixels = Adafruit_WS2801.WS2801Pixels(
            self.pixelCount, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

        # Make sure to clear out any displayed color
        self.pixels.clear()

        # Init matrix
        self.matrix = [[0 for _ in range(self.width)]
                       for _ in range(self.height)]

        """
        counter = 0
        for y in range(self.height):
            for x in range(self.width):
                if y % 2 != 0:
                    self.matrix[y][x] = counter
                else:
                    self.matrix[y][self.width - x - 1] = counter

                counter += 1
        """

        # 180 Grad drehung
        counter = 0
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width - 1, -1, -1):
                if y % 2 == 0:
                    self.matrix[y][x] = counter
                else:
                    self.matrix[y][self.width - x - 1] = counter

                counter += 1

    def clear(self):
        self.pixels.clear()

    def fill(self, color):
        if color != [0, 0, 0]:
            color = self.getCorrected(color)
            color = self.colorWithBrightness(color)
        else:
            color = [0, 0, 0]

        for i in range(self.pixelCount):
            self.pixels.set_pixel_rgb(i, color[0], color[1], color[2])

    def setPixel(self, x, y, color):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return

        idx = self.matrix[y][x]

        if color != [0, 0, 0]:
            color = self.getCorrected(color)
            color = self.colorWithBrightness(color)
        else:
            color = [0, 0, 0]

        self.pixels.set_pixel_rgb(idx, color[0], color[1], color[2])

    def getCorrected(self, color):
        return [StripDisplay.CORRECTION[int(color[i])] for i in range(3)]

    def show(self):
        self.pixels.show()
