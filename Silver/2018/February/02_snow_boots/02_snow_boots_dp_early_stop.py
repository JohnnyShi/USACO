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
cache = []
for i in range(N):
    cache.append([0] * B)
cache[0][0] = 1

for b in range(B):
    top_depth, top_size = boots[b]
    for location in range(N):
        if depth[location] > top_depth:
            cache[location][b] = -1
            continue
        for prior_location in range(location):
            if cache[prior_location][b] == 1 and prior_location + top_size >= location:
                cache[location][b] = 1
        for prior_boot in range(b):
            if cache[location][prior_boot] == 1:
                cache[location][b] = 1
    if cache[N - 1][b] == 1:
        fout.write(f"{b}")
        fout.close()
        exit(0)
