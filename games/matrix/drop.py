import random


class Drop():

    COLOR = [0, 255, 0]

    def __init__(self, maxPos, maxL):
        self.pos = [random.randint(0, maxPos - 1), random.randint(0, 0)]
        self.alpha = 0.3 + random.random() * 0.7
        self.length = random.randint(maxL // 2, maxL)

    def draw(self, screen):
        for dy in range(self.length):
            da = 1 - (dy + 1.0) / self.length
            color = [int(Drop.COLOR[i] * self.alpha * da) for i in range(3)]
            screen.setPixel(self.pos[0], self.pos[1] - dy, color)

    def fall(self):
        self.pos[1] += 1

    def checkDeath(self, maxY):
        if self.pos[1] - self.length == maxY:
            return True

        return False
