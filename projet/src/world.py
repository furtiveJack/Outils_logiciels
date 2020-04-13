from src.character import *
from src.utils import *


class World:
    def __init__(self, level: list, ariane: tuple, thesee: tuple, mino_h: list, mino_v: list, door: tuple):
        self.level = level
        self.n = len(level[0])
        self.ariane = Character(ariane[1], ariane[0], "media/ariane.png", CharacterType.ARIANE)
        self.thesee = Character(thesee[1], thesee[0], "media/thesee.png", CharacterType.THESEE)
        self.mino_h = [Character(mino[1], mino[0], "media/minoH.png", CharacterType.MINO_H) for mino in mino_h]
        self.mino_v = [Character(mino[1], mino[0], "media/minoV.png", CharacterType.MINO_V) for mino in mino_v]
        self.door = Character(door[1], door[0], "media/porte.png", CharacterType.DOOR)
        self.ariane_found = False
        self.door_found = False
        self.history = []

    def save_game_state(self):
        state = [self.ariane.get_position(), self.thesee.get_position(), [mino.get_position() for mino in self.mino_v],
                 [mino.get_position() for mino in self.mino_h]]
        self.history.append(state)

    def cancel_move(self):
        if len(self.history) < 2:
            return
        self.history.pop()              # Removing last player move
        state = self.history.pop()      # Getting the move before
        self.ariane.teleport(state[0])
        self.thesee.teleport(state[1])
        for i in range(len(self.mino_v)):
            self.mino_v[i].teleport(state[2][i])
        for i in range(len(self.mino_h)):
            self.mino_h[i].teleport(state[3][i])

    def move_all(self, ariane_dir: Direction) -> bool:
        if not self.move_ariane(ariane_dir):
            return False
        self.move_thesee()
        for mino in self.mino_v:
            self.move_mino(mino)
        for mino in self.mino_h:
            self.move_mino(mino)
        return True

    def move_ariane(self, direction: Direction) -> bool:
        if (direction is None) or (not self.valid_direction(self.ariane, direction)):
            return False
        self.ariane.move(direction)
        return True

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

    def game_lost(self) -> bool:
        return self.ariane_found

    def game_won(self) -> bool:
        return self.door_found

    def valid_direction(self, char: Character, direction: Direction) -> bool:
        x, y = char.get_position()  # Get current position
        x2, y2 = x, y  # Destination position depending on the character direction
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
            return self.level[y][x] == 0

    def to_configuration(self) -> tuple:
        mino_h = [mino.get_position() for mino in self.mino_h]
        mino_v = [mino.get_position() for mino in self.mino_v]
        conf = (self.ariane.get_position(), self.thesee.get_position(),
                self.ariane_found, self.door_found,
                tuple(mino_v), tuple(mino_h))
        return conf

    def load_configuration(self, conf: tuple) -> None:
        self.ariane.teleport(conf[0])
        self.thesee.teleport(conf[1])
        self.ariane_found = conf[2]
        self.door_found = conf[3]
        for i in range(len(self.mino_v)):
            self.__update_mino_in_level__(self.mino_v[i], NONE)
            self.mino_v[i].teleport(conf[4][i])
            self.__update_mino_in_level__(self.mino_v[i], MINO)
        for i in range(len(self.mino_h)):
            self.__update_mino_in_level__(self.mino_h[i], NONE)
            self.mino_h[i].teleport(conf[5][i])
            self.__update_mino_in_level__(self.mino_h[i], MINO)

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
        if self.__ariane_found__(char):
            return False
        if char.type == CharacterType.MINO_V:
            if self.level[y][x] == 0 and self.__v_aligned__(char):
                if (direction != Direction.LEFT and direction != Direction.RIGHT) or self.level[x2][y2] != 0:
                    return False
        if char.type == CharacterType.MINO_H:
            if self.level[y][x] == 0 and self.__h_aligned__(char):
                if (direction != Direction.UP and direction != Direction.DOWN) or self.level[x2][y2] != 0:
                    return False
        return self.level[y][x] == 0 and self.level[y2][x2] == 0

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
        self.level[y][x] = value

    def __h_aligned__(self, mino: Character) -> bool:
        xm, ym = mino.get_position()
        xa, ya = self.ariane.get_position()
        return True if (xa == xm) else False

    def __v_aligned__(self, mino: Character) -> bool:
        xm, ym = mino.get_position()
        xa, ya = self.ariane.get_position()
        return True if (ya == ym) else False


def cancel_move(m_world: World, m_view) -> None:
    m_world.cancel_move()
    m_world.save_game_state()
    m_view.display(m_world)


def move_minos(m_world: World, m_view) -> None:
    for mino in m_world.mino_v:
        m_world.move_mino(mino)
        m_view.display(m_world)
    for mino in m_world.mino_h:
        m_world.move_mino(mino)
        m_view.display(m_world)

