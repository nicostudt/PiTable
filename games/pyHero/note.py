class Note():
    def __init__(self, duration):
        self.duration = duration
        self.y = 0
    def move(self,dy):
        self.y += dy
    def update(self):
        pass
