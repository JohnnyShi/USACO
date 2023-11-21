"""
ID: mck15821
LANG: PYTHON3
PROG: Visits
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1230
N = int(input())
a = [0]
v = [0]
total = 0
for _ in range(N):
    ai, vi = map(int, input().strip().split())
    a.append(ai)
    v.append(vi)
    total += vi


class Edge:
    def __init__(self, weight, source, target):
        self.weight = weight
        self.source = source
        self.target = target

    def __repr__(self):
        return f"{self.weight} {self.source} {self.target}"


class UF:
    def __init__(self):
        self.count = N + 1
        self.roots = [i for i in range(N + 1)]
        self.sizes = [1 for _ in range(N + 1)]

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
for i in range(1, len(a)):
    edges.append(Edge(v[i], i, a[i]))
edges = sorted(edges, key=lambda x: x.weight, reverse=True)

uf = UF()
total = 0
count = 0
while len(edges) > 0 and count < N - 1:
    edge = edges.pop(0)
    if uf.find(edge.source) != uf.find(edge.target):
        total += edge.weight
        uf.union(edge.source, edge.target)
print(total)
