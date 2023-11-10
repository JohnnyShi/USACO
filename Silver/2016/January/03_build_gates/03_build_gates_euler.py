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
x, y = 0, 0
last_x, last_y = 0, 0
edges, vertices = set(), set()
vertices.add((x, y))

for ch in fin.readline().strip():
    last_x, last_y = x, y
    if ch == "N":
        y += 1
    elif ch == "S":
        y -= 1
    elif ch == "E":
        x += 1
    elif ch == "W":
        x -= 1
    vertices.add((x, y))
    if ch == "N" or ch == "E":
        edges.add(((last_x, last_y), (x, y)))
    else:
        edges.add(((x, y), (last_x, last_y)))
# V - E + F = 2 => F = 2 - V + E
fout.write(str(2 - len(vertices) + len(edges) - 1))
fout.close()
