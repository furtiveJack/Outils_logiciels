from src.world import *
from src.parser import *
from src.naive_solver import NaiveSolver
from src.minimal_solver import MinimalSolver
import src.view as view
import upemtk as upemtk
import sys


def play_game(lab_path: str) -> None:
    canceled_last_move = False
    world = create_world_from_file(lab_path)
    view.create_window(world)
    view.terminal_display(world)
    view.display(world)
    world.save_game_state()
    while True:
        ev = upemtk.attend_ev()
        tev = upemtk.type_ev(ev)
        if tev == 'Quitte':
            break
        if tev == 'Touche':
            key = touche(ev)
            if key == 'c':
                if not canceled_last_move:
                    cancel_move(world, view)
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
                upemtk.texte(500, 500, "ARIANE WON", "blue", "center")
                upemtk.attend_clic_gauche()
                break
            move_minos(world, view)
            if world.game_lost():
                upemtk.texte(500, 500, "ARIANE LOST", couleur="red", ancrage="center", taille=40)
                upemtk.attend_clic_gauche()
                break
            world.save_game_state()
    upemtk.ferme_fenetre()


def naive_game(lab_path: str, visualize: bool) -> None:
    solver = NaiveSolver()
    world = create_world_from_file(lab_path)
    initial_config = world.to_configuration()
    view.create_window(world)
    view.terminal_display(world)
    view.display(world)
    if solver.solve(world, world.to_configuration(), visualize):
        print("Solution found !")
        solver.display_solution()
        world.load_configuration(initial_config)
        upemtk.texte(HEIGHT//2, WIDTH//2, "CLICK TO SEE SOLUTION",
                    couleur='black', ancrage='center', taille=40, tag="click_to_display")
        upemtk.attend_clic_gauche()
        upemtk.efface("click_to_display")
        view.display(world)
        solver.play_game(world)
    else:
        print("No solution found...")
    upemtk.attend_clic_gauche()
    upemtk.ferme_fenetre()


def minimal_game(lap_path: str, visualize: bool) -> None:
    solver = MinimalSolver()
    world = create_world_from_file(lap_path)
    view.create_window(world)
    view.terminal_display(world)
    view.display(world)
    if solver.solve(world, visualize):
        print("Solution found!")
    else:
        print("No solution found")


def usage():
    print("\n**usage**: python3 ariane.py <lab_path> <classic|naive|minimal> -v")
    print("\n--> To visualize the progress of one of the solver, just add the -v option")


def main():
    if len(sys.argv) < 3:
        return usage()

    lab = sys.argv[1]
    game_type = sys.argv[2]
    visualize = False
    if len(sys.argv) == 4 and game_type != "classic":
        visualize = sys.argv[3] == "-v"

    if game_type == "classic":
        return play_game(lab)
    elif game_type == "naive":
        return naive_game(lab, visualize)
    elif game_type == "minimal":
        return minimal_game(lab, visualize)
    else:
        return usage()


if __name__ == '__main__':
    main()
