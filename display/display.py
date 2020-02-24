class Display():

    def __init__(self):
        self.brightness = 1

    def init(self):
        pass

    def clear(self):
        pass

    def fill(self, color):
        pass

    def setPixel(self, x, y, color):
        pass

    def show(self):
        pass

    def colorWithBrightness(self, color):
        return [int(color[i] * self.brightness) for i in range(3)]

    def increaseBrightness(self):
        self.brightness = min(1, self.brightness + 0.1)

    def decreaseBrightness(self):
        self.brightness = max(0.1, self.brightness - 0.1)
