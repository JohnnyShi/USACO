"""
ID: mck15821
LANG: PYTHON3
PROG: multimoo
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=836
fin = open('multimoo.in', 'r')
fout = open("multimoo.out", "w")
N = int(fin.readline().strip())
board = []
for _ in range(N):
    board.append(list(map(int, fin.readline().strip().split())))
id_count = dict()
visited = []
for _ in range(N):
    visited.append([False] * N)
DIRS = [[0, 1], [0, -1], [-1, 0], [1, 0]]


def dfs(row, col):
    if visited[row][col]:
        return 0
    visited[row][col] = True
    count = 1
    for dir in DIRS:
        new_row = row + dir[0]
        new_col = col + dir[1]
        if 0 <= new_row < N and 0 <= new_col < N and board[new_row][new_col] == board[row][col] and not visited[new_row][new_col]:
            count += dfs(new_row, new_col)
    return count


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if board[i][j] not in id_count:
                id_count[board[i][j]] = []
            id_count[board[i][j]].append(dfs(i, j))


single_max = 0
sum_max_1 = 0
sum_max_2 = 0
# Find single max
for _, v in id_count.items():
    single_max = max(single_max, max(v))
    id_sum = sum(v)
    if sum_max_1 <= id_sum:
        sum_max_2 = sum_max_1
        sum_max_1 = id_sum
    elif sum_max_2 < id_sum:
        sum_max_2 = id_sum

fout.write(f"{single_max}\n")
fout.write(f"{sum_max_1 + sum_max_2}\n")
fout.close()
