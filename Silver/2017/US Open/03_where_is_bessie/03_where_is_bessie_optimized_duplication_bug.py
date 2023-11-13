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


def bfs(row, col, visited, color):
    q = [(row, col)]
    while len(q) > 0:
        r, c = q.pop(0)
        if visited[r][c]:
            continue
        visited[r][c] = True
        for dir in DIRS:
            new_row = r + dir[0]
            new_col = c + dir[1]
            if 0 <= new_row < N and 0 <= new_col < N and not visited[new_row][new_col] and image[new_row][
                new_col] == color:
                q.append((new_row, new_col))


def count_regions(start_row, start_col, end_row, end_col, color):
    visited = []
    for i in range(N):
        visited.append([True] * N)
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            visited[i][j] = False
    count = 0
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            if image[i][j] == color and not visited[i][j]:
                bfs(i, j, visited, color)
                count += 1
    return count


def is_pcl(start_row, start_col, end_row, end_col):
    colors = get_colors(start_row, start_col, end_row, end_col)
    if len(colors) != 2:
        return False
    count_1 = count_regions(start_row, start_col, end_row, end_col, colors[0])
    count_2 = count_regions(start_row, start_col, end_row, end_col, colors[1])
    return count_1 == 1 and count_2 > 1 or count_1 > 1 and count_2 == 1


def search(start_min_row, start_max_row, start_min_col, start_max_col, end_min_row, end_max_row, end_min_col,
           end_max_col):
    count = 0
    for start_row in range(start_min_row, start_max_row + 1):
        for start_col in range(start_min_col, start_max_col + 1):
            for end_row in range(end_max_row, end_min_row - 1, -1):
                for end_col in range(end_max_col, end_min_col - 1, -1):
                    if is_pcl(start_row, start_col, end_row, end_col):
                        count += 1  # this PCL
                        # skip this row, fix top-left corner and count the rest of PCL
                        count += search(start_row, start_row, start_col, start_col,
                                        start_row, end_row - 1, end_col + 1, end_max_col)

                        # move 1 step to the right of the top-left corner
                        count += search(start_row, end_row, start_col + 1, start_max_col,
                                        start_row, end_row, end_col + 1, end_max_col)
                        count += search(start_row, start_max_row, start_col + 1, start_max_col,
                                        end_row + 1, end_max_row, start_col + 1, end_max_col)

                        # get to next line
                        count += search(start_row + 1, start_max_row, start_min_col, start_col - 1,
                                        start_row + 1, start_max_row, start_min_col, start_max_col)
                        count += search(start_row + 1, start_max_row, start_col, start_col,
                                        start_row + 1, end_row, end_col + 1, end_max_col)
                        count += search(start_row + 1, start_max_row, start_col, start_col,
                                        end_row + 1, start_max_row, start_col, end_max_col)

                        return count
    return count


fout.write(f"{search(0, N - 1, 0, N - 1, 0, N - 1, 0, N - 1)}")
fout.close()
