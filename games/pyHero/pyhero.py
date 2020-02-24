from engine.game import Game
from .note import Note
from .colours import *
from .lane import Lane
import random
from .font import *

class PyHero(Game):
    STARTSTATE = "START"
    GAMESTATE = "GAME"
    def __init__(self):
        Game.__init__(self, "PyHero", [16, 16])
        self.fps = 30

    def initialize(self):

        self.state = PyHero.STARTSTATE
        self.aPressed = False
        self.lanes = []
        self.lanes.append(Lane(self,5,GREEN,"Y"))
        self.lanes.append(Lane(self,8,YELLOW,"B"))
        self.lanes.append(Lane(self,11,BLUE,"X"))
        self.lanes.append(Lane(self,14,RED,"A"))

        self.counter = 0
        self.difficulty = 14
        self.score = 0

    def decreaseScore(self,value):
        if self.score >= value:
            self.score -= value
        else:
            self.score = 0
    def printLetter(self, dx, dy, letter, display):
        letterMatrix = getLetter(letter)

        for y, row in enumerate(letterMatrix):
            if y + dx >= self.size[1]:
                break

            for x, value in enumerate(row):
                if 0 > x + dx <= self.size[0] or value == 0:
                    continue

                display.setPixel(x + dx, y + dy, [150, 150, 150])

    def scoreRender(self,screen):
        numbers = [0, 0, 0]
        self.score = self.score %1000

        nums = [int(i) for i in str(self.score)]

        for i in range(len(nums)):
            numbers[-i-1] = nums[-i-1]

        for i, number in enumerate(numbers):
            self.printLetter(0, i*5, number, screen)

    def startRender(self,screen):
        #TODO PYHERO SCHREIBEN

        pass

    def gameRender(self,screen):
        for lane in self.lanes:
            lane.render(screen)

    def onButtonDown(self,playerId,button):

        if self.state == PyHero.STARTSTATE:
            if button == "START":
                self.state = PyHero.GAMESTATE
        if self.state == PyHero.GAMESTATE:
            for lane in self.lanes:
                if button == lane.button:
                    lane.pressed = True
                    hit = lane.hit()
                    if hit == 1:
                        self.score += 10
                    elif hit == 2:
                        self.score += 5

                    elif self.score >= 5:
                        self.decreaseScore(5)


    def onButtonUp(self,playerId,button):
        if self.state == PyHero.GAMESTATE:
            for lane in self.lanes:
                if button == lane.button:
                    lane.pressed = False

    def update(self, dt):
        if self.state == PyHero.GAMESTATE:
            self.counter += 1
            if self.counter % self.difficulty == 0:
                self.addNotes()

        for lane in self.lanes:

            lane.update(dt)


        noteCounter = sum([len(lane.notes) for lane in self.lanes])



    def addNotes(self):
        onLane = random.randint(0,3)
        self.lanes[onLane].notes.append(Note(1))


    def render(self, screen):

        screen.fill([0, 0, 0])
        self.scoreRender(screen)
        if self.state == PyHero.STARTSTATE:
            self.startRender(screen)
        elif self.state == PyHero.GAMESTATE:
            self.gameRender(screen)
        screen.show()
