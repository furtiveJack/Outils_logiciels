from world import *
import view as view
import upemtk as upemtk
from parser import *


def cancel_move(m_world: World, m_view) -> None:
    m_world.cancel_move()
    m_world.save_game_state()
    m_view.display(m_world)


def move_minos(m_world: World, m_view) -> None:
    for mino in m_world.mino_v:
        m_world.move_mino(mino)
        m_view.display(m_world)
    for mino in m_world.mino_h:
        m_world.move_mino(mino)
        m_view.display(m_world)


if __name__ == '__main__':
    canceled_last_move = False
    world = create_world_from_file("../maps/small/small1.txt")
    view.create_window(world)
    view.terminal_display(world)
    view.display(world)
    world.save_game_state()
    while not world.game_ended():
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
            if world.game_ended():
                break
            move_minos(world, view)
            world.save_game_state()
    upemtk.ferme_fenetre()
    if world.ariane_found:
        print("Ariane lost!")
    if world.door_found:
        print("Ariane won!")
