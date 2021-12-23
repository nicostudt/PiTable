#!/usr/bin/python

import utils.font5x3 as font
import random
from engine.game import Game
from games.snake.block import Block
from games.snake.colors import *
from games.snake.player import Player


class SnakeGame(Game):

    def __init__(self):
        Game.__init__(self, "Snake", [16, 16])
        self.fps = 45

        self.restart()

    def restart(self):
        self.food = Block(3, 6, GREEN)
        self.player = Player(self)
        self.frameCounter = 0
        self.difficulty = 7


    def onButtonDown(self, player, button):
        if button == "START" and self.player.isDead:
            self.restart()


    def onAxisMotion(self, player, axis, value):
        if axis == "x":
            if value == 1:
                self.player.set_direction("right")

            if value == -1:
                self.player.set_direction("left")

        if axis == "y":
            if value == 1:
                self.player.set_direction("down")

            if value == -1:
                self.player.set_direction("up")


    def update(self, dt):
        # Aids feature double speed
        maxCounter = self.difficulty
        if self.player.aidsFeature == "double_speed":
            maxCounter /= 2

        # Skip frames
        self.frameCounter += 1
        if self.frameCounter < maxCounter:
            return
        else:
            self.frameCounter = 0

        self.player.update()


    def spawn_random_food(self):
        self.food.xPos = random.randint(0, 15)
        self.food.yPos = random.randint(0, 15)
        self.food.color = random.choice([RED, GREEN, PURPLE, YELLOW, ORANGE])

    def render(self, display):
        if self.player.isDead:
            self.render_dead(display)
        else:
            self.render_game(display)

        display.show()


    def render_dead(self, display):
        display.fill(DEAD_BACKGROUND)
        self.displayFont(display, 5, str(self.player.score))


    def render_game(self, display):
        if self.player.aidsFeature == "fuckup_background":
            backgroundColor = [random.randint(0, 88) for _ in range(3)]
        else:
            backgroundColor = STANNI_BACKGROUND

        display.fill(backgroundColor)

        # Draw food
        display.setPixel(self.food.xPos, self.food.yPos, self.food.color)

        # Draw player
        for piece in self.player.body:
            display.setPixel(piece.xPos, piece.yPos, piece.color)


    def displayFont(self, display, dy, text):
        matrix = font.getTextMatrix(text)
        dx = 8 - len(matrix[0]) // 2

        for j, row in enumerate(matrix):
            y = j + dy
            color = TEXT_COLOR

            for x, value in enumerate(row):
                if value == 0:
                    continue

                display.setPixel(x + dx, y, color)