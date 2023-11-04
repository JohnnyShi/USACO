"""
ID: mck15821
LANG: PYTHON3
PROG: planting
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=895
import sys
sys.setrecursionlimit(10**5)
fin = open('perimeter.in', 'r')
fout = open("perimeter.out", "w")

N = int(fin.readline().strip())
DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]

ice_cream = []
visited = []
for _ in range(N):
    ice_cream.append(fin.readline().strip())
    visited.append([False] * N)

max_area = 0
perimeter_of_max_area = N * N
blob_id = 1


def get_area(row, col, visited, edges, ice_cream, blob_id):
    if visited[row][col] == blob_id or ice_cream[row][col] != "#":
        return 0
    visited[row][col] = blob_id
    count = 1

    # update edges
    edges[0] = min(edges[0], row)
    edges[1] = max(edges[1], row)
    edges[2] = min(edges[2], col)
    edges[3] = max(edges[3], col)

    # count neighbors
    for dir in DIRS:
        x = row + dir[0]
        y = col + dir[1]
        if 0 <= x < N and 0 <= y < N:
            count += get_area(x, y, visited, edges, ice_cream, blob_id)
    return count


def get_perimeter(edges, visited, blob_id):
    perimeter = 0
    # count horizontal perimeter
    for row in range(edges[0], edges[1] + 1):
        col = edges[2]
        while col <= edges[3]:
            # the visited check is for embedded holes
            if visited[row][col] == blob_id:
                perimeter += 1
                while col <= edges[3] and visited[row][col] == blob_id:
                    col += 1
            else:
                col += 1

    for col in range(edges[2], edges[3] + 1):
        row = edges[0]
        while row <= edges[1]:
            if visited[row][col] == blob_id:
                perimeter += 1
                while row <= edges[1] and visited[row][col] == blob_id:
                    row += 1
            else:
                row += 1

    return perimeter * 2


for i in range(N):
    for j in range(N):
        if ice_cream[i][j] == "#" and not visited[i][j]:
            edges = [N - 1, 0, N - 1, 0]  # top, bottom, left, right
            area = get_area(i, j, visited, edges, ice_cream, blob_id)
            if area > max_area:
                max_area = area
                perimeter_of_max_area = get_perimeter(edges, visited, blob_id)
            elif area == max_area:
                perimeter_of_max_area = min(perimeter_of_max_area, get_perimeter(edges, visited, blob_id))
            blob_id += 1

fout.write(f"{max_area} {perimeter_of_max_area}")
fout.close()
