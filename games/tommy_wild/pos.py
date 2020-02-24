import math


class Pos():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, dx, dy):
        self.x += dx
        self.y += dy

    def sub(pos1, pos2):
        return Pos(pos1.x - pos2.x, pos1.y - pos2.y)

    def len(self):
        return math.sqrt(self.x**2 + self.y**2)

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def isKey(self, key):
        if key == "up":
            return self.x == 0 and self.y == -1

        elif key == "down":
            return self.x == 0 and self.y == 1

        return False

    def clone(self):
        return Pos(self.x, self.y)

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)
