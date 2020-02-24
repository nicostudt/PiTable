class Bullet():

    def __init__(self, pos, vel, color):
        self.pos = pos
        self.vel = vel
        self.color = color

    def colide(self, body):
        return self.pos in body

    def move(self):
        self.pos = [self.pos[0] + self.vel[0], self.pos[1] + self.vel[1]]

    def isOutside(self):
        return self.pos[1] < 0 or self.pos[1] > 15
