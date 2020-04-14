from upemtk import *
from src.utils import *


class Character:
    """
    A class to represent the characters used in the Ariane's challenge.
    """
    currentId = 0  # Unique id used to identify each member of this class

    def __init__(self, x: int, y: int, image_name: str, character_type: CharacterType):
        """
        Initialize a new member of this class
        :param x: the x position of the character in the level grid
        :param y: the y position of the character in the level grid
        :param image_name: name of the image to use when drawing this character
        :param character_type: type of character (Arianne | Thesee | Horizontal/Vertical Minotaur | Door)
        """
        Character.currentId += 1
        self.x = x
        self.y = y
        self.image_name = image_name
        self.type = character_type
        self.id = self.type.name + str(Character.currentId)

    def draw(self, cell_size: int) -> None:
        """
        Draw on the window this character at its current position.
        Remove from the window the previous drawing of this character
        :param cell_size: Size of a cell in the window
        :return: None
        """
        efface(self.id)
        image(ORIGIN + self.x * cell_size, ORIGIN + self.y * cell_size, self.image_name, tag=self.id)

    def to_string(self):
        print(self.type.name, ' : (', self.x, ', ', self.y, ') - id :', self.id)

    def move(self, direction: Direction) -> None:
        """
        Move this character one cell forward in the given direction
        :param direction: the direction in which the character should move
        :return: None
        """
        if direction == Direction.UP:
            self.y -= 2
        if direction == Direction.DOWN:
            self.y += 2
        if direction == Direction.LEFT:
            self.x -= 2
        if direction == Direction.RIGHT:
            self.x += 2

    def teleport(self, position: tuple) -> None:
        """
        Move the character to the given position.
        No verification is made regarding whether the position is valid or not
        :param position: a tuple (int, int) containing the position to move to
        :return: None
        """
        self.x = position[0]
        self.y = position[1]

    def get_position(self) -> tuple:
        """
        Return the character's current position in the grid
        :return: a tuple of (int, int) representing the current position of the character
        """
        return self.x, self.y
