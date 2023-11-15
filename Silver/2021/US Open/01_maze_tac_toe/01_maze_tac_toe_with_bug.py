"""
ID: mck15821
LANG: PYTHON3
PROG: Maze Tac Toe
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1134
import copy

M = int(input())
grids = []
for _ in range(M):
    grids.append(input())
N = len(grids[0]) // 3
final_config = set()
DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def is_win(board):
    combinations = []
    for i in range(3):
        combinations.append(board[i][0] + board[i][1] + board[i][2])
        combinations.append(board[0][i] + board[1][i] + board[2][i])
    combinations.append(board[0][0] + board[1][1] + board[2][2])
    combinations.append(board[0][2] + board[1][1] + board[2][0])
    reverse_combination = []
    for comb in combinations:
        reverse_combination.append(comb[::-1])
    return "MOO" in (combinations + reverse_combination)


def search(row, col, board, depth):
    # in each search, restart a visited; visited only takes whether we took this path or not
    print("step ", depth, row, col)
    for line in board:
        print(line)
    visited = []
    for i in range(M):
        visited.append([False] * N)
    q = [(row, col)]
    while len(q) > 0:
        r, c = q.pop(-1)
        print("queue pop node", (r, c))
        print("depth:", depth)
        for line in board:
            print(line)
        if visited[r][c]:
            continue
        visited[r][c] = True

        # Process current node
        if grids[r][c * 3] in ["M", "O"]:
            board_r = int(grids[r][c * 3 + 1]) - 1
            board_c = int(grids[r][c * 3 + 2]) - 1

            # backtrack
            if board[board_r][board_c] == ".":

                # Place the character
                board[board_r][board_c] = grids[r][c * 3]
                if is_win(board):
                    final_config.add(tuple(board[0] + board[1] + board[2]))
                    print("end exploration")
                    for line in board:
                        print(line)
                    # set current r, c as visited, and turn back to other nodes
                    board[board_r][board_c] = "."
                    continue
                else:
                    search(r, c, board, depth + 1)
                    # backtrack
                    # board[board_r][board_c] = "."

        # Visit neighbors
        for dir in DIRS:
            new_r = r + dir[0]
            new_c = c + dir[1]
            if 0 <= new_r < M and 0 <= new_c < N and not visited[new_r][new_c] and grids[new_r][new_c * 3] != "#":
                q.append((new_r, new_c))
    print("end of depth", depth, row, col)



for i in range(M):
    for j in range(N):
        if grids[i][j * 3] == "B":
            blank_board = []
            for _ in range(3):
                blank_board.append(["."] * 3)
            search(i, j, blank_board, 0)

print(len(final_config))
for item in final_config:
    print(item)
    print()