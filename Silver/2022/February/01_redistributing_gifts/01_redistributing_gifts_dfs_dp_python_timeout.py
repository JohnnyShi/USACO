"""
ID: mck15821
LANG: PYTHON3
PROG: Redistributing Gifts
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1206
# time complexity: O(N ^ 3) to build cycle
N = int(input())
preferences = [[]]
for i in range(1, N + 1):
    p = list(map(int, input().strip().split()))
    while p[-1] != i:
        p.pop(-1)
    preferences.append(p)

reachable = []
for _ in range(N + 1):
    reachable.append([False] * (N + 1))

# If there's a cow i prefer gift j, then reachable[j][i] is true
# we cannot be sure about reachable[i][j], because we are not certain whether a cycle could exist
# but can backward to bottom-up and build a cycle
for cow1 in range(1, N + 1):
    for p in preferences[cow1]:
        reachable[p][cow1] = True

# cow2 as the bridge, to extend the length, and try to build a cycle
for cow2 in range(1, N + 1):
    for cow1 in range(1, N + 1):
        for cow3 in range(1, N + 1):
            reachable[cow1][cow3] = reachable[cow1][cow3] or (reachable[cow1][cow2] and reachable[cow2][cow3])

for cow in range(1, N + 1):
    for p in preferences[cow]:
        if reachable[cow][p]:
            print(p)
            break
