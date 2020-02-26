from player import Player
from obstacle import Obstacle
import utils.colors as colors
import utils.simplexnoise.noise as snoise

class World():

    def __init__(self, dy, playerColor):
        self.noise = snoise.SimplexNoise(2, 1, 3)
        self.dy = dy
        self.grassColor = colors.getColor("material_green")
        self.running = False
        self.player = Player(playerColor)
        self.obstacles = []

    def restart(self):
        self.obstacleSpawnTime = 1
        self.obstacleTimer = self.obstacleSpawnTime
        self.running = True
        self.player.reset()

    def update(self, dt):
        if self.running:
            self.player.update(dt)
            self.updateObstacles(dt)

            if self.checkCollision():
                self.running = False

    def start(self):
        if not self.running:
            self.restart()

    def updateObstacles(self, dt):
        self.obstacleTimer -= dt

        if self.obstacleTimer <= 0:
            self.spawnObstacle()
            self.obstacleTimer += self.obstacleSpawnTime


        for obstacle in self.obstacles:
            if obstacle.x - self.player.x < -3:
                self.obstacles.remove(obstacle)

    def checkCollision(self):
        pParts = [part for part in self.player.getBody()]

        for obstacle in self.obstacles:
            for oPart in obstacle.getBody():
                col = [pPart == oPart for pPart in pParts]

                if sum(col) > 0:
                    return True

        return False

    def spawnObstacle(self):
        x = int(self.player.x)

        newObs = Obstacle(x + 16, [[0, 0]])

        self.obstacles.append(newObs)

    def draw(self, screen):
        # Draw ground
        playerX = int(self.player.x)

        for i in range(playerX -2, playerX +14):
            alpha = self.noise.noise(i*0.3, mul = 4.1) / 1.5
            color = colors.interpolateColor(self.grassColor,
                                            [0,0,0], alpha)
            self.drawPixel(screen, i, -1, color)

        # Draw Player
        for x, y in self.player.getBody():
            self.drawPixel(screen, x, y, self.player.color)

        for obstacle in self.obstacles:
            for x, y in obstacle.getBody():
                self.drawPixel(screen, x, y, [255, 255, 255])

    def drawPixel(self, screen, x, y, color):
        drawx = x -int(self.player.x) + 2
        drawY = 15 - (self.dy + y)
        screen.setPixel(drawx, drawY, color)
