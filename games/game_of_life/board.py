from random import random


class Board():

    COLOR = [46, 204, 113]
    NEIGHBORS = [[-1, -1], [-1, 0], [-1, 1], [0, -1],
                 [0, 1], [1, -1], [1, 0], [1, 1]]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rules = {}

    def setRules(self, rules):
        self.rules = rules

    def generateRandom(self):
        self.fields = self.getEmptyField()

        for y in range(self.height):
            for x in range(self.width):
                self.fields[y][x] = random() < 0.3

    def update(self):
        newField = []
        changes = 0

        for y, row in enumerate(self.fields):
            newRow = []

            for x, value in enumerate(row):
                counter = self.countLivingNeighbors(x, y)
                newValue = self.rules[value][counter] != value

                if newValue != value:
                    changes += 1

                newRow.append(newValue)

            newField.append(newRow)

        self.fields = newField

        if changes == 0:
            self.generateRandom()

    def render(self, screen):
        for y, row in enumerate(self.fields):
            for x, value in enumerate(row):
                if value:
                    screen.setPixel(x, y, Board.COLOR)

    def countLivingNeighbors(self, x, y):
        counter = 0

        for dx, dy in Board.NEIGHBORS:
            newX = x + dx
            newY = y + dy

            if not self.inside(newX, newY):
                counter += 1 if self.getOutsideLiving() else 0

            else:
                counter += 1 if self.fields[newY][newX] else 0

        return counter

    def inside(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def getOutsideLiving(self):
        return False

    def getEmptyField(self):
        return [[False for x in range(self.width)] for y in range(self.height)]
