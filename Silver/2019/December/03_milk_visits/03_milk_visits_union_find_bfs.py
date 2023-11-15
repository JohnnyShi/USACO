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
ids = [0] * (N + 1)
id_to_preference = dict()

graph = dict()
for i in range(N + 1):
    graph[i] = []
for _ in range(N - 1):
    p, q = map(int, (fin.readline().strip().split()))
    graph[p].append(q)
    graph[q].append(p)


def dfs(farm, prev_preference, id):
    # visited
    if ids[farm] > 0:
        return
    if cow_type[farm - 1] != prev_preference:
        return
    ids[farm] = id
    for next in graph[farm]:
        if ids[next] == 0:
            dfs(next, prev_preference, id)


def bfs(farm, id):
    q = [farm]
    while len(q) > 0:
        cur = q.pop(0)
        if ids[cur] > 0:
            continue
        ids[cur] = id
        for next in graph[cur]:
            if ids[next] == 0 and cow_type[farm - 1] == cow_type[next - 1]:
                q.append(next)


id = 1
for i in range(1, N + 1):
    bfs(i, id)
    id_to_preference[id] = cow_type[i - 1]
    id += 1

for _ in range(M):
    s, e, p = fin.readline().strip().split()
    s = int(s)
    e = int(e)
    if ids[s] != ids[e]:
        fout.write("1")
    else:
        if p == id_to_preference[s]:
            fout.write("1")
        else:
            fout.write("0")
fout.close()
