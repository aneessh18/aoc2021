import sys

filename = sys.argv[1]
steps = int(sys.argv[2])


def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def energy_spikes(energy_levels, x, y):
    direcs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    spikes = [1 for direc in direcs if
              is_valid(direc[0] + x, direc[1] + y, 10, 10) and energy_levels[direc[0] + x][direc[1] + y] == 10]
    return sum(spikes)


def reset_energy_levels(energy_levels, i, j):

    direcs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    energy_levels[i][j] = 0
    for direc in direcs:
        x1 = direc[0] + i
        y1 = direc[1] + j
        if is_valid(x1, y1, 10, 10) and energy_levels[x1][y1] != 10and energy_levels[x1][y1] != 0:
            energy_levels[x1][y1] += 1
        if is_valid(x1, y1, 10, 10) and energy_levels[x1][y1] == 10: # should recurse its neighbors
            reset_energy_levels(energy_levels, x1, y1)



def next_step(energy_levels):
    energy_levels = [[energy_levels[i][j] + 1 for j in range(10)] for i in range(10)]
    # first inc the energy
    # then inc the adjacent ones
    # then reset the energy levels
    for i in range(10):
        for j in range(10):
            if energy_levels[i][j] == 10:
                reset_energy_levels(energy_levels, i, j)

    return energy_levels

with open(filename) as file:
    lines = file.readlines()
    energy_levels = [map(int, line.rstrip()) for line in lines]
    flashes = 0
    for i in range(steps):
        energy_levels = next_step(energy_levels)
        # print(energy_levels)
        flashes += len([1 for i in range(10) for j in range(10) if energy_levels[i][j] == 0])
    print(flashes)

    step = 0
    flashes = 0
    while True:
        energy_levels = next_step(energy_levels)
        step += 1
        # print(energy_levels)
        flashes = len([1 for i in range(10) for j in range(10) if energy_levels[i][j] == 0])
        if flashes == 100:
            print(step)
            break

