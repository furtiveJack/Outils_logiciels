from src.character import *
from src.utils import *


class World:
    """
    A class to represent the game.
    A game is composed of walls and characters.
    """
    def __init__(self, level: list, ariane: tuple, thesee: tuple, mino_h: list, mino_v: list, door: tuple):
        """
        Initialize a new member of this class.
        :param level: a matrix representing the positions of walls and minotaurs.
        :param ariane: a tuple(int, int) representing the initial position of Ariane
        :param thesee: a tuple(int, int) representing the initial position of Thesee
        :param mino_h: a list of tuple(int, int) representing the initial positions of the Horizontal Minotaurs
        :param mino_v: a list of tuple(int, int) representing the initial positions of the Vertical Minotaurs
        :param door:  a tuple(int, int) representing the initial position of the Door
        """
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

    def save_game_state(self) -> None:
        """
        Save the current state of the world. A state is a list of the position of every character at a given time.
        The state is saved in the self.history list.
        :return:  None
        """
        state = [self.ariane.get_position(), self.thesee.get_position(), [mino.get_position() for mino in self.mino_v],
                 [mino.get_position() for mino in self.mino_h]]
        self.history.append(state)

    def cancel_move(self, m_view) -> None:
        """
        Cancel the last move, and re draw the game in its previous state.
        :param m_view: The view used to re draw the world.
        :return: None
        """
        self.__cancel_move__()
        self.save_game_state()
        m_view.display(self)

    def __cancel_move__(self) -> None:
        """
        Cancel the last move, and retrieves the one before in the world history.
        Characters are moved to their previous position.
        :return: None
        """
        if len(self.history) < 2:
            return
        self.history.pop()              # Removing last player move
        state = self.history.pop()      # Getting the move before
        self.ariane.teleport(state[0])
        self.thesee.teleport(state[1])
        for i in range(len(self.mino_v)):
            self.__update_mino_in_level__(self.mino_v[i], NONE)
            self.mino_v[i].teleport(state[2][i])
            self.__update_mino_in_level__(self.mino_v[i], MINO)
        for i in range(len(self.mino_h)):
            self.__update_mino_in_level__(self.mino_h[i], NONE)
            self.mino_h[i].teleport(state[3][i])
            self.__update_mino_in_level__(self.mino_h[i], MINO)

    def move_all(self, ariane_dir: Direction) -> bool:
        """
        Move all the characters of the world in relation to Ariane direction.
        :param ariane_dir: the direction in which Ariane should move.
        :return: True if the direction is valid regarding the current position of Ariane, False otherwise.
        """
        if not self.move_ariane(ariane_dir):
            return False
        self.move_thesee()
        for mino in self.mino_v:
            self.move_mino(mino)
        for mino in self.mino_h:
            self.move_mino(mino)
        return True

    def move_ariane(self, direction: Direction) -> bool:
        """
        Move Ariane in the given direction.
        :param direction: the direction to move to.
        :return: True if move is possible, False otherwise.
        """
        if (direction is None) or (not self.valid_direction(self.ariane, direction)):
            return False
        self.ariane.move(direction)
        return True

    def move_thesee(self) -> None:
        """
        Move Thesee. If Ariane is next to him, he will follow any of her moves. Otherwise, he's just there,
        waiting (which is quite dangerous in a place full of minotaurs).
        :return: None
        """
        direction = self.__compute_thesee_dir__()
        if direction is None:
            return
        if self.valid_direction(self.thesee, direction):
            self.thesee.move(direction)
        if self.thesee.get_position() == self.door.get_position():
            if self.ariane.get_position() == self.door.get_position():
                self.door_found = True

    def move_minos(self, m_view) -> None:
        """
        Move and display every minotaur of the world.
        :param m_view: the view used to display the minotaurs.
        :return: None
        """
        for mino in self.mino_v:
            self.move_mino(mino)
            m_view.display(self)
        for mino in self.mino_h:
            self.move_mino(mino)
            m_view.display(self)

    def move_mino(self, mino: Character) -> None:
        """
        Move the provided minotaur.
        :param mino: the minotaur to move.
        :return: None
        """
        direction = self.__compute_mino_dir__(mino)
        while True:
            if not self.valid_direction(mino, direction):
                return
            self.__move_mino__(mino, direction)
            if self.__ariane_found__(mino):
                return

    def game_lost(self) -> bool:
        """
        Check if Ariane has be found by a minotaur.
        :return: True if Ariane will die eaten, False otherwise.
        """
        return self.ariane_found

    def game_won(self) -> bool:
        """
        Check if Ariane and Thesee have reach the door.
        :return: True if they have a future, False otherwise.
        """
        return self.door_found

    def valid_direction(self, char: Character, direction: Direction) -> bool:
        """
        Check if the provided character can go in the given direction, depending on its current position and on
        the game state.
        :param char: the character that wants to move.
        :param direction: the direction in which the character wants to go.
        :return: True if the direction is valid, False otherwise.
        """
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
        """
        Convert the world to a configuration used by the solvers.
        A configuration is a tuple containing the position of each character, and the variables representing the ending
        conditions of the game.
        :return: a tuple containing (in order) :
            - ariane position : tuple
            - thesee position : tuple
            - ariane_found : bool
            - door_found : bool
            - mino_v positions : list of tuples
            - mino_h positions : list of tuples
        """
        mino_h = [mino.get_position() for mino in self.mino_h]
        mino_v = [mino.get_position() for mino in self.mino_v]
        conf = (self.ariane.get_position(), self.thesee.get_position(),
                self.ariane_found, self.door_found,
                tuple(mino_v), tuple(mino_h))
        return conf

    def load_configuration(self, conf: tuple) -> None:
        """
        Load a configuration (respecting the format returned by the self.to_configuration() method).
        :param conf: the configuration to reload
        :return: None
        """
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
        """
        Check if the given minotaur has found Ariane or not.
        :param mino: a minotaur of the world
        :return: True if this minotaur has found Ariane, False otherwise.
        """
        xm, ym = mino.get_position()
        xa, ya = self.ariane.get_position()
        if xa == xm and ya == ym:
            self.ariane_found = True
            return True
        return False

    def __move_mino__(self, mino: Character, direction: Direction) -> None:
        """
        Remove this minotaur from the level grid, then move it in the given direction, and write its new position
        back into the level grid.
        :param mino: the minotaur to move.
        :param direction: the direction in which the minotaur should move.
        :return: None
        """
        self.__update_mino_in_level__(mino, NONE)
        mino.move(direction)
        self.__update_mino_in_level__(mino, MINO)

    def __check_mino_direction__(self, char: Character, direction: Direction, x: int, y: int, x2: int, y2: int) -> bool:
        """
        Check if the provided direction is valid for this minotaur. This method is use to find if the minotaur
        should continue to move in the given direction, or stop because he encountered Ariane/a wall/another minotaur.
        :param char: the minotaur currently moving.
        :param direction: the current direction of the minotaur
        :param x: the x coordinate of the next cell (to check if it contains a wall)
        :param y: the y coordinate of the next cell (to check if it contains a wall)
        :param x2: the x coordinate of the next next cell (to check if it contains Ariane/another minotaur)
        :param y2: the y coordinate of the next next cell (to check if it contains Ariane/another minotaur)
        :return: True if the minotaur should continue to move, False otherwise.
        """
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
        """
        Compute the direction in which this minotaur should go to find Ariane, depending of its type (Horizontal or
        Vertical).
        :param mino: the minotaur to move .
        :return: the next direction the minotaur should take.
        """
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

    def __compute_thesee_dir__(self) -> Direction:
        """
        Compute the direction of Thesee.

        If Ariane is on the cell next to him, Thesee will follow each of oher step.
        If not, he will wait where he is.
        :return: the Direction thesee should take if he has to move, None otherwise.
        """
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
        """
        Use the current position (x, y) of the minotaur to update its value in the level grid.
        :param mino: the minotaur to update in the grid.
        :param value: the value to use (MINO or NONE)
        :return: None
        """
        x, y = mino.get_position()
        self.level[y][x] = value

    def __h_aligned__(self, mino: Character) -> bool:
        """
        Check if this minotaur (which should be a CharacterType.MINO_H) is on the same column as Ariane.
        :param mino: a minotaur of CharacterType MINO_H.
        :return: True if the minotaur is on the same column as Ariane, False otherwise.
        """
        xm, ym = mino.get_position()
        xa, ya = self.ariane.get_position()
        return True if (xa == xm) else False

    def __v_aligned__(self, mino: Character) -> bool:
        """
        Check if this minotaur (which should be a CharacterType.MINO_V) is on the same line as Ariane.
        :param mino: a minotaur of CharacterType MINO_V.
        :return: True if the minotaur is on the same line as Ariane, False otherwise.
        """
        xm, ym = mino.get_position()
        xa, ya = self.ariane.get_position()
        return True if (ya == ym) else False


