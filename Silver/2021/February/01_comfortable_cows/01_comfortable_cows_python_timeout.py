"""
ID: mck15821
LANG: PYTHON3
PROG: Comfortable Cows
"""
import sys
sys.setrecursionlimit(10**7)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1110
N = int(input())
DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cows = []
counts = []
# 1001 to accommodate 0 - 1000, then 500 to the left and 500 to the right
length = 2001
for i in range(length):
    cows.append([False] * length)
    counts.append([0] * length)
answer = [0]


def fill_neighbors(r, c):
    for dir in DIRS:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if 0 <= new_r < length and 0 <= new_c < length:
            add(new_r, new_c)


def add(r, c):
    if cows[r][c]:
        return
    answer[0] += 1
    cows[r][c] = True
    # if (r, c) is comfortable then add 1 more cow
    if counts[r][c] == 3:
        fill_neighbors(r, c)

    # Adding a cow may affect cows nearby
    for dir in DIRS:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if 0 <= new_r < length and 0 <= new_c < length:
            counts[new_r][new_c] += 1
            if cows[new_r][new_c] and counts[new_r][new_c] == 3:
                fill_neighbors(new_r, new_c)


for _ in range(N):
    r, c = tuple(map(int, input().split()))
    add(r + 500, c + 500)
    answer[0] -= 1  # If only add one cow, then no extra cow added
    print(answer[0])
