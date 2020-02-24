class Ring():

    def __init__(self, color, radius=12):
        self.color = color
        self.timer = 0
        self.radius = radius
        self.animRadius = 0

    def update(self, dt):
        self.timer += dt
        self.animRadius = self.timer * self.radius

    def isDead(self):
        return self.timer > 1.5
