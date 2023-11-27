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

# Pre-calculate distance from each position to rest of the map
distances = []
for _ in range(N + 1):
    distances.append([-1] * (N + 1))

graph = dict()
for _ in range(M):
    a, b, w = map(int, fin.readline().strip().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append((b, w))
    graph[b].append((a, w))


# use dfs to fill the distance matrix
def dfs(current, minimum_width, source):
    # already visited, keep the maximum wormhole width
    if distances[source][current] > 0:
        distances[source][current] = max(distances[source][current], minimum_width)
        distances[current][source] = max(distances[current][source], minimum_width)
        return
    if source == current:
        distances[source][current] = 0
    else:
        distances[source][current] = minimum_width
    if current in graph:
        for next in graph[current]:
            dfs(next[0], min(minimum_width, next[1]), source)


for i in range(1, N + 1):
    dfs(i, 10**9, i)

result = -1

# Sort the orders
for i in range(N):
    if orders[i] != i + 1:
        # find where i + 1 is and swap
        cow_pos = orders.index(i + 1)
        result = max(result, distances[i + 1][cow_pos + 1])
        orders[cow_pos] = orders[i]
        orders[i] = i + 1

fout.write(str(result))
fout.close()
