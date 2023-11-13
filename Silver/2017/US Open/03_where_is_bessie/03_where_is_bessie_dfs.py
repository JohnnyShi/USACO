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


def dfs(row, col, visited, color):
    if visited[row][col]:
        return
    visited[row][col] = True
    for dir in DIRS:
        new_row = row + dir[0]
        new_col = col + dir[1]
        if 0 <= new_row < N and 0 <= new_col < N and not visited[new_row][new_col] and image[new_row][new_col] == color:
            dfs(new_row, new_col, visited, color)


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
                dfs(i, j, visited, color)
                count += 1
    return count


def is_pcl(start_row, start_col, end_row, end_col):
    colors = get_colors(start_row, start_col, end_row, end_col)
    if len(colors) != 2:
        return False
    count_1 = count_regions(start_row, start_col, end_row, end_col, colors[0])
    count_2 = count_regions(start_row, start_col, end_row, end_col, colors[1])
    return count_1 == 1 and count_2 > 1 or count_1 > 1 and count_2 == 1


def is_inside(source_start, source_end, target_start, target_end):
    return source_start[0] >= target_start[0] and source_start[1] >= target_start[1] and source_end[0] <= target_end[0] and source_end[1] <= target_end[1]


# def search(start_min_row, start_max_row, start_min_col, start_max_col, end_min_row, end_max_row, end_min_col, end_max_col):



pcl_candidates = []
for start_row in range(N):
    for start_col in range(N):
        for end_row in range(start_row, N):
            for end_col in range(start_col, N):
                if is_pcl(start_row, start_col, end_row, end_col):
                    pcl_candidates.append([(start_row, start_col), (end_row, end_col)])

                    # no need to scan the same row after this
                    # end_min_col = end_col + 1
                    # print(start_row, start_col, end_row, end_col)
                    # print(end_min_col)
                    # break
result = 0
print(pcl_candidates)
for candidate in pcl_candidates:
    for other in pcl_candidates:
        if candidate != other and is_inside(candidate[0], candidate[1], other[0], other[1]):
            break
    else:
        result += 1

fout.write(f"{result}")
fout.close()