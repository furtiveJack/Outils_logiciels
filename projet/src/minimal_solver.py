import time
import src.view as view
from src.utils import Direction, dir_to_string, get_dir_from_string
from src.world import World


class MinimalSolver:
    """
    This class represents a solver that search for a solution with the lowest number of moves possible.
    """
    def __init__(self):
        self.solution = []
        self.visited = set()

    def solve(self, world: World, display=False) -> bool:
        """
        Solve the world provided, using a Breadth-First Search algorithm.
        From the initial configuration of the world, this methods search for a winning configuration with a minimal
        number of moves for Ariane.
        :param world: the world to solve.
        :param display: if set to True, the method will draw each step of its computation. Set it to False if you need
                to quickly compute the result.
        :return: True if there is a solution for this world, False otherwise.
        """
        conf = world.to_configuration()
        to_treat = [(conf, [])]
        self.visited.add(conf)
        while len(to_treat) > 0:
            current, dir_list = to_treat.pop(0)
            world.load_configuration(current)
            if world.game_won():
                self.solution = dir_list
                return True
            if world.game_lost():
                continue
            for direction in Direction:
                if not world.valid_direction(world.ariane, direction):
                    continue
                world.move_all(direction)
                if display:
                    view.display(world)
                    time.sleep(0.05)
                updated = world.to_configuration()
                if updated not in self.visited:
                    self.visited.add(updated)
                    # Constructing a new list containing all the directions that lead to the previous configuration,
                    # and add the direction that leads to the new configuration
                    updated_dir_list = dir_list + [dir_to_string(direction)]
                    to_treat.append((updated, updated_dir_list))
                world.load_configuration(current)
        return False

    def display_solution(self) -> None:
        """
        Display the solution computed by this solver
        :return: None, but display the list containing all the moves Ariane should do to win the game
        """
        print(self.solution)

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
