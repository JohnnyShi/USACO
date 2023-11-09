"""
ID: mck15821
LANG: PYTHON3
PROG: ccski
"""
# Time Complexity: MN * log(10**9)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=380
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


def reachable(d, start_point):
    q = [start_point]
    visited = []
    for _ in range(M):
        visited.append([False for i in range(N)])
    while len(q) > 0:
        r, c = q.pop(0)
        if visited[r][c]:
            continue
        visited[r][c] = True

        for dir in DIRS:
            x = r + dir[0]
            y = c + dir[1]
            if 0 <= x < M and 0 <= y < N and not visited[x][y]:
                if abs(elevations[x][y] - elevations[r][c]) <= d:
                    q.append((x, y))
    for waypoint in waypoints:
        if not visited[waypoint[0]][waypoint[1]]:
            return False
    return True


left, right = 0, 10**9
while left < right:
    mid = (left + right) // 2
    print(mid)
    if reachable(mid, waypoints[0]):
        right = mid
    else:
        left = mid + 1


fout.write(str(left))
fout.close()
