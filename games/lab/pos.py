import math

class Pos:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, dx, dy):
        self.x += dx
        self.y += dy

    def len(self):
        return abs(self.x) + abs(self.y)

    def dist(self, other):
        #return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return abs(self.x - other.x) + abs(self.y - other.y)

    def clone(self):
        return Pos(self.x, self.y)

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "[%d, %d]" %(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Pos):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def fromHash(hash):
        return Pos(hash // 128, hash %128)

    def __hash__(self):
        return self.x * 128 + self.y