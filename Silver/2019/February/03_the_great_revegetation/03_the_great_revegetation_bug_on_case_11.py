"""
ID: mck15821
LANG: PYTHON3
PROG: revegetate
"""
import sys
sys.setrecursionlimit(10**5)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=920
fin = open('revegetate.in', 'r')
fout = open("revegetate.out", "w")
N, M = map(int, fin.readline().strip().split())
graph = []
for _ in range(N):
    graph.append([])
for _ in range(M):
    ch, a, b = fin.readline().strip().split()
    a = int(a) - 1
    b = int(b) - 1
    graph[a].append((b, ch))
    graph[b].append((a, ch))

visited = [False] * N


def dfs(current):
    if visited[current]:
        return
    visited[current] = True
    for next in graph[current]:
        if not visited[next[0]]:
            dfs(next[0])


count = 0
for i in range(N):
    if not visited[i]:
        dfs(i)
        count += 1

result = 2 ** (N - sum(visited)) * 2 ** count

# to binary
fout.write('{0:b}'.format(result))
fout.close()
