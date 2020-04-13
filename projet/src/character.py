from upemtk import *
from src.utils import *


class Character:
    currentId = 0

    def __init__(self, x, y, image_name, character_type):
        Character.currentId += 1
        self.x = x
        self.y = y
        self.image_name = image_name
        self.type = character_type
        self.id = self.type.name + str(Character.currentId)

    def draw(self, cell_size: int):
        efface(self.id)
        image(ORIGIN + self.x * cell_size, ORIGIN + self.y * cell_size, self.image_name, tag=self.id)

    def to_string(self):
        print(self.type.name, ' : (', self.x, ', ', self.y, ') - id :', self.id)

    def move(self, direction: Direction) -> None:
        if direction == Direction.UP:
            self.y -= 2
        if direction == Direction.DOWN:
            self.y += 2
        if direction == Direction.LEFT:
            self.x -= 2
        if direction == Direction.RIGHT:
            self.x += 2

    def teleport(self, position: tuple) -> None:
        self.x = position[0]
        self.y = position[1]

    def get_position(self) -> tuple:
        return self.x, self.y
