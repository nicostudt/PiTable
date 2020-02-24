class Vec():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

        return self

    def add(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y

    def isZero(self):
        return self.x == 0 and self.y == 0

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"
