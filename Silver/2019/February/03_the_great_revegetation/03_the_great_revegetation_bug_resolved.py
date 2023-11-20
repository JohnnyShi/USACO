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

visited = [0] * N


def dfs(current, flag):
    if visited[current] != 0:
        if visited[current] != flag:
            fout.write(str(0))
            exit()
        return

    visited[current] = flag
    for next in graph[current]:
        if next[1] == "S":
            dfs(next[0], flag)
        else:
            dfs(next[0], -flag)



count = 0
for i in range(N):
    if visited[i] == 0:
        dfs(i, 1)
        count += 1
print(visited)

result = 2 ** (visited.count(0)) * 2 ** count

# to binary
fout.write('{0:b}'.format(result))
fout.close()
