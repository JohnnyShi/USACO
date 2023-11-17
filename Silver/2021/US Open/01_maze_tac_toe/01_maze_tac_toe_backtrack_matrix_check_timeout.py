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


def is_win(board):
    # construct board back
    board_matrix = []
    for i in range(3):
        board_matrix.append(board[i * 3: (i + 1) * 3])

    # check win
    combinations = []
    for i in range(3):
        combinations.append(board_matrix[i][0] + board_matrix[i][1] + board_matrix[i][2])
        combinations.append(board_matrix[0][i] + board_matrix[1][i] + board_matrix[2][i])
    combinations.append(board_matrix[0][0] + board_matrix[1][1] + board_matrix[2][2])
    combinations.append(board_matrix[0][2] + board_matrix[1][1] + board_matrix[2][0])
    reverse_combination = []
    for comb in combinations:
        reverse_combination.append(comb[::-1])
    return "MOO" in (combinations + reverse_combination)


# Convert list to string for hash
def list_to_str_helper(board):
    return "".join(board)


def print_board_helper(board):
    for i in range(3):
        print(board[i * 3: (i + 1) * 3])
    print()


def search(row: int, col: int, board: list, visited):
    # Already visit this point with the current board setting, return
    if list_to_str_helper(board) in visited[row][col]:
        return
    visited[row][col].add(list_to_str_helper(board))

    original_board = board.copy()  # for backtrack purpose

    # if meet a character
    if grids[row][col * 3] in ["M", "O"]:
        board_r = int(grids[row][col * 3 + 1]) - 1
        board_c = int(grids[row][col * 3 + 2]) - 1
        board_coordinate = board[board_r * 3 + board_c]

        # an empty place
        if board_coordinate == ".":
            board[board_r * 3 + board_c] = grids[row][col * 3]

            if is_win(list_to_str_helper(board)):
                final_config.add(list_to_str_helper(board.copy()))

                # Clear for backtrack
                board.clear()
                for c in original_board:
                    board.append(c)
                visited[row][col].remove(list_to_str_helper(board))
                return

            # not win, continue to explore

    # Visit neighbors
    for dir in DIRS:
        new_r = row + dir[0]
        new_c = col + dir[1]
        if 0 <= new_r < M and 0 <= new_c < N and grids[new_r][new_c * 3] != "#" and list_to_str_helper(board) not in visited[new_r][new_c]:
            search(new_r, new_c, board, visited)

    # revert for backtrack
    board.clear()
    for c in original_board:
        board.append(c)
    visited[row][col].remove(list_to_str_helper(board))


for i in range(M):
    for j in range(N):
        if grids[i][j * 3] == "B":
            blank_board = ["."] * 9
            # visited is a M * N matrix, and each coordinate has a set to record board status
            visited = []
            for x in range(M):
                line = []
                for y in range(N):
                    line.append(set())
                visited.append(line)
            search(i, j, blank_board, visited)

print(len(final_config))
