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

locations = set()
for _ in range(K):
    loc = tuple(map(int, fin.readline().strip().split()))
    locations.add(loc)

DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def get_region_count(source, visited):
    q = [source]
    count = 0
    while len(q) > 0:
        r, c = q.pop(0)
        if visited[r][c]:
            continue
        visited[r][c] = True
        if (r, c) in locations:
            count += 1
        for dir in DIRS:
            new_r = r + dir[0]
            new_c = c + dir[1]
            if 0 < new_r <= N and 0 < new_c <= N and not visited[new_r][new_c]:
                if ((r, c), (new_r, new_c)) in roads or ((new_r, new_c), (r, c)) in roads:
                    continue
                q.append((new_r, new_c))
    return count


region_count = []
visited = []
for _ in range(N + 1):
    visited.append([False] * (N + 1))
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if not visited[i][j]:
            cow_count = get_region_count((i, j), visited)
            if cow_count != 0:
                region_count.append(cow_count)

pair_count = 0
for i in range(len(region_count)):
    for j in range(i + 1, len(region_count)):
        pair_count += region_count[i] * region_count[j]
fout.write(f"{pair_count}")
fout.close()
