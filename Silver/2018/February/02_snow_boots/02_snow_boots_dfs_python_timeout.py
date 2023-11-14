"""
ID: mck15821
LANG: PYTHON3
PROG: snowboots
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=811
import sys
sys.setrecursionlimit(10**5)
fin = open('snowboots.in', 'r')
fout = open("snowboots.out", "w")
N, B = map(int, fin.readline().strip().split())
depth = list(map(int, fin.readline().strip().split()))
boots = []
for _ in range(B):
    d, s = map(int, fin.readline().strip().split())
    boots.append((d, s))

max_boots = [B]
visited = []
for i in range(N):
    visited.append([False] * B)


def dfs(location, index):
    if visited[location][index]:
        return
    visited[location][index] = True

    if location == N - 1:
        max_boots[0] = min(max_boots[0], index)
        return

    for i in range(index, B):
        top_depth, top_size = boots[i]
        # continue switch boots
        if top_depth < depth[location]:
            continue
        # use current top boot
        for new_location in range(location + top_size, location, -1):
            if new_location <= N - 1 and depth[new_location] <= top_depth:
                dfs(new_location, i)


# take boots on the top
dfs(0, 0)
fout.write(f"{max_boots[0]}")
fout.close()
