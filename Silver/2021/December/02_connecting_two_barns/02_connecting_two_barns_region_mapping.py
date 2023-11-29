"""
ID: mck15821
LANG: PYTHON3
PROG: Connecting two barns
"""
import sys
sys.setrecursionlimit(10**7)
# Time complexity: O(N) (mark region) +  N/2 * N/2(worst case) = O(N^2)
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1159


def dfs(current, visited, region_id, graph, barn_to_region_id, region_id_to_barn):
    if visited[current]:
        return
    visited[current] = True
    barn_to_region_id[current] = region_id
    region_id_to_barn[region_id].append(current)
    for next in graph[current]:
        if not visited[next]:
            dfs(next, visited, region_id, graph, barn_to_region_id, region_id_to_barn)


def calc_distance(region1, region2):
    result = 10 ** 5  # max distance
    for barn1 in region_id_to_barn[region1]:
        for barn2 in region_id_to_barn[region2]:
            result = min(abs(barn1 - barn2), result)
    return result


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
    region_id_to_barn = dict()
    visited = [False] * N

    # Mark region id for each barn
    for i in range(0, N):
        # if not visited yet
        if not visited[i]:
            region_id_to_barn[region_id] = []
            dfs(i, visited, region_id, graph, barn_to_region_id, region_id_to_barn)
            region_id += 1

    # barn 0 and N - 1 already connected
    if barn_to_region_id[0] == barn_to_region_id[N - 1]:
        print(0)
        continue

    # calculate the distance from region of 0 to other regions
    region_first_distance = [10 ** 10] * len(region_id_to_barn)
    for other_region in region_id_to_barn:
        region_first_distance[other_region] = calc_distance(barn_to_region_id[0], other_region)

    region_last_distance = [10 ** 10] * len(region_id_to_barn)
    for other_region in region_id_to_barn:
        region_last_distance[other_region] = calc_distance(barn_to_region_id[N - 1], other_region)

    result = 10 ** 10
    for i in range(len(region_id_to_barn)):
        result = min(result, region_first_distance[i] ** 2 + region_last_distance[i] ** 2)
    print(result)

