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


def find_cycle_min(start):
    slow = a[start]
    fast = a[a[start]]
    while slow != fast:
        # Has visited this loop
        if visited[slow]:
            return 0
        visited[slow] = True
        slow = a[slow]  # move 1 step
        fast = a[a[fast]]  # move 2 steps
    # Cycle found
    min_value = v[slow]
    visited[slow] = True
    fast = a[slow]
    # slow stops, fast move along the cycle to find minimum
    while fast != slow:
        visited[fast] = True
        min_value = min(min_value, v[fast])
        fast = a[fast]
    return min_value


# Find cycles and remove the minimum from each cycle
for i in range(1, N + 1):
    if not visited[i]:
        min_value = find_cycle_min(i)
        total -= min_value
        visited[i] = True
print(total)