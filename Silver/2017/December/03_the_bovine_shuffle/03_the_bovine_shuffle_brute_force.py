"""
ID: mck15821
LANG: PYTHON3
PROG: shuffle
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=764
fin = open('shuffle.in', 'r')
fout = open("shuffle.out", "w")
N = int(fin.readline().strip())
shuffles = list(map(int, fin.readline().strip().split()))
shuffles.insert(0, 0)  # match 1-base index


def find_cycle(start):
    q = [start]
    cur = start
    visited = [False] * (N + 1)
    while len(q) > 0:
        cur = q.pop(0)
        # Found an existed cycle, this start point cannot be a cycle
        if in_cycle[cur]:
            return 0
        if visited[cur]:
            break
        visited[cur] = True
        q.append(shuffles[cur])
    # Mark cycle
    start = cur
    count = 0
    while True:
        in_cycle[start] = True
        start = shuffles[start]
        count += 1
        if start == cur:
            return count


result = 0
in_cycle = [False] * (N + 1)
# Find cycle and the length of all cycles are the answer
for i in range(1, N + 1):
    if not in_cycle[i]:
        result += find_cycle(i)

fout.write(str(result))
fout.close()
