"""
ID: mck15821
LANG: PYTHON3
PROG: Mootube
"""
import sys
sys.setrecursionlimit(10**5)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=788
fin = open('mootube.in', 'r')
fout = open("mootube.out", "w")
N, Q = map(int, (fin.readline().strip().split()))

graph = dict()
for i in range(N):
    graph[i] = []
for i in range(N - 1):
    p, q, r = map(int, (fin.readline().strip().split()))
    graph[p - 1].append((q - 1, r))
    graph[q - 1].append((p - 1, r))


def dfs(origin, current, threshold, visited):
    if visited[current]:
        return 0
    visited[current] = True
    count = int(current != origin)
    for next in graph[current]:
        if threshold <= next[1] and not visited[next[0]]:
            count += dfs(origin, next[0], threshold, visited)
    return count


for i in range(Q):
    k, v = map(int, (fin.readline().strip().split()))
    visited = [False] * N
    total = dfs(v - 1, v - 1, k, visited)
    fout.write(f"{total}\n")
fout.close()
