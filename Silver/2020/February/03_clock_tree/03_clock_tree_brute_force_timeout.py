"""
ID: mck15821
LANG: PYTHON3
PROG: clocktree
"""
import sys
sys.setrecursionlimit(10**9)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1016
fin = open('clocktree.in', 'r')
fout = open("clocktree.out", "w")
N = int(fin.readline().strip())
clocks = list(map(int, fin.readline().strip().split()))
paths = []
for _ in range(N):
    paths.append([])
for _ in range(N - 1):
    a, b = map(int, fin.readline().strip().split())
    paths[a - 1].append(b - 1)
    paths[b - 1].append(a - 1)

result = 0
# at one location, state of N clocks, True or False
visited = []
for i in range(N):
    visited.append(set())


def dfs(state, location):
    print(state, location)
    if tuple(state) in visited[location]:
        return False
    visited[location].add(tuple(state))
    if state.count(0) == N:
        return True
    for neighbor in paths[location]:
        original_neighbor_value = state[neighbor]
        state[neighbor] = (state[neighbor] + 1) % 12
        if dfs(state, neighbor):
            state[neighbor] = original_neighbor_value
            return True
        state[neighbor] = original_neighbor_value
    return False


for i in range(N):
    if dfs(clocks, i):
        result += 1
fout.write(f"{result}")
fout.close()
