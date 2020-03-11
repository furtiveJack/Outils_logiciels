from upemtk import *
from utils import *


class Character:
    def __init__(self, x, y, image_name, type):
        self.x = x
        self.y = y
        self.image_name = image_name
        self.type = type

    def draw(self, cell_size):
        image(ORIGIN + self.x * cell_size, ORIGIN + self.y * cell_size, self.image_name)

    def to_string(self):
        print(self.type.name, ' : (', self.x, ', ', self.y, ')')
