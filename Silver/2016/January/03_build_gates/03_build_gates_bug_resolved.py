"""
ID: mck15821
LANG: PYTHON3
PROG: gates
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=596
fin = open('gates.in', 'r')
fout = open("gates.out", "w")

N = int(fin.readline().strip())
visited_edge = set()
visited_point = set()
result = 0
x, y = 0, 0
prev_x, prev_y = 0, 0
visited_point.add((x, y))

for c in fin.readline().strip():
    prev_x, prev_y = x, y
    if c == "N":
        y += 1
    elif c == "S":
        y -= 1
    elif c == "W":
        x -= 1
    else:
        x += 1

    edge = ((prev_x, prev_y), (x, y))
    reverse_edge = ((x, y), (prev_x, prev_y))

    if edge not in visited_edge and reverse_edge not in visited_edge and (x, y) in visited_point:
        result += 1
    visited_edge.add(edge)
    visited_point.add((x, y))

fout.write(str(result))
fout.close()
