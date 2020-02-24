from engine.game import Game
from .player import Player
from .bullet import Bullet
from .enemy import Enemy
import random


class SpaceInvaders(Game):

    def __init__(self):
        Game.__init__(self, "Space Invaders", [16, 16])
        self.fps = 15
        self.enemyShootTime = 1
        self.enemyMoveTime = 0.7

    def initialize(self):
        self.player = Player([8, 15])
        self.bullets = []
        self.enemies = []
        self.enemyShootTimer = 0
        self.enemyMoveTimer = self.enemyMoveTime

        for i in range(3):
            pos = [2 + i * 4, 1]
            enemy = Enemy(pos)
            self.enemies.append(enemy)

    def onButtonDown(self, player, button):
        if player != 0:
            return

        if button == "A":
            if self.player.shoot():
                bullet = self.player.createBullet()
                self.bullets.append(bullet)

    def onAxisMotion(self, player, axis, value):
        if player != 0:
            return

        if axis == "x":
            self.player.setVel(value)

    def update(self, dt):
        # Move bullets
        for bullet in self.bullets:
            bullet.move()

            if bullet.isOutside():
                self.bullets.remove(bullet)
                continue

        # Check bullet collision
        for object in self.allObjects():
            for bullet in self.bullets:
                if bullet.colide(object.getBody()):
                    object.destroy(bullet.pos)
                    self.bullets.remove(bullet)

            if object.isDead():
                if isinstance(object, Player):
                    pass
                    # player dead
                elif isinstance(object, Enemy):
                    self.enemies.remove(object)

        # Update player
        self.player.update(dt)

        # Move enemies
        self.enemyMoveTimer -= dt
        if self.enemyMoveTimer < 0:
            self.enemyMoveTimer = self.enemyMoveTime

            for enemy in self.enemies:
                enemy.move()
        # Let random enemy shoot
        self.enemyShootTimer -= dt
        if self.enemyShootTimer < 0:
            self.enemyShootTimer = self.enemyShootTime

            enemy = self.enemies[random.randint(0, len(self.enemies) - 1)]
            bullet = enemy.createBullet()
            self.bullets.append(bullet)

    def render(self, screen):
        screen.fill([0, 0, 0])

        # Draw Player
        color = self.player.getColor()
        for bodyPart in self.player.getBody():
            screen.setPixel(bodyPart[0], bodyPart[1], color)

        # Draw bullets
        for bullet in self.bullets:
            pos = bullet.pos
            screen.setPixel(pos[0], pos[1], bullet.color)

        # Draw enemies
        for enemy in self.enemies:
            color = enemy.getColor()
            for bodyPart in enemy.getBody():
                screen.setPixel(bodyPart[0], bodyPart[1], color)
        screen.show()

    def allObjects(self):
        for enemy in self.enemies:
            yield enemy

        yield self.player
