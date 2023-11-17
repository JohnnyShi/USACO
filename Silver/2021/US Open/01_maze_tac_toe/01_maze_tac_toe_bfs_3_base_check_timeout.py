"""
ID: mck15821
LANG: PYTHON3
PROG: Maze Tac Toe
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1134

M = int(input())
grids = []
for _ in range(M):
    grids.append(input())
N = len(grids[0]) // 3
final_config = set()
DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# [3^0, 3^1, 3^2, 3^3, 3^4, 3^5, 3^6, 3&7, 3^8], each digit has 0, 1 and 2 numbers
visited = []
for i in range(M):
    matrix = []
    for j in range(N):
        matrix.append([False] * (3 ** 9))
    visited.append(matrix)


# board is a 9 digit base 3 number
winning = [
    "211000000", "112000000", "000211000", "000112000", "000000211", "000000112",  # by row
    "200100100", "100100200", "020010010", "010010020", "002001001", "001001002",  # by cow
    "200010001", "100010002", "002010100", "001010200"  # by diag
]


def is_win(board):
    s = []
    for i in range(9):
        s.append(str(board % 3))
        board //= 3
    for sol in winning:
        found = True
        for i in range(9):
            if sol[i] != "0" and sol[i] != s[i]:
                found = False
                break
        if found:
            return True
    return False


def search(row: int, col: int, board: int):
    q = [(row, col, board)]
    while len(q) > 0:
        r, c, b = q.pop(0)
        if visited[r][c][b]:
            continue
        visited[r][c][b] = True

        if grids[r][c * 3] in ["M", "O"]:
            board_r = int(grids[r][c * 3 + 1]) - 1
            board_c = int(grids[r][c * 3 + 2]) - 1
            board_coordinate = board_r * 3 + board_c

            # an empty place
            if b // (3 ** board_coordinate) % 3 == 0:
                if grids[r][c * 3] == "M":
                    b += 2 * 3 ** board_coordinate
                elif grids[r][c * 3] == "O":
                    b += 3 ** board_coordinate

                if is_win(b):
                    final_config.add(b)
                    # since board is number, no need to backtrack
                    continue
                # not win, continue to explore

        # Visit neighbors
        for dir in DIRS:
            new_r = r + dir[0]
            new_c = c + dir[1]
            if 0 <= new_r < M and 0 <= new_c < N and grids[new_r][new_c * 3] != "#" and not visited[new_r][new_c][b]:
                q.append((new_r, new_c, b))


for i in range(M):
    for j in range(N):
        if grids[i][j * 3] == "B":
            search(i, j, 0)

print(len(final_config))
