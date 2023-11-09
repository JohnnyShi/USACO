"""
ID: mck15821
LANG: PYTHON3
PROG: ccski
"""
# Time Complexity: MN * log(MN)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=380
fin = open('ccski.in', 'r')
fout = open("ccski.out", "w")
M, N = map(int, fin.readline().strip().split())
elevations = []
for _ in range(M):
    elevations.append(list(map(int, fin.readline().strip().split())))
waypoints = []
for i in range(M):
    line = list(map(int, fin.readline().strip().split()))
    for j in range(len(line)):
        if line[j] == 1:
            waypoints.append((i, j))

DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]


class Edge:
    def __init__(self, weight, source, target):
        self.weight = weight
        self.source = source
        self.target = target

    def __repr__(self):
        return f"{self.weight} {self.source} {self.target}"


class UF:
    def __init__(self):
        self.count = M * N
        self.roots = [i for i in range(M * N)]
        self.sizes = [1 for _ in range(M * N)]

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


edges = []
for i in range(M):
    for j in range(N):
        if i > 0:
            edges.append(Edge(abs(elevations[i][j] - elevations[i - 1][j]), (i, j), (i - 1, j)))
        if j > 0:
            edges.append(Edge(abs(elevations[i][j] - elevations[i][j - 1]), (i, j), (i, j - 1)))

edges = sorted(edges, key=lambda x: x.weight)
uf = UF()

while len(edges) > 0:
    edge = edges.pop(0)
    s_r, s_c = edge.source
    t_r, t_c = edge.target
    uf.union(s_r * N + s_c, t_r * N + t_c)
    ancestor = uf.find(waypoints[0][0] * N + waypoints[0][1])
    for waypoint in waypoints:
        if uf.find(waypoint[0] * N + waypoint[1]) != ancestor:
            break
    else:
        fout.write(str(edge.weight))
        fout.close()
        exit(0)
