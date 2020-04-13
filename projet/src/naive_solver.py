import time

from src.world import move_minos
import src.view as view
from src.parser import *


class NaiveSolver:
    def __init__(self):
        self.visited = set()
        self.solution = []

    def solve(self, world: World, conf: tuple, display=False) -> bool:
        if world.game_won():
            return True
        if world.game_lost():
            return False
        self.visited.add(conf)
        for direction in Direction:
            world.load_configuration(conf)
            if not world.valid_direction(world.ariane, direction):
                continue
            else:
                world.move_all(direction)
                if display:
                    view.display(world)
                    time.sleep(0.05)
                updated_conf = world.to_configuration()
            if updated_conf in self.visited:
                continue
            if self.solve(world, updated_conf, display):
                self.solution.append(direction)
                return True
            else:
                continue
        return False

    def play_game(self, world: World) -> None:
        ariane_inputs = self.solution[::-1]
        for input_dir in ariane_inputs:
            world.move_ariane(input_dir)
            world.move_thesee()
            view.display(world)
            if world.game_lost() or world.game_won():
                return
            move_minos(world, view)
            time.sleep(0.3)

    def display_solution(self):
        for direction in self.solution[::-1]:
            if direction == Direction.UP:
                print("Up - ", end="")
            if direction == Direction.DOWN:
                print("Down - ", end="")
            if direction == Direction.LEFT:
                print("Left - ", end="")
            if direction == Direction.RIGHT:
                print("Right - ", end="")
        print("")

