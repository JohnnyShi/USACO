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

relevance = []
for i in range(N):
    relevance.append([0] * N)

graph = dict()
for i in range(N):
    graph[i] = []
for i in range(N - 1):
    p, q, r = map(int, (fin.readline().strip().split()))
    graph[p - 1].append((q - 1, r))
    graph[q - 1].append((p - 1, r))


def dfs(start, end, r):
    # already visited
    if relevance[start][end] > 0:
        return
    relevance[start][end] = r
    for next in graph[end]:
        if start != next[0]:
            dfs(start, next[0], min(r, next[1]))


# build relevance matrix
for i in range(N):
    for next in graph[i]:
        dfs(i, next[0], next[1])

for i in range(Q):
    k, v = map(int, (fin.readline().strip().split()))
    count = 0
    for i in range(N):
        if relevance[v - 1][i] >= k:
            count += 1
    fout.write(f"{count}\n")
fout.close()
