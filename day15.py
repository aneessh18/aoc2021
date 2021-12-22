import collections
import sys
import heapq

filename = sys.argv[1]


class DistNode:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.b < other.b

    def __str__(self):
        return f"{self.a}{self.b}"


def dijkstra(weights):
    n, m = len(weights), len(weights[0])

    def encode(i, j):
        return i * n + j

    def decode(pos):
        return pos // n, pos % m

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    priority_queue = []
    heapq.heappush(priority_queue, DistNode(encode(0, 0), 0))
    visited = collections.defaultdict(bool)
    visited[0] = True

    distance = collections.defaultdict(int)
    c = 0
    while len(priority_queue) != 0:

        direcs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        top = heapq.heappop(priority_queue)
        node, dis = top.a, top.b
        # print("c",node)
        i, j = decode(node)
        for direc in direcs:
            x1 = direc[0] + i
            y1 = direc[1] + j
            neigh_node = encode(x1, y1)
            if is_valid(x1, y1) and not visited[neigh_node]:
                # print("n",neigh_node)
                visited[neigh_node] = True

                distance[neigh_node] = dis + weights[x1][y1]
                heapq.heappush(priority_queue, DistNode(neigh_node, distance[neigh_node]))
        c += 1
        # nodes_in_queue = [node.a for node in priority_queue]
        # print(nodes_in_queue)

    # print(distance)
    return distance[encode(n - 1, m - 1)]


with open(filename) as file:
    lines = [line.rstrip() for line in file.readlines()]
    weights = [list(map(int, list(line))) for line in lines]
    # print(weights)
    print(dijkstra(weights))
    n, m = len(weights), len(weights[0])

    new_weights = [[0 for j in range(5 * m)] for i in range(5 * n)]
    for i in range(5 * n):
        for j in range(m):
            # print(i, j)
            if i < n:
                new_weights[i][j] = weights[i][j]
            else:
                # print(i,j , i-n, j)
                new_weight = new_weights[i - n][j] + 1
                new_weights[i][j] = 9 if new_weight == 9 else new_weight % 9

    for j in range(m, 5 * m):
        for i in range(5 * n):
            new_weight = (new_weights[i][j - m] if i < n else new_weights[i][j - m]) + 1
            new_weights[i][j] = new_weight % 9 if new_weight != 9 else 9

        # print()
    print(dijkstra(new_weights))

    # dp = [[0 for j in range(m+1)] for i in range(n+1)]
    # for i in range(1,n+1):
    #     dp[i][0] = dp[i-1][0] + weights[i - 1][0]
    #
    # for j in range(1,m+1):
    #     dp[0][j] = dp[0][j-1] + weights[0][j - 1]
    #
    # for i in range(1,n+1):
    #     for j in range(1,m+1):
    #         dp[i][j] = min(dp[i-1][j], dp[i][j-1])+weights[i-1][j-1]

    # print(dp[n][m]-dp[1][1])
