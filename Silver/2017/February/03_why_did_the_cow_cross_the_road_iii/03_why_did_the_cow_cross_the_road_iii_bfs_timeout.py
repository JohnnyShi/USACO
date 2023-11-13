"""
ID: mck15821
LANG: PYTHON3
PROG: countcross
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=716
fin = open('countcross.in', 'r')
fout = open("countcross.out", "w")
N, K, R = map(int, fin.readline().strip().split())
roads = set()
for _ in range(R):
    r1, c1, r2, c2 = map(int, fin.readline().strip().split())
    road = ((r1, c1), (r2, c2))
    roads.add(road)

locations = []
for _ in range(K):
    loc = tuple(map(int, fin.readline().strip().split()))
    locations.append(loc)

DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def can_reach_without_cross(source, target):
    visited = []
    for _ in range(N + 1):
        visited.append([False] * (N + 1))
    q = [source]
    while len(q) > 0:
        r, c = q.pop(0)
        if (r, c) == target:
            return True
        if visited[r][c]:
            continue
        visited[r][c] = True
        for dir in DIRS:
            new_r = r + dir[0]
            new_c = c + dir[1]
            if 0 < new_r <= N and 0 < new_c <= N and not visited[new_r][new_c]:
                if ((r, c), (new_r, new_c)) in roads or ((new_r, new_c), (r, c)) in roads:
                    continue
                q.append((new_r, new_c))
    return False


pair_count = 0
for i in range(K):
    for j in range(i + 1, K):
        if not can_reach_without_cross(locations[i], locations[j]):
            pair_count += 1
fout.write(f"{pair_count}")
fout.close()
