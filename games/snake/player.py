from games.snake.block import Block
from games.snake.colors import *


class Player():

    opposite = {
        "left": "right",
        "right": "left",
        "up": "down",
        "down": "up",
    }


    def __init__(self, game):
        self.game = game

        self.body = []
        for i in range(3):
            self.body.append(Block(8 - i, 8, BLUE))

        self.isDead = False
        self.score = 0
        self.aidsFeature = "none"
        self.direction = "right"


    def update(self):
        # Move player according to direction
        if self.direction == "right":
            self.move(1, 0)

        elif self.direction == "left":
            self.move(-1, 0)

        elif self.direction == "down":
            self.move(0, 1)

        elif self.direction == "up":
            self.move(0, -1)


    def move(self, moveX, moveY):
        # Add new head in front of snake
        head = self.body[0]
        newHead = Block(head.xPos + moveX, head.yPos + moveY, head.color)
        self.body.insert(0, newHead)

        # Remove tail
        del self.body[-1]

        head = self.body[0]
        if head.check_wall():
            if self.aidsFeature == "wall_block":
                self.isDead = True
            else:
                head.loop()

        # Check food collision
        if head.collision(self.game.food):
            self.eat_food(self.game.food)
            self.game.spawn_random_food()

        self.head_collision()


    def head_collision(self):
        # Die if self collision
        head = self.body[0]

        for piece in self.body[1:]:
            if piece.collision(head):
                self.isDead = True


    def eat_food(self, food):
        self.score += 1

        tail = self.body[-1]
        self.body.append(tail)

        if food.color == RED:
            self.aidsFeature = "double_speed"

        elif food.color == PURPLE:
            self.aidsFeature = "wall_block"

        elif food.color == YELLOW:
            self.aidsFeature = "reverse_steering"

        elif food.color == ORANGE:
            self.aidsFeature = "fuckup_background"

        elif food.color == GREEN:
            self.aidsFeature = "none"


    def set_direction(self, newDirection):
        if self.aidsFeature == "reverse_steering":
            newDirection = self.opposite[newDirection]

        if self.direction != self.opposite[newDirection]:
            self.direction = newDirection

