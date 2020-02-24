import games.tommy_wild.colors as colors
from engine.game import Game
from .camera import Camera
from .fog import Fog
from .tommy import Tommy
from .world import World
from .pos import Pos


class TommyWild(Game):

    def __init__(self):
        Game.__init__(self, "Tommy Wild", [16, 16])
        self.fps = 10
        self.fog = Fog(colors.getColor("black"), 0.0)
        self.bloodColor = colors.getColor("red")
        self.camera = Camera(self.size)

    def initialize(self):
        startPos = Pos(20, 9)

        self.world = World(100, 100)
        self.tommy = Tommy(self.world)
        self.tommy.setPos(startPos)

        self.camera.setOffset(self.tommy.pos)

    def onButtonDown(self, player, button):
        if player != 0:
            return

        if button == "A":
            self.world.addLadder(self.tommy.pos)

    def onAxisMotion(self, player, axis, value):
        if player != 0:
            return

        if axis == "x":
            self.tommy.setMovement(Pos(int(value), 0))
        elif axis == "y":
            self.tommy.setMovement(Pos(0, int(value)))

    def update(self, dt):
        self.tommy.update(dt)
        self.camera.updateOffset(self.tommy.pos)

    def render(self, screen):
        screen.fill([0, 0, 0])

        self.blood = self.tommy.getDeath()

        for y in range(self.size[1]):
            for x in range(self.size[0]):
                self.renderBlock(screen, x, y)

        x, y = self.camera.translateToPx(self.tommy.pos)
        screen.setPixel(x, y, self.tommy.getColor())

        screen.show()

    def renderBlock(self, screen, x, y):
        worldpos = self.camera.translate(x, y)
        block = self.world.getBlock(worldpos)

        if block is None:
            return

        # define colors
        color = block.getColor()
        color = self.fog.getColor(
            color, self.tommy.pos, worldpos, self.tommy.getSight())

        # Render blood
        if self.blood > 0:
            dist = min(x, self.size[0] - x - 1,
                       y, self.size[1] - y - 1)
            if dist < 5:
                alpha = 0.5 * (1 - dist / 5.0) * self.blood
                color = colors.interpolateColor(color, self.bloodColor, alpha)

        screen.setPixel(x, y, color)
