#!/usr/bin/python

from engine.game import Game
from games.snake.block import Block
import random

class Snake(Game):

    def __init__(self):
        Game.__init__(self, "Snake", [16, 16])
        self.fps = 30
        self.death = False

        # Spieler erstellen
        self.player = []

        for i in range(3):
            self.player.append(Block(i, 0, [150, 0, 0]))

        # fruit erstellen
        self.food = Block(0, 0, [255, 255, 0])

    def initialize(self):
        pass


    def onButtonDown(self, player, button):
        pass


    def move_head(self, moveX, moveY):
        newX = self.player[0].xPos + moveX
        newY = self.player[0].yPos + moveY
        newColor = self.player[0].color
        newBlock = Block(newX, newY, newColor)

        self.player.insert(0, newBlock)
        del self.player[-1]

        self.head_collide()

    def head_collide(self):
        head = self.player[0]

        for bodyPiece in self.player[3:]:
            if bodyPiece.collide_with(head):
                self.death = True


    def onAxisMotion(self, player, axis, value):
        print(player, axis, value)

        if axis == "x":
            if value == 1:
                self.move_head(1, 0)
            elif value == -1:
                self.move_head(-1, 0)

        if axis == "y":
            if value == 1:
                self.move_head(0, 1)
            elif value == -1:
                self.move_head(0, -1)

    def update(self, dt):
        head = self.player[0]

        if head.collide_with(self.food):
            self.spawn_random_food()
            self.ate_food()


    def spawn_random_food(self):
        self.food.xPos = random.randint(0, 15)
        self.food.yPos = random.randint(0, 15)
        self.food.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


    def ate_food(self):
        head = self.player[0]
        newBlock = head.copy()
        self.player.insert(0, newBlock)


    def loop_motion(self):
        if self.player.xPos >= 16:
            self.player.xPos = 0

        if self.player.yPos >= 16:
            self.player.yPos = 0

        if self.player.xPos < 0:
            self.player.xPos = 15

        if self.player.yPos < 0:
            self.player.yPos = 15


    def render(self, display):
        if self.death:
            display.fill([255, 0, 0])

        else:
            # Zeichne ganz normal
            display.fill([0, 0, 0])

            self.food.render_to(display)

            for block in self.player:
                block.render_to(display)

        display.show()
