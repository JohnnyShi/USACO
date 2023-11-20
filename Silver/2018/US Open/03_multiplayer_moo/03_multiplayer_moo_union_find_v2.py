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


class UF:
    def __init__(self):
        self.count = N * N
        self.roots = [i for i in range(N * N)]
        self.sizes = [1 for _ in range(N * N)]

    def find(self, id):
        while id != self.roots[id]:
            self.roots[id] = self.roots[self.roots[id]]
            id = self.roots[id]
        return id

    def union(self, id1, id2):
        root1 = self.find(id1)
        root2 = self.find(id2)
        if root1 == root2:
            return
        if self.sizes[root1] > self.sizes[root2]:
            self.roots[root2] = root1
            self.sizes[root1] += self.sizes[root2]
        else:
            self.roots[root1] = root2
            self.sizes[root2] += self.sizes[root1]
        self.count -= 1


uf = UF()
def dfs(row, col, id):
    if visited[row][col]:
        return
    visited[row][col] = True
    uf.union(row * N + col, id)
    for dir in DIRS:
        new_row = row + dir[0]
        new_col = col + dir[1]
        if 0 <= new_row < N and 0 <= new_col < N and board[new_row][new_col] == board[row][col] and not visited[new_row][new_col]:
            dfs(new_row, new_col, id)


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, i * N + j)

# Find single max
fout.write(f"{max(uf.sizes)}\n")

for i in range(N):
    print(uf.roots[i * N : (i + 1) * N])
for i in range(N):
    print(uf.sizes[i * N : (i + 1) * N])
for line in uf.roots:
    print(line)
for line in uf.sizes:
    print(line)

# region max
region_max = 0
for i in range(N - 1):
    for j in range(N - 1):
        if board[i][j] != board[i + 1][j]:
            root1 = uf.roots[i * N + j]
            root2 = uf.roots[(i + 1) * N + j]
            region_max = max(uf.sizes[root1] + uf.sizes[root2], region_max)
        if board[i][j] != board[i][j + 1]:
            root1 = uf.roots[i * N + j]
            root2 = uf.roots[i * N + j + 1]
            region_max = max(uf.sizes[root1] + uf.sizes[root2], region_max)

fout.write(f"{region_max}")
fout.close()
