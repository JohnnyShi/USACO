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


def dfs(node, threshold, visited, count):
    if visited[node]:
        return
    visited[node] = True
    count[0] += 1
    for next in graph[node]:
        if threshold <= next[1] and not visited[next[0]]:
            dfs(next[0], threshold, visited, count)


for i in range(Q):
    k, v = map(int, (fin.readline().strip().split()))
    visited = [False] * N
    visited[v - 1] = True
    count = [0]
    for next in graph[v - 1]:
        if k <= next[1] and not visited[next[0]]:
            dfs(next[0], k, visited, count)
    fout.write(f"{count[0]}\n")
fout.close()
