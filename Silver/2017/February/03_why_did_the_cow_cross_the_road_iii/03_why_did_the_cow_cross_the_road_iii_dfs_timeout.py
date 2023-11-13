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


def can_reach_without_cross(source, target, visited):
    if source == target:
        return True
    r, c = source
    if visited[r][c]:
        return False
    visited[r][c] = True
    for dir in DIRS:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if 0 < new_r <= N and 0 < new_c <= N and not visited[new_r][new_c]:
            if ((r, c), (new_r, new_c)) in roads or ((new_r, new_c), (r, c)) in roads:
                continue
            if can_reach_without_cross((new_r, new_c), target, visited):
                return True
    return False


pair_count = 0
for i in range(K):
    for j in range(i + 1, K):
        visited = []
        for _ in range(N + 1):
            visited.append([False] * (N + 1))
        if not can_reach_without_cross(locations[i], locations[j], visited):
            pair_count += 1
fout.write(f"{pair_count}")
fout.close()
