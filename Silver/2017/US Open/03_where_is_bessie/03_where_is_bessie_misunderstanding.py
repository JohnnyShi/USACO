"""
ID: mck15821
LANG: PYTHON3
PROG: where
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=740
fin = open('where.in', 'r')
fout = open("where.out", "w")
N = int(fin.readline().strip())
image = []
for _ in range(N):
    image.append(fin.readline().strip())
DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def get_colors(start_row, start_col, end_row, end_col):
    visited = set()
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            visited.add(image[i][j])
    return list(visited)


def dfs(row, col, visited, start_row, start_col, end_row, end_col, color):
    if visited[row][col]:
        return
    visited[row][col] = True
    for dir in DIRS:
        new_row = row + dir[0]
        new_col = col + dir[1]
        if start_row <= new_row <= end_row and start_col <= new_col <= end_col and image[new_row][new_col] == color:
            dfs(new_row, new_col, visited, start_row, start_col, end_row, end_col, color)


def count_regions(start_row, start_col, end_row, end_col, color):
    visited = []
    for i in range(N):
        visited.append([False] * N)
    count = 0
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            if image[i][j] == color and not visited[i][j]:
                dfs(i, j, visited, start_row, start_col, end_row, end_col, color)
                count += 1
    return count


def is_pcl(start_row, start_col, end_row, end_col):
    colors = get_colors(start_row, start_col, end_row, end_col)
    if len(colors) != 2:
        return False
    count_1 = count_regions(start_row, start_col, end_row, end_col, colors[0])
    count_2 = count_regions(start_row, start_col, end_row, end_col, colors[1])
    return count_1 == 1 and count_2 > 1 or count_1 > 1 and count_2 == 1


result = 0
for start_row in range(N):
    for start_col in range(N):
        end_max_col = N - 1
        for end_row in range(start_row + 1, N):
            for end_col in range(start_col + 1, end_max_col + 1):
                if is_pcl(start_row, start_col, end_row, end_col):
                    result += 1
                    print(start_row, start_col, end_row, end_col)
                    # no need to scan the same row after this
                    end_max_col = end_col
                    break

fout.write(f"{result}")
fout.close()