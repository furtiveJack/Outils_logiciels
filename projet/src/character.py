from upemtk import *
from utils import *


class Character:
    def __init__(self, x, y, image_name, character_type):
        self.x = x
        self.y = y
        self.image_name = image_name
        self.type = character_type

    def draw(self, cell_size: int):
        efface(self.type)
        image(ORIGIN + self.x * cell_size, ORIGIN+self.y * cell_size, self.image_name, tag=self.type)

    def to_string(self):
        print(self.type.name, ' : (', self.x, ', ', self.y, ')')

    def move(self, direction: Direction) -> None:
        if self.type == CharacterType.ARIANE:
            self.move_ariane(direction)
        if self.type == CharacterType.THESEE:
            self.move_thesee(direction)
        if self.type == CharacterType.MINO:
            self.move_mino(direction)

    def move_ariane(self, direction: Direction) -> None:
        if direction == Direction.UP:
            self.y -= 2
        if direction == Direction.DOWN:
            self.y += 2
        if direction == Direction.LEFT:
            self.x -= 2
        if direction == Direction.RIGHT:
            self.x += 2

    def move_thesee(self, direction):
        pass

    def move_mino(self, direction):
        pass