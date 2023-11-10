"""
ID: mck15821
LANG: PYTHON3
PROG: gates
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=596
import sys
sys.setrecursionlimit(10**5)
fin = open('gates.in', 'r')
fout = open("gates.out", "w")

N = int(fin.readline().strip())
pos = (0, 0)
paths = set()
paths.add(pos)
for c in fin.readline().strip():
    if c == "N":
        pos = (pos[0], pos[1] + 1)
    elif c == "S":
        pos = (pos[0], pos[1] - 1)
    elif c == "W":
        pos = (pos[0] - 1, pos[1])
    else:
        pos = (pos[0] + 1, pos[1])
    paths.add(pos)
print(paths)
# map = []
# for i in range(21):
#     map.append([0] * 21)
# for p in paths:
#     map[p[0] + 10][p[1] + 10] = 1
# for line in map:
#     print(line)


DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(r, c, last_r, last_c, visited_point, visited_edge):
    print(r, c)
    edge = ((last_r, last_c), (r, c))
    reverse_edge = ((r, c), (last_r, last_c))
    if (edge in visited_edge) or (reverse_edge in visited_edge):
        return
    visited_edge.add(edge)
    if (r, c) in visited_point:
        count[0] += 1
        print("count + 1")
        return
    visited_point.add((r, c))
    for dir in DIRS:
        x = r + dir[0]
        y = c + dir[1]
        if (x, y) in paths and (x, y) != (last_r, last_c):
            dfs(x, y, r, c, visited_point, visited_edge)

count = [0]
visited_edge = set()
visited_point = set()
dfs(0, 0, 0, 0, visited_point, visited_edge)
fout.write(str(count[0]))
fout.close()
