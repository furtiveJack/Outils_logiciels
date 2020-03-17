from world import *

world = create_world_from_file("../maps/labyrinthe2.txt")

create_window()
world.terminal_display()
world.window_display()


