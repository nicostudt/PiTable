class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def addX(self, dx):
        self.x += dx

    def addY(self, dy):
        self.y += dy

    def __add__(self, other):
        if isinstance(other, list):
            return Vector(self.x + other[0], self.y + other[1])
        else:
            return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        if isinstance(other, list):
            self.x += other[0]
            self.y += other[1]
        else:
            self.x += other.x
            self.y += other.y

        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def copy(self):
        return Vector(self.x, self.y)

    def wrapAround(self, size):
        self.x %= size[0]
        self.y %= size[1]

    def negative(self):
        return Vector(self.x * -1, self.y * -1)
