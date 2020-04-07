import time

from world import *
from utils import *
import view as view
from parser import *


class NaiveSolver:
    def __init__(self):
        self.visited = set()
        self.solution = []

    def solve(self, world: World) -> bool:
        print("start")
        conf = world.to_configuration()
        print(conf)
        if world.ariane.get_position() == world.door.get_position():
            print("ariane won")
            return True
        if world.ariane_found:
            print("ariane found on conf ", conf)
            return False
        self.visited.add(conf)
        # print("visited : ", self.visited)
        for direction in Direction:
            world.load_configuration(conf)
            if not world.valid_direction(world.ariane, direction):
                continue
            else:
                world.move_all(direction)
                view.display(world)
                time.sleep(0.3)
                updated_conf = world.to_configuration()
                print("new conf: ", updated_conf)
            if updated_conf in self.visited:
                print("already visited")
                continue
            if self.solve(world):
                self.solution.append(direction)
                return True
            else:
                print("next dir")
                continue
        return False


if __name__ == '__main__':
    solver = NaiveSolver()
    world = create_world_from_file("../maps/small/small1.txt")
    view.create_window(world)
    view.terminal_display(world)
    view.display(world)
    print(solver.solve(world))
    for direc in solver.solution[::-1]:
        if direc == Direction.UP:
            print("Up - ", end="")
        if direc == Direction.DOWN:
            print("Down - ", end="")
        if direc == Direction.LEFT:
            print("Left - ", end="")
        if direc == Direction.RIGHT:
            print("Right - ", end="")
