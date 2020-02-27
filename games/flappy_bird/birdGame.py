from engine.game import Game
from player import Player
from obstacle import Obstacle
from utils.colors import *
import utils.simplexnoise.noise as snoise
import utils.font5x3 as font
import random
import os.path


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
        self.state = "START"

        my_path = os.path.abspath(os.path.dirname(__file__))
        self.scorePath = os.path.join(my_path, "highscore.txt")

        self.initColors()

    def initialize(self):
        self.loadHighScore()
        self.points = 0
        self.running = False
        self.dead = False
        self.player = Player("material_red")
        self.obstacles = []

        for i in range(3):
            self.addObstacle(25 + i*self.obstacleDist)

    def loadHighScore(self):
        with open(self.scorePath) as f:
            self.hightscore = int(next(f))

    def safeHighscore(self):
        score = max(self.hightscore, self.points)

        with open(self.scorePath, mode="w") as f:
            f.write(str(score))

    def initColors(self):
        self.obstacleColor = getColor("material_green")
        self.textColor = getColor("material_white")
        self.goldTextColor = getColor("material_gold")
        skyBlue = getColor("material_darkblue")
        skyPurple = getColor("material_darkpurple")
        skyOrange = getColor("material_darkorange")
        darkGrass = getColor("material_darkgreen")
        lightGrass = getColor("material_darklime")

        light = 0.65

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
                    c = (r-0.4)/0.6 *1 * a
                    color = interpolateColor(color, [255, 255, 255], c)

                row.append([int(x*light) for x in color])

            self.skyColor.append(row)

        # Init grass color
        self.grassColor = []
        for y in range(3):
            row = []
            a = (4-y) / 4.0

            for i in range(100):
                r = i/100.0
                color = interpolateColor(darkGrass, lightGrass, r)
                row.append([int(x*light*a) for x in color])

            self.grassColor.append(row)


    def getSkyColor(self, y, r):
        return self.skyColor[y][int(r*100)]


    def getGrassColor(self, y, r):
        return self.grassColor[y][int(r*100)]


    def update(self, dt):
        if self.state == "DEAD":
            self.deadTimer += dt

            if self.deadTimer >= 1.5:
                self.setState("HIGHSCORE")
            return

        elif self.state == "HIGHSCORE":
            self.hightscoreTimer += dt
            return

        elif self.state != "GAME":
            return

        #self.bgDX += 0.01
        self.skyX += self.skyDX *dt
        self.grassX += self.grassDX *dt

        for obstacle in self.obstacles:
            obstacle.addPos(-self.obstacleDx*dt)

            if obstacle.x < -1:
                self.addObstacle(obstacle.x + self.obstacleDist * 3)
                self.obstacles.remove(obstacle)
                self.points += 1

        self.player.update(dt)

        if self.checkCollision():
            self.setState("DEAD")

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
        r = random.randint(1, 15 - Obstacle.HOLE_WIDTH)
        self.obstacles.insert(0, Obstacle(x, r))


    def onButtonDown(self, player, button):
        if player != 0:
            return

        if button == "A":
            if self.state == "START":
                self.setState("GAME")

            elif self.state == "GAME":
                self.player.jump()

        if button == "START":
            if self.state == "HIGHSCORE":
                self.setState("START")


    def setState(self, state):
        self.state = state

        if state == "START":
            self.initialize()

        elif state == "GAME":
            self.running = True
            self.player.jump()

        elif state == "DEAD":
            self.running = False
            self.deadTimer = 0
            self.safeHighscore()

        elif state == "HIGHSCORE":
            self.hightscoreTimer = 0

    def render(self, screen):
        screen.fill([0,0,0])

        self.drawBackground(screen)

        if self.state != "HIGHSCORE":
            self.drawObstacles(screen)
            self.drawPlayer(screen)
        else:
            self.drawHighscore(screen)

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


    def drawHighscore(self, screen):
        dy1 = 2
        dy2 = 9

        if self.points > self.hightscore:
            dy = max(0, (self.hightscoreTimer-1) // 0.05)

            dy1 += dy
            dy1 = min(9, dy1)

            if dy > 1:
                dy2 += dy -1
                dy2 = min(16, dy2)

        self.displayFont(screen, dy1, str(self.points))
        self.displayFont(screen, dy2, str(self.hightscore))

    def drawPixel(self, screen, x, y, color):
        screen.setPixel(x, 15 - y, color)


    def displayFont(self, screen, dy, text):
        matrix = font.getTextMatrix(text)
        dx = 8 -len(matrix[0])//2

        for j, row in enumerate(matrix):
            y = j + dy
            color = self.textColor
            if y > 8 and y < 14:
                color = self.goldTextColor

            for x, value in enumerate(row):
                if value == 0: continue

                screen.setPixel(x + dx, y, color)
