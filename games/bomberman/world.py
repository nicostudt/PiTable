from .entities.player import Player
from .entities.wall import Wall
from .entities.block import Block
from .entities.bomb import Bomb
from .entities.fire import Fire
from .entities.item import Item

from .vec import Vec
import random


class World():

    def __init__(self):
        self.width = 16
        self.height = 16
        self.grid = [[None for _ in range(self.width)]
                     for _ in range(self.height)]

        self.bombs = []
        self.items = []
        self.walls = []
        self.players = []
        self.blocks = []
        self.fires = []

        self.addPlayer(0, Vec(0, 0), [0, 255, 0])
        self.addPlayer(1, Vec(15, 15), [0, 0, 255])

        # Create walls
        for j in range(8):
            for i in range(8):
                x = i * 2 + (0 if i > 3 else 1)
                y = j * 2 + (0 if j > 3 else 1)
                self.addWall(Vec(x, y))

        # Create blocks
        for pos in self.getAllPos():

            # Keep positions near players free
            notNear = True
            for player in self.players:
                if pos.x == player.pos.x and \
                        abs(pos.y - player.pos.y) < 3 or \
                        pos.y == player.pos.y and \
                        abs(pos.x - player.pos.x) < 3:
                    notNear = False
                    break

            if notNear and self.isFree(pos) and random.random() < 0.8:
                self.addBlock(pos)

    def update(self, dt):
        for player in self.players:
            player.update(dt)

            # check if item collisions
            for item in self.items:
                if item.pos == player.pos:
                    player.addItem(item)
                    self.items.remove(item)
                    
        for bomb in self.bombs:
            bomb.update(dt)

            if bomb.timeover():
                self.bombExplode(bomb)

        for fire in self.fires:
            fire.update(dt)

            if fire.timeover():
                self.fires.remove(fire)

    def allPlayersReady(self):
        for player in self.players:
            if not player.isReady():
                return False

        return True

    def gameIsOver(self):
        return len(self.players) < 2

    def getWinner(self):
        if len(self.players) == 1:
            return self.players[0]
        else:
            return None

    def bombExplode(self, bomb):
        self.bombs.remove(bomb)

        player = self.getPlayer(bomb.playerId)

        if player is not None:
            player.addBomb()

        # add fire
        r = bomb.radius

        # Define ranges for directions
        pos = bomb.pos
        ranges = [[Vec(pos.x, pos.y)],
                  [Vec(pos.x - i, pos.y) for i in range(1, r + 1)],
                  [Vec(pos.x + i, pos.y) for i in range(1, r + 1)],
                  [Vec(pos.x, pos.y - i) for i in range(1, r + 1)],
                  [Vec(pos.x, pos.y + i) for i in range(1, r + 1)]]

        for innerRange in ranges:
            for pos in innerRange:
                if not self.addFire(pos):
                    break

    def addBombOfPlayer(self, playerId):
        player = self.getPlayer(playerId)

        if player is not None and player.hasBomb():
            self.addBomb(player)

    def isFree(self, pos):
        if pos.x < 0 or pos.x > 15 or pos.y < 0 or pos.y > 15:
            return False

        if self.getEntityOnGrid(pos):
            return False

        for player in self.players:
            if player.pos == pos:
                return False

        for bomb in self.bombs:
            if bomb.pos == pos:
                return False

        return True

    def getAllEntities(self):
        for player in self.players:
            yield player

        for bomb in self.bombs:
            yield bomb

        for item in self.items:
            yield item

        for wall in self.walls:
            yield wall

        for block in self.blocks:
            yield block

        for fire in self.fires:
            yield fire

        for item in self.items:
            yield item

    def getUpdatable(self):
        for player in self.players:
            yield player

        for bomb in self.bombs:
            yield bomb

    def getAllPos(self):
        for y in range(self.height):
            for x in range(self.width):
                yield Vec(x, y)

    def getEntityOnGrid(self, pos):
        return self.grid[pos.y][pos.x]

    def addOnGrid(self, pos, entity):
        self.grid[pos.y][pos.x] = entity

    def addFire(self, pos):
        fire = Fire(pos)

        # Check collisions
        if pos.x < 0 or pos.x > 15 or pos.y < 0 or pos.y > 15:
            return False

        # check if fire consists
        for f in self.fires:
            if f.pos == pos:
                return False

        ent = self.getEntityOnGrid(pos)

        if isinstance(ent, Wall):
            return False
        elif isinstance(ent, Block):
            self.removeBlock(ent)
            self.fires.append(fire)
            return False

        for bomb in self.bombs:
            if bomb.pos == pos:
                self.bombExplode(bomb)
                return False

        for player in self.players:
            if player.pos == pos:
                self.removePlayer(player)

        self.fires.append(fire)
        return True

    def removePlayer(self, player):
        self.players.remove(player)

        # TODO: DEATH

    def removeBlock(self, block):
        self.blocks.remove(block)
        self.addOnGrid(block.pos, None)

        item = self.getRandomItem(block.pos)

        if item is not None:
            self.items.append(item)

    def getRandomItem(self, pos):
        if random.random() > 0.25:
            return None

        r = random.randint(0, 2)

        if r == 0:
            item = Item.getPlusBomb(pos)
        elif r == 1:
            item = Item.getPlusRange(pos)
        else:
            item = Item.getPlusSpeed(pos)

        return item

    def addBomb(self, player):
        bomb = Bomb(player.id, player.color, player.getBombRange(), player.pos)
        self.bombs.append(bomb)

        player.subBomb()

    def getPlayer(self, id):
        for player in self.players:
            if player.id == id:
                return player

        return None

    def addPlayer(self, id, pos, color):
        player = Player(self, id, pos, color)
        self.players.append(player)

    def addWall(self, pos):
        wall = Wall(pos)
        self.walls.append(wall)
        self.addOnGrid(pos, wall)

    def addBlock(self, pos):
        block = Block(pos)
        self.blocks.append(block)
        self.addOnGrid(pos, block)
