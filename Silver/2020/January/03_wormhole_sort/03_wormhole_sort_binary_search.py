"""
ID: mck15821
LANG: PYTHON3
PROG: wormsort
"""
import sys
sys.setrecursionlimit(10**6)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=992
fin = open('wormsort.in', 'r')
fout = open("wormsort.out", "w")

# This is equivalent to build a connected graph to all positions

N, M = map(int, fin.readline().strip().split())
orders = list(map(int, fin.readline().strip().split()))

graph = dict()
weights = []
for _ in range(M):
    a, b, w = map(int, fin.readline().strip().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append((b, w))
    graph[b].append((a, w))
    weights.append(w)


def dfs(current, min_width, regions, label):
    if regions[current] > 0:
        return
    regions[current] = label
    if current in graph:
        for next in graph[current]:
            if min_width <= next[1]:
                dfs(next[0], min_width, regions, label)


def is_valid(min_width):
    regions = [0] * (N + 1)
    label = 1
    # Mark regions; if region of orders[i] != region of i + 1, then the swap never works
    for i in range(1, N + 1):
        if regions[i] == 0:
            dfs(i, min_width, regions, label)
            label += 1

    for i in range(len(orders)):
        # don't belong to the same region, so return False
        if regions[i + 1] != regions[orders[i]]:
            return False
    return True


weights = sorted(weights)
# already sorted
if is_valid(weights[-1] + 1):
    fout.write("-1")
    fout.close()
    exit(0)

left, right = 0, M - 1
while left < right:
    mid = (left + right) // 2
    if is_valid(weights[mid]):
        left = mid + 1
    else:
        right = mid - 1
if is_valid(weights[left]):
    fout.write(str(weights[left]))
else:
    fout.write(str(weights[left - 1]))
fout.close()
