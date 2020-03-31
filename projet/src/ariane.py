from world import *
import view as view
import upemtk as upemtk
from parser import *

if __name__ == '__main__':
    world = create_world_from_file("../maps/small/small2.txt")
    view.create_window(world)
    view.terminal_display(world)
    view.display(world)
    while not world.game_ended():
        ev = upemtk.attend_ev()
        tev = upemtk.type_ev(ev)
        if tev == 'Quitte':
            break
        if tev == 'Touche':
            key = touche(ev)
            direction = get_dir_from_string(key)
            if direction is None:
                continue
            if not world.valid_direction(world.ariane, direction):
                continue
            world.move_ariane(direction)
            world.move_thesee()
            view.display(world)
            if world.game_ended():
                break
            for mino in world.mino_v:
                world.move_mino(mino)
                view.display(world)
            for mino in world.mino_h:
                world.move_mino(mino)
                view.display(world)
    upemtk.ferme_fenetre()
    if world.ariane_found:
        print("Ariane lost!")
    if world.door_found:
        print("Ariane won!")
