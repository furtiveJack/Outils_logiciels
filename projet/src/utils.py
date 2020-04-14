from enum import Enum
from typing import Optional
"""
Utility methods and variables for the game.
"""
# Height of the window (in px)
HEIGHT = 1000
# Width of the window (in px)
WIDTH = 1000
# Shift from the side of the window
ORIGIN = 20

NONE = 0
H_WALL = 1
V_WALL = 2
C_WALL = 3
MINO = 4


class CharacterType(Enum):
    """
    Enumeration class to define the possibles types of character
    """
    ARIANE = 0
    THESEE = 1
    DOOR = 2
    MINO_H = 3
    MINO_V = 4


class Direction(Enum):
    """
    Enumeration class to define the possible move directions
    """
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def get_dir_from_string(direction: str) -> Optional[Direction]:
    """
    Convert a string representing a direction to its value in the enum Direction class.
    Valid directions are UP, DOWN, RIGHT, LEFT.
    Case does not matter.
    :param direction: a string representing a direction
    :return: a direction from the Direction class, or None if the parameter is incorrect.
    """
    direction = direction.lower()
    if direction == "left":
        return Direction.LEFT
    if direction == "right":
        return Direction.RIGHT
    if direction == "up":
        return Direction.UP
    if direction == "down":
        return Direction.DOWN
    return None


def dir_to_string(direction: Direction) -> str:
    """
    Convert a direction from the Direction class to its string representation.
    :param direction: the direction to convert
    :return: a string representing the direction.
    """
    if direction == Direction.LEFT:
        return "Left"
    if direction == Direction.RIGHT:
        return "Right"
    if direction == Direction.DOWN:
        return "Down"
    if direction == Direction.UP:
        return "Up"
