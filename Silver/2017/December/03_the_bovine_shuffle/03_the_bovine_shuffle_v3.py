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


def mark(start, target):
    q = [start]
    first_time = True
    while len(q) > 0:
        cur = q.pop(0)
        if cur == target:
            if not first_time:
                return
            first_time = not first_time
        visited[cur] = True
        q.append(shuffles[cur])


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
            mark(start, cur)
            return length - distance[cur]
        distance[cur] = length
        length += 1
        # if shuffles[cur] not in distance:
        q.append(shuffles[cur])
    mark(start, cur)
    return 0


result = 0
# Find cycle and the length of all cycles are the answer
for i in range(1, N + 1):
    if not visited[i]:
        result += find_cycle(i)

fout.write(str(result))
fout.close()
