"""
ID: mck15821
LANG: PYTHON3
PROG: ccski
"""
# Time Complexity: MN * MN * log(MN)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=380
from queue import PriorityQueue
fin = open('ccski.in', 'r')
fout = open("ccski.out", "w")
M, N = map(int, fin.readline().strip().split())
elevations = []
for _ in range(M):
    elevations.append(list(map(int, fin.readline().strip().split())))
waypoints = []
for i in range(M):
    line = list(map(int, fin.readline().strip().split()))
    for j in range(len(line)):
        if line[j] == 1:
            waypoints.append((i, j))

DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
result = 0


def bfs(source, target):
    q = PriorityQueue()
    visited = []
    for _ in range(M):
        visited.append([False for i in range(N)])
    q.put((0, source))
    while q.qsize() > 0:
        cur = q.get()
        if cur[1] == target:
            return cur[0]
        r, c = cur[1]
        visited[r][c] = True

        for dir in DIRS:
            x = r + dir[0]
            y = c + dir[1]
            if 0 <= x < M and 0 <= y < N and not visited[x][y]:
                distance = abs(elevations[x][y] - elevations[r][c])
                q.put((distance, (x, y)))


# pick 2 waypoints and update D
for i in range(len(waypoints)):
    for j in range(i + 1, len(waypoints)):
        result = max(result, bfs(waypoints[i], waypoints[j]))

fout.write(str(result))
fout.close()
