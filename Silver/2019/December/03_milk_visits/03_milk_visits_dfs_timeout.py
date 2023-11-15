"""
ID: mck15821
LANG: PYTHON3
PROG: milkvisits
"""
import sys
sys.setrecursionlimit(10**5)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=968
fin = open('milkvisits.in', 'r')
fout = open("milkvisits.out", "w")
N, M = map(int, (fin.readline().strip().split()))
cow_type = fin.readline().strip()

graph = dict()
for i in range(N + 1):
    graph[i] = []
for _ in range(N - 1):
    p, q = map(int, (fin.readline().strip().split()))
    graph[p].append(q)
    graph[q].append(p)


def dfs(current, end, visited, preference, satisfied):
    if visited[current]:
        return False
    visited[current] = True
    if cow_type[current - 1] == preference:
        satisfied = True
    if current == end:
        return satisfied
    for next in graph[current]:
        if not visited[next]:
            if dfs(next, end, visited, preference, satisfied):
                return True
    return False


for _ in range(M):
    s, e, p = fin.readline().strip().split()
    s = int(s)
    e = int(e)
    visited = [False] * (N + 1)
    fout.write(f"{int(dfs(s, e, visited, p, False))}")
fout.close()
