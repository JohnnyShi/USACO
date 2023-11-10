"""
ID: mck15821
LANG: PYTHON3
PROG: gates
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=596
import sys
sys.setrecursionlimit(10**7)
fin = open('gates.in', 'r')
fout = open("gates.out", "w")

N = int(fin.readline().strip())
path = fin.readline().strip()
r, c = 2001, 2001  # change to 1002 to pass the time limit
min_r, max_r, min_c, max_c = 2001, 2001, 2001, 2001  # change to 1002 to pass the time limit
DIRS = {
    "N": [-1, 0],
    "S": [1, 0],
    "W": [0, -1],
    "E": [0, 1]
}

fence, visited = [], []
for _ in range(4003):  # change to 2005 to pass the time limit
    fence.append([False for i in range(4003)])  # change to 2005 to pass the time limit
    visited.append([False for i in range(4003)])  # change to 2005 to pass the time limit

# Mark fences, scaling to 2 units
for ch in path:
    fence[r + DIRS[ch][0]][c + DIRS[ch][1]] = True
    fence[r + 2 * DIRS[ch][0]][c + 2 * DIRS[ch][1]] = True
    r += 2 * DIRS[ch][0]
    c += 2 * DIRS[ch][1]
    min_r = min(min_r, r)
    max_r = max(max_r, r)
    min_c = min(min_c, c)
    max_c = max(max_c, c)
min_r -= 1
max_r += 1
min_c -= 1
max_c += 1


def flood_fill(r, c):
    if visited[r][c] or fence[r][c]:
        return
    visited[r][c] = True
    for dir in DIRS.values():
        x = r + dir[0]
        y = c + dir[1]
        if min_r <= x <= max_r and min_c <= y <= max_c:
            flood_fill(x, y)


# expand 1 unit to include the edge in flood fill
result = 0
for i in range(min_r, max_r + 1):
    for j in range(min_c, max_c + 1):
        if not visited[i][j] and not fence[i][j]:
            flood_fill(i, j)
            result += 1

fout.write(f"{result - 1}\n")
fout.close()
