from engine.game import Game
from .board import Board


class GameOfLife(Game):

    def __init__(self):
        Game.__init__(self, "GameOfLife", [16, 16])
        self.fps = 5

    def initialize(self):
        self.board = Board(16, 16)
        self.board.setRules({
            False: [False, False, False, True, False,
                    False, False, False, False],
            True: [True, True, False, False, True,
                   True, True, True, True]
        })
        self.board.generateRandom()

    def onButtonDown(self, player, button):
        self.board.generateRandom()

    def update(self, dt):
        self.board.update()

    def render(self, screen):
        screen.fill([0, 0, 0])

        self.board.render(screen)

        screen.show()
