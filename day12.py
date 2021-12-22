import sys
import collections
filename = sys.argv[1]

def dfs(graph, node, path, paths, visited):
    if node == "end":
        paths.append(path.copy())
    else:
        if node.islower():
            visited[node] = True
        for neigh in graph[node]:
            if not visited[neigh]:
                path.append(neigh)
                dfs(graph, neigh, path, paths, visited)
                path.pop()

        visited[node] = False

def dfs_partb(graph, node, path, paths, visited):
    if node == "end":
        paths.append(path.copy())
    else:
        if node.islower():
            visited[node] += 1
        for neigh in graph[node]:
            # print(visited)
            if neigh.islower() and visited[neigh] == 1 and (2 not in visited.values()):
                path.append(neigh)
                dfs_partb(graph, neigh, path, paths, visited)
                path.pop()
            if visited[neigh] == 0:
                path.append(neigh)
                dfs_partb(graph, neigh, path, paths, visited)
                path.pop()

        if node.islower():
            visited[node] -= 1

with open(filename) as file:
    lines = file.readlines()
    edges = [line.rstrip().split("-") for line in lines]
    graph = collections.defaultdict(set)
    for edge in edges: # build the graph
        src = edge[0]
        dest = edge[1]
        graph[src].add(dest)
        graph[dest].add(src)

    visited = collections.defaultdict(bool)
    paths = []
    visited['start'] = True
    dfs(graph, 'start', ['start'], paths, visited)
    # print(paths)
    print(len(paths))

    visited = collections.defaultdict(int)
    paths = []
    visited['start'] = 3
    dfs_partb(graph, 'start', ['start'], paths, visited)
    print(len(paths))
