"""
ID: mck15821
LANG: PYTHON3
PROG: Connecting two barns
"""
import sys
sys.setrecursionlimit(10**7)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1159
T = int(input())


class UF:
    def __init__(self, N):
        self.count = N
        self.roots = [i for i in range(N)]
        self.sizes = [1 for _ in range(N)]

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

for _ in range(T):
    N, M = map(int, input().strip().split())
    # Build regions, and connect region by greedy order
    uf = UF(N + 1)
    for edge in range(M):
        node1, node2 = map(int, input().strip().split())
        uf.union(node1, node2)
    count = 0
    for i in range(1, N):
        if uf.find(i) != uf.find(i + 1):
            uf.union(i, i + 1)
            count += 1
    print(count)
