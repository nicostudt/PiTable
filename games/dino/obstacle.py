class Obstacle():

    def __init__(self, x, body):
        self.x = x
        self.body = [[x + dx, dy] for dx, dy in body]

    def getBody(self):
        return self.body
