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

visited = [False] * (N + 1)


def find_cycle_min(current):
    met = set()
    while current not in met:
        met.add(current)
        if visited[current]:
            return 0
        visited[current] = True
        current = a[current]
    # Cycle found
    pointer = current
    min_value = v[current]
    # find minimum in cycle
    while a[pointer] != current:
        pointer = a[pointer]
        min_value = min(min_value, v[pointer])
    return min_value


# Find cycles and remove the minimum from each cycle
for i in range(1, N + 1):
    if not visited[i]:
        min_value = find_cycle_min(i)
        total -= min_value
print(total)