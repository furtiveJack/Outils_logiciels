from upemtk import *
from character import *
from utils import *


def create_window():
    cree_fenetre(HEIGHT, WIDTH)


def create_world_from_file(path):
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
                j = 0
                continue
            elif char == "+" or char == "-" or char == "|":
                grid[j][i] = 1
            elif char == 'A':
                ariane = (j, i)
            elif char == 'T':
                thesee = (j, i)
            elif char == 'H':
                mino_h.append((j, i))
            elif char == 'V':
                mino_v.append((j, i))
            elif char == 'P':
                door = (j, i)
            else:
                grid[j][i] = 0
            j += 1
        i += 1
    return World(grid, ariane, thesee, mino_h, mino_v, door)


def draw_vertical_wall(i, j, scale):
    print(i, ' ', j, scale)
    ligne(ORIGIN + i * scale, ORIGIN + j * scale, ORIGIN + (i+1 * scale), ORIGIN + j*scale, couleur="black")


class World:
    """
    :param level : list[n][n]
    :param ariane: tuple : pos
    :param thesee: tuple : pos
    :param door : tuple : pos
    :param mino_h : list of tuple (pos)
    :param mino_v : list of tuple (pos)
    """

    def __init__(self, level, ariane, thesee, mino_h, mino_v, door):
        self.level = level
        self.ariane = Character(ariane[0], ariane[1], "../media/ariane.png", CharacterType.ARIANE)
        self.thesee = Character(thesee[0], thesee[1], "../media/thesee.png", CharacterType.THESEE)
        self.mino_h = [Character(mino[0], mino[1], "../media/minoH.png", CharacterType.MINO_H) for mino in mino_h]
        self.mino_v = [Character(mino[0], mino[1], "../media/minoV.png", CharacterType.MINO_V) for mino in mino_v]
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

    # def draw_walls(self):
    #     for i in range(0, n):
    #         for j in range(0, n):
    # draw_wall()

    def draw_walls(self, n, scale):
        for i in range(0, n):
            for j in range(0, n):
                if i % 2 == 0 and j % 2 != 0:
                    draw_vertical_wall(j, i, scale)
                # elif j % 2 == 0 and i % 2 != 0:
                #     self.draw_horizontal_wall(i, j, scale)
                # else:
                #     self.draw_intersect_wall(i, j, scale)

    def window_display(self):
        n = len(self.level[0])
        scale = HEIGHT / n
        self.draw_walls(n, scale)
        self.ariane.draw(scale)
        self.thesee.draw(scale)
        self.door.draw(scale)
        for mino in self.mino_h:
            mino.draw(scale)
        for mino in self.mino_v:
            mino.draw(scale)
        mise_a_jour()
        attente_clic()
