"""
ID: mck15821
LANG: PYTHON3
PROG: multimoo
"""
import sys
sys.setrecursionlimit(10**7)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=836
fin = open('multimoo.in', 'r')
fout = open("multimoo.out", "w")
N = int(fin.readline().strip())
board = []
for _ in range(N):
    board.append(list(map(int, fin.readline().strip().split())))
region_board = []
for _ in range(N):
    region_board.append([-1] * N)
DIRS = [[0, 1], [0, -1], [-1, 0], [1, 0]]
region_list = []


class Region:
    def __init__(self, region_id, cow_id):
        self.region_id = region_id
        self.region_size = 0
        self.cow_id = cow_id

    def __repr__(self):
        return f"{self.region_id} {self.region_size} {self.cow_id}"


def dfs(row, col, region_id, visited):
    if visited[row][col]:
        return 0
    visited[row][col] = True
    region_board[row][col] = region_id
    count = 1
    for dir in DIRS:
        new_row = row + dir[0]
        new_col = col + dir[1]
        if 0 <= new_row < N and 0 <= new_col < N and board[new_row][new_col] == board[row][col] and not visited[new_row][new_col]:
            count += dfs(new_row, new_col, region_id, visited)
    return count


visited = []
for _ in range(N):
    visited.append([False] * N)

region_id = 0
single_max_region = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            r = Region(region_id, board[i][j])
            count = dfs(i, j, region_id, visited)
            single_max_region = max(single_max_region, count)
            r.region_size = count
            region_id += 1
            region_list.append(r)

fout.write(f"{single_max_region}\n")

# Find neighbor list for all regions
region_neighbors = dict()
for i in range(region_id):
    region_neighbors[i] = set()

visited = []
for _ in range(N):
    visited.append([False] * N)


def find_neighbors(row, col, region_id, visited):
    if visited[row][col]:
        return
    visited[row][col] = True
    for dir in DIRS:
        new_row = row + dir[0]
        new_col = col + dir[1]
        if 0 <= new_row < N and 0 <= new_col < N:
            if board[new_row][new_col] == board[row][col] and not visited[new_row][new_col]:
                dfs(new_row, new_col, region_id, visited)
            else:
                other_region_id = region_board[new_row][new_col]
                region_neighbors[region_id].add(other_region_id)
                region_neighbors[other_region_id].add(region_id)


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            find_neighbors(i, j, region_board[i][j], visited)

print(region_neighbors)

region_max = 0


# Count combined area for each region
def find_combined_area(region_id1, region_id2, current_region, visited_region):
    if visited_region[current_region]:
        return 0
    visited_region[current_region] = True
    total = region_list[current_region].region_size
    for neighbor in region_neighbors[current_region]:
        # 
        if neighbor not in [region_id1, region_id2] and not visited_region[neighbor]:
            if region_list[neighbor].cow_id in [region_list[region_1].cow_id, region_list[region_2].cow_id]:
                total += find_combined_area(region_id1, region_id2, neighbor, visited_region)
    return total


for region_1 in range(len(region_list)):
    for region_2 in region_neighbors[region_1]:
        # To avoid duplication check
        if region_2 < region_1:
            continue
        visited_region = [False] * len(region_list)
        region_1_area = find_combined_area(region_1, region_2, region_1, visited_region)
        region_2_area = find_combined_area(region_1, region_2, region_2, visited_region)
        if region_1_area + region_2_area == 72:
            print(region_1, region_2, region_1_area, region_2_area, region_1_area + region_2_area)
        region_max = max(region_max, region_1_area + region_2_area)


fout.write(f"{region_max}")
fout.close()
