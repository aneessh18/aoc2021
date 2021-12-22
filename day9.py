import sys

filename = sys.argv[1]


def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def is_low_point(smoke_flows, x, y):
    rows = len(smoke_flows)
    columns = len(smoke_flows[0])
    direcs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for direc in direcs:
        x1 = x + direc[0]
        y1 = y + direc[1]
        if is_valid(x1, y1, rows, columns) and smoke_flows[x1][y1] <= smoke_flows[x][y]:
            return False

    return True


def compute_low_points(smoke_flows):
    rows = len(smoke_flows)
    columns = len(smoke_flows[0])
    return [smoke_flows[i][j] for i in range(rows) for j in range(columns) if is_low_point(smoke_flows, i, j)]


def compute_basin_size(smoke_flows, visited, x, y):
    if visited[x][y]:
        return 0
    else:
        visited[x][y] = True
        direcs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        sub_basin_sizes = 0
        for direc in direcs:
            x1 = direc[0]+x
            y1 = direc[1]+y
            if is_valid(x1, y1, len(smoke_flows),len(smoke_flows[0])) and smoke_flows[x1][y1] != 9 and smoke_flows[x1][y1]>smoke_flows[x][y]:
                sub_basin_sizes += compute_basin_size(smoke_flows, visited, x1, y1)

        return 1 + sub_basin_sizes


def compute_basins(smoke_flows):
    rows = len(smoke_flows)
    columns = len(smoke_flows[0])
    visited = [[False for j in range(columns)] for i in range(rows)]
    basin_sizes = [compute_basin_size(smoke_flows, visited, i, j) for i in range(rows) for j in range(columns) if
                   is_low_point(smoke_flows, i, j)]

    basin_sizes.sort()
    print(basin_sizes)
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


with open(filename) as file:
    lines = file.readlines()
    smoke_flows = [map(int, line.rstrip()) for line in lines]
    # print(smoke_flows)
    low_points = compute_low_points(smoke_flows)
    risk = [low_point + 1 for low_point in low_points]
    print(risk)
    print(sum(risk))
    print(compute_basins(smoke_flows))
