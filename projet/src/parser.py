from src.world import World
from src.utils import *


def create_world_from_file(path: str) -> World:
    """
    Parse the file provided and generate a world that represents the content of this file.
    :param path: path of the file to parse.
    :return: a world representing the content of the file (walls, characters).
    """
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
            j += 1
        i += 1
    map_name = path.split("/")[1]
    return World(grid, ariane, thesee, mino_h, mino_v, door, map_name)
