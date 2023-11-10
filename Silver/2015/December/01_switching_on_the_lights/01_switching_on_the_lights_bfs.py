"""
ID: mck15821
LANG: PYTHON3
PROG: lightson
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=570
fin = open('lightson.in', 'r')
fout = open("lightson.out", "w")
N, M = map(int, fin.readline().strip().split())
graph = dict()
for _ in range(M):
    source_r, source_c, target_r, target_c = map(int, fin.readline().strip().split())
    if (source_r, source_c) not in graph:
        graph[(source_r, source_c)] = set()
    graph[(source_r, source_c)].add((target_r, target_c))
DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
can_reach = set()
lighted = set()
visited = set()
lighted.add((1, 1))
can_reach.add((1, 1))

q = [(1, 1)]
while len(q) > 0:
    r, c = q.pop(0)
    if (r, c) in visited:
        continue
    visited.add((r, c))
    # turn the light on
    if (r, c) in graph:
        for next in graph[(r, c)]:
            lighted.add(next)

    # Expand
    for dir in DIRS:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if 1 <= new_r <= N and 1 <= new_c <= N and (new_r, new_c) not in visited:
            can_reach.add((new_r, new_c))

    for next in can_reach.intersection(lighted):
        if next not in visited and next not in q:
            q.append(next)


fout.write(f"{len(lighted)}")
fout.close()
