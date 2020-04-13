import time

import src.view as view
from src.utils import Direction
from src.world import World


class MinimalSolver:
    def __init__(self):
        self.solution = []
        self.visited = set()

    def solve(self, world: World, display=False) -> bool:
        conf = world.to_configuration()
        to_treat = []
        self.visited.add(conf)
        to_treat.append(conf)
        while len(to_treat) > 0:
            current = to_treat.pop(0)
            print("--- conf :", current)
            world.load_configuration(current)
            if world.game_won():
                print("ARIANE WON")
                return True
            if world.game_lost():
                print("Ariane lost in this config")
                continue
            for direction in Direction:
                if not world.valid_direction(world.ariane, direction):
                    print("Cant go to", direction)
                    continue
                print("Ariane going to", direction)
                world.move_all(direction)
                if display:
                    view.display(world)
                    time.sleep(1)
                updated = world.to_configuration()
                print("--- updated conf : ", updated)
                if updated not in self.visited:
                    print("--- Adding updated conf to visited")
                    self.visited.add(updated)
                    to_treat.append(updated)
        return False
