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
rooms = []
for i in range(N + 1):
    rooms.append([False] * (N + 1))
graph = dict()
for _ in range(M):
    source_r, source_c, target_r, target_c = map(int, fin.readline().strip().split())
    if (source_r, source_c) not in graph:
        graph[(source_r, source_c)] = []
    graph[(source_r, source_c)].append((target_r, target_c))
DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
keys = set()


def light_up(r, c, rooms):
    if rooms[r][c]:
        return
    rooms[r][c] = True
    if (r, c) in graph:
        for next in graph[(r, c)]:
            light_up(next[0], next[1], rooms)


def navigate(r, c, rooms, visited):
    if visited[r][c] or not rooms[r][c]:
        return 0
    count = 1
    visited[r][c] = True
    for dir in DIRS:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if 1 <= new_r <= N and 1 <= new_c <= N:
            count += navigate(new_r, new_c, rooms, visited)
    return count


light_up(1, 1, rooms)

visited = []
for i in range(N + 1):
    visited.append([False] * (N + 1))
fout.write(f"{navigate(1, 1, rooms, visited)}")
fout.close()
