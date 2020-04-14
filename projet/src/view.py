import upemtk as upemtk
from src.world import World
from src.utils import *
"""
Methods for drawing all the elements of the game
"""


def create_window(world: World) -> None:
    """
    Create a graphical window, and display a view of the world in its initial state.
    This method only display the walls of the world, not its characters.
    :param world: the world (game level) to display
    :return: None
    """
    upemtk.cree_fenetre(HEIGHT, WIDTH)
    upemtk.rectangle(0, 0, WIDTH, HEIGHT, "white", "white")
    draw_walls(world)


def display(world: World) -> None:
    """
    Display all the characters of this world in the window.
    :param world: the world for which the characters should be displayed
    :return: None
    """
    scale = HEIGHT // world.n
    world.ariane.draw(scale)
    world.thesee.draw(scale)
    world.door.draw(scale)
    for mino in world.mino_h:
        mino.draw(scale)
    for mino in world.mino_v:
        mino.draw(scale)
    upemtk.mise_a_jour()


def terminal_display(world: World) -> None:
    """
    Display the world (walls + characters) in a shell.
    :param world: the world to display
    :return:
    """
    for i in range(len(world.level[0])):
        for j in range(len(world.level[i])):
            if world.level[i][j] == C_WALL:
                print("+", end="")
            if world.level[i][j] == H_WALL:
                print("-", end="")
            if world.level[i][j] == V_WALL:
                print("|", end="")
            if world.level[i][j] == NONE:
                print(" ", end="")
            if world.level[i][j] == MINO:
                print("M", end="")
        print("")
    world.ariane.to_string()
    world.thesee.to_string()
    world.door.to_string()
    for mino in world.mino_h:
        mino.to_string()
    for mino in world.mino_v:
        mino.to_string()


def draw_walls(world: World) -> None:
    """
    Draw the walls of this world on the window
    :param world: the world for which the walls should be draw
    :return: None
    """
    scale = HEIGHT // world.n
    for i in range(0, world.n):
        for j in range(0, world.n):
            if world.level[j][i] == V_WALL:
                upemtk.image(ORIGIN + i * scale, ORIGIN + j * scale, "media/wallV.png")
            if world.level[j][i] == H_WALL:
                upemtk.image(ORIGIN + i * scale, ORIGIN + j * scale, "media/wallH.png")
            if world.level[j][i] == C_WALL:
                upemtk.image(ORIGIN + i * scale, ORIGIN + j * scale, "media/wallC.png")
