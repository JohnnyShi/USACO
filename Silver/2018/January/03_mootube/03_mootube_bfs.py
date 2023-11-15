"""
ID: mck15821
LANG: PYTHON3
PROG: Mootube
"""
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


def bfs(origin, threshold):
    visited = [False] * N
    q = [origin]
    while len(q) > 0:
        cur = q.pop(0)
        if visited[cur]:
            continue
        visited[cur] = True
        for next in graph[cur]:
            if threshold <= next[1] and not visited[next[0]]:
                q.append(next[0])
    return sum(visited) - 1


for i in range(Q):
    k, v = map(int, (fin.readline().strip().split()))
    total = bfs(v - 1, k)
    fout.write(f"{total}\n")
fout.close()
