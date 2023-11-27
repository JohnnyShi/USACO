"""
ID: mck15821
LANG: PYTHON3
PROG: wormsort
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=992
fin = open('wormsort.in', 'r')
fout = open("wormsort.out", "w")

N, M = map(int, fin.readline().strip().split())
orders = list(map(int, fin.readline().strip().split()))


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
for _ in range(M):
    a, b, w = map(int, fin.readline().strip().split())
    edges.append(Edge(w, a, b))
edges = sorted(edges, key=lambda x: x.weight, reverse=True)
uf = UF()

# For sorted cow, union with group 0 to form a group
for i in range(len(orders)):
    if orders[i] == i + 1:
        uf.union(0, i + 1)

if uf.count == 1:
    fout.write("-1")
    fout.close()
    exit(0)

for e in edges:
    uf.union(e.source, e.target)
    if uf.count == 1:
        fout.write(str(e.weight))
        fout.close()
        exit(0)
