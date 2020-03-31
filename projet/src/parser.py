from world import World
from utils import *


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
                grid[i][j] = MINO
            elif char == 'V':
                mino_v.append((i, j))
                grid[i][j] = MINO
            elif char == 'P':
                door = (i, j)
            i += 1
        j += 1
    return World(grid, ariane, thesee, mino_h, mino_v, door)
