"""
ID: mck15821
LANG: PYTHON3
PROG: Cowntagion
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1062
import math
N = int(input())

graph = dict()
for i in range(N):
    graph[i] = []
for _ in range(N - 1):
    p, q = map(int, input().strip().split())
    graph[p - 1].append(q - 1)
    graph[q - 1].append(p - 1)


def bfs(start):
    q = [start]
    total_days = 0
    visited = [False] * N
    while len(q) > 0:
        cur = q.pop(0)
        if visited[cur]:
            continue
        visited[cur] = True
        neighbor_count = 0
        for neighbor in graph[cur]:
            if not visited[neighbor]:
                neighbor_count += 1
                q.append(neighbor)
        grow_days = math.log(neighbor_count + 1, 2)  # include itself
        grow_days = int(grow_days) + (int(grow_days) != grow_days)
        total_days += grow_days + neighbor_count  # grow days and time to move to neighbors
    return total_days


print(bfs(0))
