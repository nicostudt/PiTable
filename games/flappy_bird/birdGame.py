from engine.game import Game
import random
from player import Player
from obstacle import Obstacle
import utils.simplexnoise.noise as snoise
from utils.colors import *


class BirdGame(Game):

    def __init__(self):
        Game.__init__(self, "Bird", [16, 16])
        self.fps = 30
        self.noise = snoise.SimplexNoise(2, 1, 2)
        self.x = 0
        self.skyX = 0
        self.skyDX = 2
        self.grassX = 0
        self.grassDX = 4
        self.obstacleDx = 8
        self.obstacleDist = 8

        self.initColors()

    def initialize(self):
        self.running = False
        self.dead = False
        self.player = Player("material_red")
        self.obstacles = []

        for i in range(3):
            self.addObstacle(25 + i*self.obstacleDist)

    def initColors(self):
        self.obstacleColor = getColor("material_green")
        skyBlue = getColor("material_darkblue")
        skyPurple = getColor("material_darkpurple")
        skyOrange = getColor("material_darkorange")
        darkGrass = getColor("material_darkgreen")
        lightGrass = getColor("material_darklime")

        # Init sky color
        self.skyColor = []

        for y in range(16):
            row = []
            a = y / 16.0

            for i in range(100):
                r = i/100.0

                color = interpolateBetween([[skyOrange, 0.1],
                                            [skyPurple, 0.4],
                                            [skyBlue, 0.8]], a)
                if r > 0.6:
                    c = (r-0.4)/0.6 *0.8 * a
                    color = interpolateColor(color, [255, 255, 255], c)

                row.append([int(x*0.7) for x in color])

            self.skyColor.append(row)

        # Init grass color
        self.grassColor = []
        for y in range(3):
            row = []
            a = (4-y) / 4.0

            for i in range(100):
                r = i/100.0
                color = interpolateColor(darkGrass, lightGrass, r)
                row.append([int(x*0.5*a) for x in color])

            self.grassColor.append(row)


    def getSkyColor(self, y, r):
        return self.skyColor[y][int(r*100)]


    def getGrassColor(self, y, r):
        return self.grassColor[y][int(r*100)]


    def update(self, dt):
        if not self.running:
            return

        #self.bgDX += 0.01
        self.skyX += self.skyDX *dt
        self.grassX += self.grassDX *dt

        for obstacle in self.obstacles:
            obstacle.addPos(-self.obstacleDx*dt)

            if obstacle.x < -1:
                self.addObstacle(obstacle.x + self.obstacleDist * 3)
                self.obstacles.remove(obstacle)

        self.player.update(dt)

        if self.checkCollision():
            self.running = False
            self.dead = True

    def checkCollision(self):
        pParts = [part for part in self.player.getBody()]

        for obstacle in self.obstacles:
            if int(obstacle.x) != int(self.player.x):
                continue

            for oPart in obstacle.getBody():
                col = [pPart == oPart for pPart in pParts]

                if sum(col) > 0:
                    return True

        return False


    def addObstacle(self, x):
        r = random.randint(0, 16 - Obstacle.HOLE_WIDTH)
        self.obstacles.append(Obstacle(x, r))


    def onButtonDown(self, player, button):
        if player == 0:

            if button == "A":
                if not self.dead and not self.running:
                    self.running = True

                self.player.jump()

            if button == "START":
                if self.dead:
                    self.initialize()


    def render(self, screen):
        screen.fill([0,0,0])

        self.drawBackground(screen)
        self.drawPlayer(screen)
        self.drawObstacles(screen)

        screen.show()


    def drawBackground(self, screen):
        skydx = int(self.skyX)
        grassDx = int(self.grassX)

        for i in range(16):
            skyX = skydx + i
            grassX = grassDx + i

            for y in range(16):

                if y < 3:
                    r = self.noise.noise(grassX * 0.3, y * 0.3, mul=2)
                    color = self.getGrassColor(y, r)
                else:
                    r = self.noise.noise(skyX * 0.1, y * 0.15, mul=2)
                    color = self.getSkyColor(y, r)

                self.drawPixel(screen, i, y, color)


    def drawPlayer(self, screen):
        for x, y in self.player.getBody():
            self.drawPixel(screen, x, y, self.player.color)


    def drawObstacles(self, screen):
        for obstacle in self.obstacles:
            for x, y in obstacle.getBody():
                self.drawPixel(screen, int(x), y, self.obstacleColor)


    def drawPixel(self, screen, x, y, color):
        screen.setPixel(x, 15 - y, color)
