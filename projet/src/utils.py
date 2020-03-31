from enum import Enum
from typing import Optional

HEIGHT = 1000
WIDTH = 1000
ORIGIN = 20

NONE = 0
H_WALL = 1
V_WALL = 2
C_WALL = 3
MINO = 4


class CharacterType(Enum):
    ARIANE = 0
    THESEE = 1
    DOOR = 2
    MINO_H = 3
    MINO_V = 4


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def get_dir_from_string(direction: str) -> Optional[Direction]:
    if direction == "Left":
        return Direction.LEFT
    if direction == "Right":
        return Direction.RIGHT
    if direction == "Up":
        return Direction.UP
    if direction == "Down":
        return Direction.DOWN
    return None

