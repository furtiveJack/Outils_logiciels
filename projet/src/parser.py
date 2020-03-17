from world import World


def create_from_file(path):
    file = open(path, "r")
    size = int(file.readline())
    grid = [[0 for _ in range(2 * size + 1)] for _ in range(2 * size + 1)]
    i = 0
    j = 0
    ariane = (-1, -1)
    thesee = (-1, -1)
    door = (-1, -1)
    minoH = []
    minoV = []

    for line in file:
        for char in line:
            if char == "\n":
                j = 0
                continue
            elif char == "+" or char == "-" or char == "|":
                grid[i][j] = 1
            elif char == 'A':
                ariane = (i, j)
            elif char == 'T':
                thesee = (i, j)
            elif char == 'H':
                minoH.append((i, j))
            elif char == 'V':
                minoV.append((i, j))
            elif char == 'P':
                door = (i, j)
            else:
                grid[i][j] = 0
            j += 1
        i += 1
    return World(grid, ariane, thesee, minoH, minoV, door)
