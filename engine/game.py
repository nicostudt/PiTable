#!/usr/bin/python


class Game(object):

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.fps = 20

    def initialize(self):
        pass

    def onAxisMotion(self, player, axis, value):
        pass

    def onButtonDown(self, player, button):
        pass

    def onButtonUp(self, player, button):
        pass

    def mouseInput(self):
        pass

    def onButtonPressed(self, btn):
        pass

    def onMouseMoved(self, pos):
        pass

    def onMouseButtonPressed(self, btn, pos):
        pass

    def onMouseButtonReleased(self, btn, pos):
        pass

    def onKeyPressed(self, key):
        pass

    def onKeyReleased(self, key):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        # Test screen
        for y in range(16):
            start = 0 if y % 2 == 0 else 1
            for x in range(start, 16, 2):
                screen.setPixel(x, y, [255, 255, 255])

    def quit(self):
        pass

    def getFps(self):
        return self.fps

    def getSize(self):
        return self.size

    def getName(self):
        return self.name
