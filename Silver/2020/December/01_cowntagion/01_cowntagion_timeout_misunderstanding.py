"""
ID: mck15821
LANG: PYTHON3
PROG: Cowntagion
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1062
import math
N = int(input())

graph = dict()
for i in range(N + 1):
    graph[i] = []
for _ in range(N - 1):
    p, q = map(int, input().strip().split())
    graph[p].append(q)
    graph[q].append(p)


def dfs_calculate_radius(farm, visited, distance):
    print(farm, distance)
    if visited[farm] or distance > N // 2:
        return distance
    visited[farm] = True
    d = distance
    for next in graph[farm]:
        if not visited[next]:
            d = max(dfs_calculate_radius(next, visited, distance + 1), d)
    return d

# Option 2: find the radius less than N // 2
# Step 1: Find the farm that is at the center (the shortest distance to all other nodes)
min_radius = N
center_pos = [0]  # For an even N, it's possible to have two center nodes
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    distance = dfs_calculate_radius(i, visited, 0)
    if distance == min_radius:
        center_pos.append(i)
    elif distance < min_radius:
        min_radius = distance
        center_pos = [i]

print(min_radius, center_pos)

# Step 2: Move from farm 1 to center
def dfs_traverse(cur, visited, distance, target):
    if cur in target:
        target.clear()
        target.append(cur)
        return distance
    if visited[cur]:
        return distance
    visited[cur] = True
    d = distance
    for next in graph[cur]:
        if not visited[next]:
            d = max(dfs_traverse(next, visited, distance + 1, target), d)
    return d


visited = [False] * (N + 1)
result = dfs_traverse(1, visited, 0, center_pos)
print(result)

# Step 3: grow at the center
days_to_grow = math.log(N, 2)
days_to_grow = int(days_to_grow) + (int(days_to_grow) != days_to_grow)
result += days_to_grow
print("days to grow", days_to_grow)


def bfs_flood_fill(center):
    visited = [False] * (N + 1)
    total = 0
    q = [(center, 0)]
    while len(q) > 0:
        cur, d = q.pop(0)
        if visited[cur]:
            continue
        visited[cur] = True
        total += d
        for next in graph[cur]:
            if not visited[next]:
                q.append([next, d + 1])
    return total


# Step 4: move to other farm
result += bfs_flood_fill(center_pos[0])
print(result)
