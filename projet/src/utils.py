from enum import Enum

HEIGHT = 1000
WIDTH = 1000
ORIGIN = 20

H_WALL = 1
V_WALL = 2
C_WALL = 3


class CharacterType(Enum):
    ARIANE = 0
    THESEE = 1
    DOOR = 2
    MINO = 3
    # MINO_V = 4


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

