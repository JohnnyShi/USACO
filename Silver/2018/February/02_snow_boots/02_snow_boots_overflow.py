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

max_boots = [0]


def dfs(location, boots):
    # Use current top boot
    while len(boots) > 0:
        top_depth, top_size = boots[0]
        # use current top boot
        for new_location in range(location + top_size, location - 1, -1):
            if new_location >= N - 1:
                max_boots[0] = max(max_boots[0], len(boots))
                return
            if depth[new_location] <= top_depth:
                dfs(new_location, boots.copy())
        # drop the top boot
        boots.pop(0)


# take boots on the top
dfs(0, boots.copy())
fout.write(f"{len(boots) - max_boots[0]}")
fout.close()
