import upemtk as upemtk
from character import *
from utils import *


class World:
    def __init__(self, level: list, ariane: tuple, thesee: tuple, mino_h: list, mino_v: list, door: tuple):
        self.level = level
        self.n = len(level[0])
        self.ariane = Character(ariane[0], ariane[1], "../media/ariane.png", CharacterType.ARIANE)
        self.thesee = Character(thesee[0], thesee[1], "../media/thesee.png", CharacterType.THESEE)
        self.mino_h = [Character(mino[0], mino[1], "../media/minoH.png", CharacterType.MINO_H) for mino in mino_h]
        self.mino_v = [Character(mino[0], mino[1], "../media/minoV.png", CharacterType.MINO_V) for mino in mino_v]
        self.door = Character(door[0], door[1], "../media/porte.png", CharacterType.DOOR)
        self.ariane_found = False
        self.door_found = False

    def move_ariane(self, direction: Direction) -> None:
        return self.ariane.move(direction)

    def move_thesee(self) -> None:
        direction = self.__compute_thesee_dir__()
        if direction is None:
            return
        if self.valid_direction(self.thesee, direction):
            self.thesee.move(direction)
        if self.thesee.get_position() == self.door.get_position():
            if self.ariane.get_position() == self.door.get_position():
                self.door_found = True

    def move_mino(self, mino: Character) -> None:
        direction = self.__compute_mino_dir__(mino)
        while True:
            if not self.valid_direction(mino, direction):
                return
            self.__move_mino__(mino, direction)
            if self.__ariane_found__(mino):
                return

    def game_ended(self) -> bool:
        return self.ariane_found or self.door_found

    def valid_direction(self, char: Character, direction: Direction) -> bool:
        x, y = char.get_position()
        x2, y2 = x, y
        if direction == Direction.UP:
            if y == 0:
                return False
            y = y - 1
            y2 = y2 - 2
        if direction == Direction.RIGHT:
            if x == self.n - 1:
                return False
            x = x + 1
            x2 = x2 + 2
        if direction == Direction.DOWN:
            if y == self.n - 1:
                return False
            y = y + 1
            y2 = y2 + 2
        if direction == Direction.LEFT:
            if x == 0:
                return False
            x = x - 1
            x2 = x2 - 2
        if char.type in (CharacterType.MINO_H, CharacterType.MINO_V):
            return self.__check_mino_direction__(char, direction, x, y, x2, y2)
        else:
            return self.level[x][y] == 0

    def __ariane_found__(self, mino: Character) -> bool:
        xm, ym = mino.get_position()
        xa, ya = self.ariane.get_position()
        if xa == xm and ya == ym:
            self.ariane_found = True
            return True
        return False

    def __move_mino__(self, mino: Character, direction: Direction) -> None:
        self.__update_mino_in_level__(mino, NONE)
        mino.move(direction)
        self.__update_mino_in_level__(mino, MINO)

    def __check_mino_direction__(self, char: Character, direction: Direction, x: int, y: int, x2: int, y2: int) -> bool:
        if char.type == CharacterType.MINO_V:
            if self.level[x][y] == 0 and self.__v_aligned__(char):
                if self.__ariane_found__(char) or (direction != Direction.LEFT and direction != Direction.RIGHT)\
                        or self.level[x2][y2] != 0:
                    return False
                return True
        if char.type == CharacterType.MINO_H:
            if self.level[x][y] == 0 and self.__h_aligned__(char):
                if self.__ariane_found__(char) or (direction != Direction.UP and direction != Direction.DOWN) \
                        or self.level[x2][y2] != 0:
                    return False
                return True
        return self.level[x][y] == 0

    def __compute_mino_dir__(self, mino: Character) -> Direction:
        xa, ya = self.ariane.get_position()
        xm, ym = mino.get_position()
        x, y = xa - xm, ya - ym
        if mino.type == CharacterType.MINO_V:
            if y == 0:
                return Direction.RIGHT if (x > 0) else Direction.LEFT
            else:
                return Direction.UP if (y < 0) else Direction.DOWN
        if mino.type == CharacterType.MINO_H:
            if x == 0:
                return Direction.UP if (y < 0) else Direction.DOWN
            else:
                return Direction.RIGHT if (x > 0) else Direction.LEFT

    def __compute_thesee_dir__(self):
        xt, yt = self.thesee.get_position()
        xa, ya = self.ariane.get_position()
        if ya == yt:
            if xa - xt == 2:
                return Direction.RIGHT
            if xa - xt == -2:
                return Direction.LEFT
        if xa == xt:
            if ya - yt == 2:
                return Direction.DOWN
            if ya - yt == -2:
                return Direction.UP

    def __update_mino_in_level__(self, mino: Character, value: str) -> None:
        x, y = mino.get_position()
        self.level[x][y] = value

    def __h_aligned__(self, mino: Character) -> bool:  # for minoH
        xm, ym = mino.get_position()
        xa, ya = self.ariane.get_position()
        return True if (xa == xm) else False

    def __v_aligned__(self, mino: Character) -> bool:  # for minoV
        xm, ym = mino.get_position()
        xa, ya = self.ariane.get_position()
        return True if (ya == ym) else False
