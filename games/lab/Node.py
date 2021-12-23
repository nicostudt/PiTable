class Node:

    def __init__(self, pos):
        self.id = hash(pos)
        self.pos = pos
        self.parent = None
        self.children = []
        self.neighbors = []
        self.rootDist = -1
        self.wayNeights = 0

    def getUnvisitedNeights(self):
        neights = []
        for neight in self.neighbors:
            if neight.wayNeights < 5 and neight.rootDist == -1 and not neight.isBlocked():
                neights.append(neight)

        return neights

    def isBlocked(self):
        for neight in self.neighbors:
            if neight.wayNeights > 4:
                return True

        return False

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return self.id