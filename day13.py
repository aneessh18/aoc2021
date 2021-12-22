import sys

filename = sys.argv[1]
# num_folds = int(sys.argv[2])

with open(filename) as file:

    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    points = []
    i = 0
    while lines[i] != "":
        # print(lines[i].split(","))
        points.append(tuple(map(int, lines[i].split(","))))
        i += 1
    folds = []
    i += 1
    while i<len(lines):
        folds.append(lines[i].split(" ")[2].split("="))
        i += 1

    # print(points)
    # print(folds)
    for num_fold in range(len(folds)):
        direc, magnitude = folds[num_fold][0], int(folds[num_fold][1])
        print(direc, magnitude)
        points_snapshots = points.copy()
        for i, (x, y) in enumerate(points):
            # print(i)
            if direc == 'y' and y>magnitude:
                points_snapshots[i] = (points_snapshots[i][0],2*magnitude-points_snapshots[i][1])
            elif direc == 'x' and x>magnitude:
                points_snapshots[i] = (2*magnitude-points_snapshots[i][0], points_snapshots[i][1])

        points = list(set(points_snapshots))
    print(points)
    x_max= max(points, key=lambda p:p[0])[0]
    y_max= max(points,key= lambda p:p[1])[1]
    print(x_max)
    thermal_map = [['#' if (i,j) in points else '.' for j in range(y_max+1)] for i in range(x_max+1)]
    for i in range(x_max+1):
        print(thermal_map[i])
    print(len(points))
