import os
import random
import pygame

TILE = 50
COLS = 10
ROWS = 10
HUD_H = 80
WIDTH = COLS * TILE
HEIGHT = ROWS * TILE + HUD_H
FPS = 60

ASSET_DIR = r"C:\Users\super\Projects\WumpusWorld\Images"

STEMS = {
    "floor": ["Floor","floor"],
    "fog": ["black","fog"],
    "arrow": ["arrow","Picture1"],
    "gold": ["gold","Gold"],
    "ladder": ["ladder","Ladder"],
    "pit": ["pit","Pit"],
    "breeze": ["breeze","Breeze"],
    "wumpus": ["wumpus","Wumpus"],
    "deadWumpus": ["deadwumpus","DeadWumpus"],
    "stench": ["stench","Stench"],
    "playerUp": STEMS.get(key,[key]):
        for ext in (".gif",".png"):
            p = os.path.join(ASSET_DIR, stem + ext)
            if os.path.exists(p):
                img = pygame.image.load(p).convert_alpha()
                return pygame.transform.scale(img, (TILE, TILE))
    return None

class WumpusSquare:
    def __init__(self):
        self.gold = False
        self.ladder = False
        self.pit = False
        self.breeze = False
        self.wumpus = False
        self.deadWumpus = False
        self.stench = False
        self.visited = False["playerUp","PlayerUp"],
    "playerDown": ["playerDown","PlayerDown"],
    "playerLeft": ["playerLeft","PlayerLeft"],
    "playerRight": ["playerRight","PlayerRight"],
}

def load_image(key):
    for stem in 

class WumpusMap:
    NUM_ROWS = ROWS
    NUM_COLUMNS = COLS
    NUM_PITS = 10
    def __init__(self):
        self.grid = None
        self.ladderC = 0
        self.ladderR = 0
        self.create_map()
    def create_map(self):
        self.grid = [[WumpusSquare() for _ in range(ROWS)] for _ in range(COLS)]
        r = random.Random()
        while True:
            c = r.randint(0, COLS - 1)
            rr = r.randint(0, ROWS - 1)
            if not self.grid[c][rr].pit:
                self.grid[c][rr].ladder = True
                self.ladderC = c
                self.ladderR = rr
                break
        pits = 0
        while pits < self.NUM_PITS:
            c = r.randint(0, COLS - 1)
            rr = r.randint(0, ROWS - 1)
            sq = self.grid[c][rr]
            if not sq.pit and not sq.ladder:
                sq.pit = True
                if c - 1 >= 0:
                    self.grid[c - 1][rr].breeze = True
                if c + 1 < COLS:
                    self.grid[c + 1][rr].breeze = True
                if rr - 1 >= 0:
                    self.grid[c][rr - 1].breeze = True
                if rr + 1 < ROWS:
                    self.grid[c][rr + 1].breeze = True
                pits += 1
        while True:
            c = r.randint(0, COLS - 1)
            rr = r.randint(0, ROWS - 1)
            sq = self.grid[c][rr]
            if not sq.pit and not sq.ladder:
                sq.gold = True
                break
        while True:
            c = r.randint(0, COLS - 1)
            rr = r.randint(0, ROWS - 1)
            sq = self.grid[c][rr]
            if not sq.pit and not sq.ladder:
                sq.wumpus = True
                if c - 1 >= 0:
                    self.grid[c - 1][rr].stench = True
                if c + 1 < COLS:
                    self.grid[c + 1][rr].stench = True
                if rr - 1 >= 0:
                    self.grid[c][rr - 1].stench = True
                if rr + 1 < ROWS:
                    self.grid[c][rr + 1].stench = True
                break
    def get_ladder_col(self):
        return self.ladderC
    def get_ladder_row(self):
        return self.ladderR
    def get_square(self, col, row):
        if 0 <= col < COLS and 0 <= row < ROWS:
            return self.grid[col][row]
        return None

class WumpusPlayer:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    def __init__(self, c, r):
        self.direction = WumpusPlayer.NORTH
        self.arrow = True
        self.gold = False
        self.col = c
        self.row = r
    def direction_name(self):
        if self.direction == WumpusPlayer.NORTH:
            return "up"
        elif self.direction == WumpusPlayer.SOUTH:
            return "down"
        elif self.direction == WumpusPlayer.WEST:
            return "left"
        else:
            return "right"

class WumpusGame:
    PLAYING = 0
    DEAD = 1
    WON = 2
    def __init__(self, screen):
        self.screen = screen
        self.buffer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 22)
        self.big = pygame.font.SysFont(None, 36)
        self.messages = []
        self.cheat = False
        self.status = self.PLAYING
        self.key_processed = False
        self.map = None
        self.player = None
        self.images = {}
        self.images["floor"] = load_image("floor")
        self.images["fog"] = load_image("fog")
        self.images["arrow"] = load_image("arrow")
        self.images["gold"] = load_image("gold")
        self.images["ladder"] = load_image("ladder")
        self.images["pit"] = load_image("pit")
        self.images["breeze"] = load_image("breeze")
        self.images["wumpus"] = load_image("wumpus")
        self.images["deadWumpus"] = load_image("deadWumpus")
        self.images["stench"] = load_image("stench")
        self.images["playerUp"] = load_image("playerUp")
        self.images["playerDown"] = load_image("playerDown")
        self.images["playerLeft"] = load_image("playerLeft")
        self.images["playerRight"] = load_image("playerRight")
        self.reset()
    def reset(self):
        self.status = self.PLAYING
        self.messages = []
        self.map = WumpusMap()
        for r in range(ROWS):
            for c in range(COLS):
                if self.map.grid[c][r].pit:
                    self.map.grid[c][r].breeze = False
        self.player = WumpusPlayer(self.map.get_ladder_col(), self.map.get_ladder_row())
        s = self.map.get_square(self.player.col, self.player.row)
        s.visited = True
        if s.breeze:
            self.messages.append("You feel a breeze.")
        if s.stench or s.deadWumpus:
            self.messages.append("You smell a stench.")
        if s.gold:
            self.messages.append("You see a glimmer.")
        if s.ladder:
            self.messages.append("You bumped into a ladder.")