import random
import os.path
import utils.font5x3 as font
from engine.game import Game
from utils.colors import *
from games.flappy_bird.player import Player
from games.flappy_bird.obstacle import Obstacle
from games.flappy_bird.sky import Sky
from games.flappy_bird.grass import Grass


class BirdGame(Game):

    OBSTACLE_DX = 8
    OBSTACLE_DIST = 8
    SKY_DX = 2
    GRASS_DX = 4


    def __init__(self):
        Game.__init__(self, "Bird", [16, 16])

        self.fps = 30
        self.x = 0
        self.sky = Sky(BirdGame.SKY_DX)
        self.grass = Grass(BirdGame.GRASS_DX)
        self.state = "START"

        my_path = os.path.abspath(os.path.dirname(__file__))
        self.scorePath = os.path.join(my_path, "highscore.txt")

        self.initColors()


    def initialize(self):
        self.loadHighScore()
        self.points = 0
        self.player = Player("material_red")
        self.obstacles = []

        for i in range(3):
            self.addObstacle(25 + i * BirdGame.OBSTACLE_DIST)


    def initColors(self):
        self.obstacleColor = getColor("material_green")
        self.textColor = getColor("material_white")
        self.goldTextColor = getColor("material_gold")

        self.sky.move(16)
        self.grass.move(16)


    def loadHighScore(self):
        with open(self.scorePath) as f:
            self.hightscore = int(next(f))


    def safeHighscore(self):
        score = max(self.hightscore, self.points)

        with open(self.scorePath, mode="w") as f:
            f.write(str(score))
            

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

        self.sky.update(dt)
        self.grass.update(dt)

        for obstacle in self.obstacles:
            obstacle.addPos(-BirdGame.OBSTACLE_DX * dt)

            if obstacle.x < -1:
                self.addObstacle(obstacle.x + BirdGame.OBSTACLE_DIST * 3)
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
            self.player.jump()

        elif state == "DEAD":
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
        self.sky.draw(screen)
        self.grass.draw(screen)


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
        dx = 8 - len(matrix[0])//2

        for j, row in enumerate(matrix):
            y = j + dy
            color = self.textColor
            if 8 < y < 14:
                color = self.goldTextColor

            for x, value in enumerate(row):
                if value == 0:
                    continue

                screen.setPixel(x + dx, y, color)
