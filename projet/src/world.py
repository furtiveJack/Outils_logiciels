import upemtk as upemtk
from character import *
from utils import *


def create_window():
    upemtk.cree_fenetre(HEIGHT, WIDTH)
    upemtk.rectangle(0, 0, WIDTH, HEIGHT, "white", "white")


def create_world_from_file(path: str):
    file = open(path, "r")
    size = int(file.readline())
    grid = [[0 for _ in range(2 * size + 1)] for _ in range(2 * size + 1)]
    i = 0
    j = 0
    ariane = (-1, -1)
    thesee = (-1, -1)
    door = (-1, -1)
    mino_h = []
    mino_v = []

    for line in file:
        for char in line:
            if char == "\n":
                i = 0
                continue
            elif char == "-":
                grid[i][j] = H_WALL
            elif char == "|":
                grid[i][j] = V_WALL
            elif char == "+":
                grid[i][j] = C_WALL
            elif char == 'A':
                ariane = (i, j)
            elif char == 'T':
                thesee = (i, j)
            elif char == 'H':
                mino_h.append((i, j))
            elif char == 'V':
                mino_v.append((i, j))
            elif char == 'P':
                door = (i, j)
            i += 1
        j += 1
    return World(grid, ariane, thesee, mino_h, mino_v, door)


class World:
    def __init__(self, level: list, ariane: tuple, thesee: tuple, mino_h: list, mino_v: list, door: tuple):
        self.level = level
        self.n = len(level[0])
        self.ariane = Character(ariane[0], ariane[1], "../media/ariane.png", CharacterType.ARIANE)
        self.thesee = Character(thesee[0], thesee[1], "../media/thesee.png", CharacterType.THESEE)
        self.mino_h = [Character(mino[0], mino[1], "../media/minoH.png", CharacterType.MINO) for mino in mino_h]
        self.mino_v = [Character(mino[0], mino[1], "../media/minoV.png", CharacterType.MINO) for mino in mino_v]
        self.door = Character(door[0], door[1], "../media/porte.png", CharacterType.DOOR)

    def terminal_display(self):
        for line in self.level:
            print(line)
        self.ariane.to_string()
        self.thesee.to_string()
        self.door.to_string()
        for mino in self.mino_h:
            mino.to_string()
        for mino in self.mino_v:
            mino.to_string()

    def draw_walls(self, scale):
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.level[i][j] == V_WALL:
                    image(ORIGIN + i * scale, ORIGIN + j * scale, "../media/wallV.png")
                if self.level[i][j] == H_WALL:
                    image(ORIGIN + i * scale, ORIGIN + j * scale, "../media/wallH.png")
                if self.level[i][j] == C_WALL:
                    image(ORIGIN + i * scale, ORIGIN + j * scale, "../media/wallC.png")

    def window_display(self):
        scale = HEIGHT // self.n
        print(scale, ' ', self.n)
        self.draw_walls(scale)
        self.ariane.draw(scale)
        self.thesee.draw(scale)
        self.door.draw(scale)
        for mino in self.mino_h:
            mino.draw(scale)
        for mino in self.mino_v:
            mino.draw(scale)
        mise_a_jour()
        attente_clic()
