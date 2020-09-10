INFINITE_FLOW = 10000000


def bfs(C, F, s, t):
    queue = [s]
    paths = {s: []}

    if s == t:
        return paths[s]

    while queue:
        u = queue.pop(0)

        for v in range(len(C)):
            if (C[u][v] - F[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]

                if v == t:
                    return paths[v]

                queue.append(v)

    return None


def max_flow(C, s, t):
    n = len(C)

    F = [[0] * n for _ in range(n)]

    path = bfs(C, F, s, t)
    while path != None:
        flow = min(C[u][v] - F[u][v] for u, v in path)
        for u, v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = bfs(C, F, s, t)
    return sum(F[s][i] for i in range(n))


def solution(entrances, exits, path):
    # Your code here

    # Add in super source and super sink node

    source = [0] * (len(path[0]) + 2)
    sink = [0] * (len(path[0]) + 2)
    for e in entrances:
        source[e + 1] = INFINITE_FLOW

    path.insert(0, source)

    for i in range(1, len(path)):
        path[i].insert(0, 0)

        if i-1 in exits:
            path[i].append(INFINITE_FLOW)
        else:
            path[i].append(0)

    path.append(sink)
    print(path)
    return max_flow(path, 0, len(path) - 1)


print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [
      0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
