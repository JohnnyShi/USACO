"""
ID: mck15821
LANG: PYTHON3
PROG: Redistributing Gifts
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1206
# time complexity: cache for N * N
N = int(input())
preferences = [[]]
for i in range(1, N + 1):
    p = list(map(int, input().strip().split()))
    while p[-1] != i:
        p.pop(-1)
    preferences.append(p)

# if cow i wants to take a preferred gift j, then the original gift i needs to be taken by someone else,
# and ultimately cow j needs to find another gift to take.
# So if a cycle exist that can traverse from j to i, then i can take j
reachable = []
for _ in range(N + 1):
    reachable.append([-1] * (N + 1))
for i in range(1, N + 1):
    reachable[i][i] = True


def find_cycle(source, current, visited):
    # Found a loop
    if source == current:
        return True

    # cache result
    if reachable[source][current] != -1:
        return reachable[source][current]

    # a visited gift
    if visited[current]:
        return False

    visited[current] = True
    for next in preferences[current]:
        if find_cycle(source, next, visited):
            # mark cache for each edge along the graph
            reachable[current][next] = True
            return True
    reachable[current][next] = False
    return False


for i in range(1, N + 1):
    for p in preferences[i]:
        visited = [False] * (N + 1)
        if find_cycle(i, p, visited):
            print(p)
            break
