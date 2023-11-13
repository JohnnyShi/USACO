"""
ID: mck15821
LANG: PYTHON3
PROG: mooyomooyo
"""
import copy
# http://www.usaco.org/index.php?page=viewproblem2&cpid=860
fin = open('mooyomooyo.in', 'r')
fout = open("mooyomooyo.out", "w")
N, K = map(int, fin.readline().strip().split())
boards = []
for _ in range(N):
    boards.append(list(fin.readline().strip()))
DIRS = [[0, -1], [0, 1], [-1, 0], [1, 0]]


def bfs_count_reaches_k(start_r, start_c, new_boards):
    number = new_boards[start_r][start_c]
    q = [(start_r, start_c)]
    new_visited = []
    for _ in range(N):
        new_visited.append([False] * 10)
    count = 0
    # count consecution
    while len(q) > 0:
        r, c = q.pop(0)
        if new_visited[r][c]:
            continue
        new_visited[r][c] = True
        count += 1
        if count == K:
            return True
        for dir in DIRS:
            new_r = r + dir[0]
            new_c = c + dir[1]
            if 0 <= new_r < N and 0 <= new_c < 10 and not new_visited[new_r][new_c] and new_boards[new_r][new_c] == number:
                q.append((new_r, new_c))
    return False


def transform(start_r, start_c, visited, new_boards):
    number = new_boards[start_r][start_c]
    q = [(start_r, start_c)]
    while len(q) > 0:
        r, c = q.pop(0)
        if visited[r][c]:
            continue
        visited[r][c] = True
        new_boards[r][c] = "0"
        for dir in DIRS:
            new_r = r + dir[0]
            new_c = c + dir[1]
            if 0 <= new_r < N and 0 <= new_c < 10 and not visited[new_r][new_c] and new_boards[new_r][new_c] == number:
                q.append((new_r, new_c))


def mark_visited(start_r, start_c, visited, new_boards):
    number = new_boards[start_r][start_c]
    q = [(start_r, start_c)]
    while len(q) > 0:
        r, c = q.pop(0)
        if visited[r][c]:
            continue
        visited[r][c] = True
        for dir in DIRS:
            new_r = r + dir[0]
            new_c = c + dir[1]
            if 0 <= new_r < N and 0 <= new_c < 10 and not visited[new_r][new_c] and new_boards[new_r][new_c] == number:
                q.append((new_r, new_c))


def bfs_count_and_transform(start_r, start_c, visited, new_boards):
    if bfs_count_reaches_k(start_r, start_c, new_boards):
        transform(start_r, start_c, visited, new_boards)
    else:
        mark_visited(start_r, start_c, visited, new_boards)


def apply_gravity(boards):
    for j in range(10):
        k = N - 1
        for i in range(N - 1, -1, -1):
            if boards[i][j] != "0":
                boards[k][j] = boards[i][j]
                k -= 1
        for i in range(k, -1, -1):
            boards[i][j] = "0"


while True:
    new_boards = copy.deepcopy(boards)
    visited = []
    for i in range(N):
        visited.append([False] * 10)
    for i in range(N):
        for j in range(10):
            if (not visited[i][j]) and new_boards[i][j] != "0":
                bfs_count_and_transform(i, j, visited, new_boards)
    apply_gravity(new_boards)
    if boards == new_boards:
        break
    boards = new_boards

for line in boards:
    fout.write(f"{''.join(line)}\n")
fout.close()
