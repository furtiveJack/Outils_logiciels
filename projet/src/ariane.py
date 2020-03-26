from world import *
world = create_world_from_file("../maps/big/big2.txt")

create_window()
world.terminal_display()
world.window_display()
world.ariane.move(Direction.RIGHT)
