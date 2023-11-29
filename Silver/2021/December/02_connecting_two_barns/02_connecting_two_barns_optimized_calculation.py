"""
ID: mck15821
LANG: PYTHON3
PROG: Connecting two barns
"""
import sys
sys.setrecursionlimit(10**7)
# Time complexity: O(N) (mark region) + 2 * O(N)(worst case) = O(N)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1159


def dfs(current, visited, region_id, graph, barn_to_region_id):
    if visited[current]:
        return
    visited[current] = True
    barn_to_region_id[current] = region_id
    for next in graph[current]:
        if not visited[next]:
            dfs(next, visited, region_id, graph, barn_to_region_id)


# Optimize O(N^2 to O(N + size of region))
def calc_distance(region, number_of_regions):
    barns = region_id_to_barn[region]
    region_distance = [10 ** 5] * number_of_regions

    # Use two pointer to compare distance between region and a single barn
    barnIndex = 0
    for i in range(N):
        dist = abs(barns[barnIndex] - i)
        while barnIndex < len(barns) - 1 and abs(barns[barnIndex + 1] - i) < dist:
            barnIndex += 1
        region_distance[barn_to_region_id[i]] = min(region_distance[barn_to_region_id[i]], dist)

    return region_distance



T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split())
    graph = []
    for _ in range(N):
        graph.append([])
    for _ in range(M):
        a, b = map(int, input().strip().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    # map barn to region id
    barn_to_region_id = [0 for i in range(N)]
    region_id = 0
    visited = [False] * N

    # Mark region id for each barn
    for i in range(0, N):
        # if not visited yet
        if not visited[i]:
            dfs(i, visited, region_id, graph, barn_to_region_id)
            region_id += 1

    # barn 0 and N - 1 already connected
    if barn_to_region_id[0] == barn_to_region_id[N - 1]:
        print(0)
        continue

    # construct mapping from region_id to barn, in ascending order
    region_id_to_barn = []
    for i in range(region_id):
        region_id_to_barn.append([])
    for i in range(N):
        region_id_to_barn[barn_to_region_id[i]].append(i)

    # calculate the distance from region of 0 to other barn
    region_first_distance = calc_distance(barn_to_region_id[0], region_id)
    region_last_distance = calc_distance(barn_to_region_id[N - 1], region_id)

    result = 10 ** 10
    for i in range(len(region_id_to_barn)):
        result = min(result, region_first_distance[i] ** 2 + region_last_distance[i] ** 2)
    print(result)
