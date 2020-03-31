import upemtk as upemtk
from world import World
from utils import *


def create_window(world: World):
    upemtk.cree_fenetre(HEIGHT, WIDTH)
    upemtk.rectangle(0, 0, WIDTH, HEIGHT, "white", "white")
    draw_walls(world)


def display(world: World) -> None:
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
    for line in world.level:
        print(line)
    world.ariane.to_string()
    world.thesee.to_string()
    world.door.to_string()
    for mino in world.mino_h:
        mino.to_string()
    for mino in world.mino_v:
        mino.to_string()


def draw_walls(world):
    scale = HEIGHT // world.n
    for i in range(0, world.n):
        for j in range(0, world.n):
            if world.level[i][j] == V_WALL:
                upemtk.image(ORIGIN + i * scale, ORIGIN + j * scale, "../media/wallV.png")
            if world.level[i][j] == H_WALL:
                upemtk.image(ORIGIN + i * scale, ORIGIN + j * scale, "../media/wallH.png")
            if world.level[i][j] == C_WALL:
                upemtk.image(ORIGIN + i * scale, ORIGIN + j * scale, "../media/wallC.png")
