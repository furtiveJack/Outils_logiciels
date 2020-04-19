import os
import time

from src.world import *
from src.parser import *
from src.naive_solver import NaiveSolver
from src.minimal_solver import MinimalSolver
import src.view as view
import upemtk as upemtk
import sys


def display_result(world: World):
    """
    Display a text on the window when the game is in a winning or loosing state.
    :param: world : the world attached to the current window view.
    """
    if world.game_won():
        upemtk.texte(HEIGHT // 2, WIDTH // 2, "ARIANE WON", couleur="blue", ancrage="center", taille=40)
        upemtk.attend_clic_gauche()
        return
    if world.game_lost():
        upemtk.texte(HEIGHT // 2, WIDTH // 2, "ARIANE LOST", couleur="red", ancrage="center", taille=40)
        upemtk.attend_clic_gauche()
        return


def still_remaining_options(world: World) -> bool:
    solver = NaiveSolver()
    current_conf = world.to_configuration()
    clue = solver.solve(world)
    world.load_configuration(current_conf)
    if not clue:
        upemtk.texte(HEIGHT // 2, WIDTH // 2, "NO MORE OPTION, GAME LOST :(", couleur="red", ancrage="center",
                     taille=40)
        upemtk.attend_clic_gauche()
        return False
    return True


def player_game(lab_path: str) -> None:
    """
    Start a new game where the player controls Ariane. The world is loaded using the file whose path has been provided.
    :param lab_path: path of the file to parse to create the world
    :return: None
    """
    canceled_last_move = False
    world = create_world_from_file(lab_path)
    view.create_window(world)
    view.terminal_display(world)
    view.display(world)
    world.save_game_state()
    while True:
        # If the player has no more chance of winning, the game is stopped
        if not still_remaining_options(world):
            break
        ev = upemtk.attend_ev()
        tev = upemtk.type_ev(ev)
        if tev == 'Quitte':
            break
        if tev == 'Touche':
            key = touche(ev)
            if key == 'c':
                if not canceled_last_move:
                    world.cancel_move(view)
                    canceled_last_move = True
                    continue
            else:
                canceled_last_move = False
            direction = get_dir_from_string(key)
            if not world.move_ariane(direction):
                continue
            world.move_thesee()
            view.display(world)
            if world.game_won():
                display_result(world)
                break
            world.move_minos(view)
            if world.game_lost():
                display_result(world)
                break
            world.save_game_state()
    upemtk.ferme_fenetre()


def solver_game(lab_path: str, game_type: str, display: bool) -> None:
    """
    Start a new game where one of the solver tries to solve the game, and then demonstrate its solution if it can
    find one.
    :param lab_path: path of the file to parse to create the world.
    :param game_type: type of solver that the user wants to use (naive or minimal)
    :param display: set to True, the user will visualize all the computations steps made by the solver to find a
           solution.
    :return: None
    """
    if game_type == "naive":
        solver = NaiveSolver()
    elif game_type == "minimal":
        solver = MinimalSolver()
    else:
        return usage()
    world = create_world_from_file(lab_path)
    initial_config = world.to_configuration()
    view.create_window(world)
    view.display(world)
    if solver.solve(world, display):
        print("Solution found (", len(solver.solution), "moves) !")
        solver.display_solution()
        world.load_configuration(initial_config)
        upemtk.texte(HEIGHT // 2, WIDTH // 2, "CLICK TO SEE SOLUTION",
                     couleur='black', ancrage='center', taille=40, tag="click_to_display")
        upemtk.attend_clic_gauche()
        upemtk.efface("click_to_display")
        view.display(world)
        solver.play_game(world)
        display_result(world)
    else:
        print("No solution found...")
    upemtk.ferme_fenetre()


def benchmark() -> None:
    """
    Start a benchmark to compare the two implemented solvers : NaiveSolver and MinimalSolver.
    This method runs both of the solvers and all the levels marked as "defi" in maps/defi directory.
    Then both of there results are print in the terminal.
    :return: None
    """
    directory = "maps/defi/"
    challenges = os.listdir(directory)
    challenges.sort()
    for challenge in challenges:
        if challenge.startswith("defi") and challenge.endswith(".txt"):
            naive = NaiveSolver()
            minimal = MinimalSolver()
            world = create_world_from_file(directory + challenge)
            config = world.to_configuration()
            n_time_ms = int(round(time.time() * 1000))
            n_res = naive.solve(world, False)
            n_time_ms = int(round(time.time() * 1000)) - n_time_ms
            world.load_configuration(config)
            m_time_ms = int(round(time.time() * 1000))
            m_res = minimal.solve(world, False)
            m_time_ms = int(round(time.time() * 1000)) - m_time_ms
            if n_res:
                dfs = "\t- DFS : " + str(len(naive.solution)) + " moves\t(" + str(n_time_ms) + "ms)\t\t"
            else:
                dfs = "\t- DFS : " + "No solution\t(" + str(n_time_ms) + "ms)\t\t"
            if m_res:
                bfs = "\t- BFS : " + str(len(minimal.solution)) + " moves\t(" + str(m_time_ms) + "ms)"
            else:
                bfs = "\t- BFS : " + "No solution\t(" + str(m_time_ms) + "ms)"
            print(challenge, dfs, bfs)


def usage():
    print("\n**usage**: python3 ariane.py <lab_path> <classic|naive|minimal> -v")
    print("\n--> To visualize the progress of one of the solver, just add the -v option")


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "benchmark":
        return benchmark()
    if len(sys.argv) < 3:
        return usage()
    lab = sys.argv[1]
    game_type = sys.argv[2]
    visualize = False
    if len(sys.argv) == 4 and game_type != "classic":
        visualize = sys.argv[3] == "-v"

    if game_type == "classic":
        return player_game(lab)
    elif game_type == "minimal" or game_type == "naive":
        return solver_game(lab, game_type, visualize)
    else:
        return usage()


if __name__ == '__main__':
    main()
