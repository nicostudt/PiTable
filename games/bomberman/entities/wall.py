from .entity import Entity


class Wall(Entity):

    def __init__(self, pos):
        Entity.__init__(self, pos, [100, 100, 100])
