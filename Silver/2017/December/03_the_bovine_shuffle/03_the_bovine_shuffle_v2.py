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

visited = [False] * (N + 1)


def mark_cycle(start):
    q = [shuffles[start]]
    while len(q) > 0:
        cur = q.pop(0)
        visited[cur] = 1
        if cur == start:
            return
        q.append(shuffles[cur])


def mark_non_cycle(current, target):
    if current == target:
        return
    visited[current] = -1
    mark_non_cycle(shuffles[current], target)


def find_cycle(start):
    q = [start]
    distance = dict()
    length = 0
    cur = start
    while len(q) > 0:
        cur = q.pop(0)
        # already processed
        if visited[cur] != 0:
            return 0
        # found a new cycle
        if cur in distance:
            # mark the pos that's not cycle
            mark_non_cycle(start, cur)
            # mark the pos that's cycle
            mark_cycle(cur)
            return length - distance[cur]
        distance[cur] = length
        length += 1
        # if shuffles[cur] not in distance:
        q.append(shuffles[cur])
    mark_non_cycle(start, cur)
    return 0


result = 0
# Find cycle and the length of all cycles are the answer
for i in range(1, N + 1):
    if visited[i] == 0:
        result += find_cycle(i)

fout.write(str(result))
fout.close()
