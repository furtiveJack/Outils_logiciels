import time

from src.world import World
import src.view as view
from src.parser import *


class NaiveSolver:
    """
    This class represents a solver that search for a solution in the game
    """
    def __init__(self):
        self.visited = set()
        self.solution = []

    def solve(self, world: World, display = False) -> bool:
        """
        Solve the world provided, using a Depth-First Search algorithm.
        From the initial configuration of the world, this methods search for a winning configuration by exploring all
        the configuration possibles.
        :param world: the world to solve.
        :param display: if set to True, the method will draw each step of its computation. Set it to False if you need
                to quickly compute the result.
        :return True if there is a solution for this world, False otherwise.
        """
        res = self.__solve__(world, world.to_configuration(), display)
        self.solution = self.solution[::-1]
        return res

    def __solve__(self, world: World, conf: tuple, display=False) -> bool:
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
            if self.__solve__(world, updated_conf, display):
                self.solution.append(dir_to_string(direction))
                return True
            else:
                continue
        return False

    def play_game(self, world: World) -> None:
        """
        This method should be called after self.solve() has been called.
        Emulate the game by making Ariane play all the moves found in the self.solution list.
        :param world: the world in which the solver should play the game
        :return: None
        """
        for direction in self.solution:
            input_dir = get_dir_from_string(direction)
            world.move_ariane(input_dir)
            world.move_thesee()
            view.display(world)
            if world.game_lost() or world.game_won():
                return
            world.move_minos(view)
            time.sleep(0.3)

    def display_solution(self):
        """
        Display the solution computed by this solver
        :return: None, but display the list containing all the moves Ariane should do to win the game
        """
        print(self.solution)

