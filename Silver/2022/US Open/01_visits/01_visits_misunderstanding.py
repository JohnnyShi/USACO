"""
ID: mck15821
LANG: PYTHON3
PROG: Visits
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1230
N = int(input())
a = [0]
v = [0]
for _ in range(N):
    ai, vi = map(int, input().strip().split())
    a.append(ai)
    v.append(vi)


# Misunderstand that it's a whole cycle
def find_cycle(start):
    q = [start]
    min_v = v[start]
    total = 0
    while len(q) > 0:
        cur = q.pop(0)
        # cycle ends
        if visited[cur]:
            return total - min_v
        visited[cur] = True
        min_v = min(min_v, v[cur])
        total += v[cur]
        q.append(a[cur])


# Found how many cycles in a, then for each cycle find the minimum
visited = [False] * (N + 1)
result = 0
for i in range(1, N + 1):
    if not visited[i]:
        result += find_cycle(i)
print(result)
