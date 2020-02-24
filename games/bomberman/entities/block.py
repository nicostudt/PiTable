from .entity import Entity


class Block(Entity):

    def __init__(self, pos, item=None):
        Entity.__init__(self, pos, [188, 170, 164])  # [161, 136, 127])

        self.item = item
