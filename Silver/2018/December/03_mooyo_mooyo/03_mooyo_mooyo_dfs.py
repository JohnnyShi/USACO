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


def dfs_count_reaches_k(r, c, visited, new_boards, number, counter):
    if visited[r][c]:
        return False
    visited[r][c] = True
    counter[0] -= 1
    if counter[0] == 0:
        return True
    for dir in DIRS:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if 0 <= new_r < N and 0 <= new_c < 10 and not visited[new_r][new_c] and new_boards[new_r][new_c] == number:
            if dfs_count_reaches_k(new_r, new_c, visited, new_boards, number, counter):
                return True
    return False


def transform(r, c, visited, new_boards, number):
    if visited[r][c]:
        return
    visited[r][c] = True
    new_boards[r][c] = "0"
    for dir in DIRS:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if 0 <= new_r < N and 0 <= new_c < 10 and not visited[new_r][new_c] and new_boards[new_r][new_c] == number:
            transform(new_r, new_c, visited, new_boards, number)


def mark_visited(r, c, visited, new_boards, number):
    if visited[r][c]:
        return
    visited[r][c] = True
    for dir in DIRS:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if 0 <= new_r < N and 0 <= new_c < 10 and not visited[new_r][new_c] and new_boards[new_r][new_c] == number:
            mark_visited(new_r, new_c, visited, new_boards, number)


def dfs_count_and_transform(start_r, start_c, visited, new_boards):
    new_visited = []
    for i in range(N):
        new_visited.append([False] * 10)
    if dfs_count_reaches_k(start_r, start_c, new_visited, new_boards, new_boards[start_r][start_c], [K]):
        transform(start_r, start_c, visited, new_boards, new_boards[start_r][start_c])
    else:
        mark_visited(start_r, start_c, visited, new_boards, new_boards[start_r][start_c])


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
                dfs_count_and_transform(i, j, visited, new_boards)
    apply_gravity(new_boards)
    if boards == new_boards:
        break
    boards = new_boards

for line in boards:
    fout.write(f"{''.join(line)}\n")
fout.close()
