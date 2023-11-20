"""
ID: mck15821
LANG: PYTHON3
PROG: clocktree
"""
import sys
sys.setrecursionlimit(10**9)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1016
fin = open('clocktree.in', 'r')
fout = open("clocktree.out", "w")
N = int(fin.readline().strip())
clocks = list(map(int, fin.readline().strip().split()))
paths = []
for _ in range(N):
    paths.append([])
for _ in range(N - 1):
    a, b = map(int, fin.readline().strip().split())
    paths[a - 1].append(b - 1)
    paths[b - 1].append(a - 1)

# 3 questions:
# 1. Why use color algorithm to mark as 2 colors?
# 2. How to decide where to start?
# 3. How many start point available?

# Q1:
# Every clock needs to tune the adjacent n clocks; then the adjacent n clocks form a group
# As the tuning run back and forth between the center clock and neighbors,
# center increment % 12 == all neighbor increment % 12, or +-1 based on the order of start
# So every neighbor clock belongs to the same group, we can use 0-1 to mark the color

# Q2:
# If the increment of center and neighbor are equivalent, then can start anywhere
# For example: 11, 10, 11 -> 12, 10, 11 -> 12, 11, 11 -> 12, 11, 12 -> 12, 12, 12
# 10 is tuning with the first and third 11. (11 + 11) % 12 = 10, so can actually start anywhere, like:
# 11, 10, 11 -> 11, 11, 11 -> 11, 11, 12 -> 11, 12, 12 -> 12, 12, 12

# If the increment of center and neighbor has distance 1, then need to start from the bigger group
# Another example, 12, 10, 11, (12 + 11) % 12 = 11, then has to start from the group of (12, 11), like:
# 12, 10, 11 -> 12, 11, 11 -> 12, 11, 12 -> 12, 12, 12

# If distance of increment is too big then cannot tune

# Q3:
# Anypoint belongs to the same color group can start


def dfs(current, color, parent):
    if color == 0:
        clock_0_sum[0] += clocks[current]
        clock_0_count[0] += 1
    else:
        clock_1_sum[0] += clocks[current]
        clock_1_count[0] += 1
    for next in paths[current]:
        if next != parent:
            dfs(next, 1 - color, current)


clock_0_sum, clock_1_sum, clock_0_count, clock_1_count = [0], [0], [0], [0]
dfs(0, 0, -1)

if (clock_0_sum[0] % 12) == (clock_1_sum[0] % 12):
    fout.write(str(N))
elif ((clock_0_sum[0] + 1) % 12) == (clock_1_sum[0] % 12):  # color 1 is the bigger group
    fout.write(str(clock_1_count[0]))
elif (clock_0_sum[0] % 12) == ((clock_1_sum[0] + 1) % 12):  # color 0 is the bigger group
    fout.write(str(clock_0_count[0]))
else:
    fout.write("0")
fout.close()
