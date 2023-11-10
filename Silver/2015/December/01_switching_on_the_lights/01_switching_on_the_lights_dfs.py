"""
ID: mck15821
LANG: PYTHON3
PROG: lightson
"""
import sys
sys.setrecursionlimit(10**7)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=570
fin = open('lightson.in', 'r')
fout = open("lightson.out", "w")
N, M = map(int, fin.readline().strip().split())
graph = dict()
for _ in range(M):
    source_r, source_c, target_r, target_c = map(int, fin.readline().strip().split())
    if (source_r, source_c) not in graph:
        graph[(source_r, source_c)] = set()
    graph[(source_r, source_c)].add((target_r, target_c))
DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
can_reach = set()
lighted = set()
visited = set()
can_reach.add((1, 1))
lighted.add((1, 1))


def dfs(r, c, visited, can_reach, lighted):
    if (r, c) in visited:
        return
    visited.add((r, c))

    # Turn on the light first
    if (r, c) in graph:
        for light in graph[(r, c)]:
            lighted.add(light)

    # Expand reachable space
    for dir in DIRS:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if 1 <= new_r <= N and 1 <= new_c <= N:
            can_reach.add((new_r, new_c))

    for next in can_reach.intersection(lighted):
        if next not in visited:
            dfs(next[0], next[1], visited, can_reach, lighted)


dfs(1, 1, visited, can_reach, lighted)
fout.write(f"{len(lighted)}")
fout.close()
