class Shooter():

    def __init__(self, pos, body, color):
        self.pos = pos
        self.body = body
        self.color = color

    def getColor(self):
        return self.color

    def getBody(self):
        return [[self.pos[i] + d[i] for i in [0, 1]] for d in self.body]

    def destroy(self, pos):
        pos = [pos[i] - self.pos[i] for i in range(2)]
        self.body.remove(pos)

    def isDead(self):
        return len(self.body) == 0
