"""
ID: mck15821
LANG: PYTHON3
PROG: closing
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=644
fin = open('closing.in', 'r')
fout = open("closing.out", "w")
N, M = map(int, fin.readline().strip().split())
graph = [set() for i in range(N)]

for _ in range(M):
    a, b = map(int, fin.readline().strip().split())
    graph[a - 1].add(b - 1)
    graph[b - 1].add(a - 1)

region_id_to_farm = dict()
region_id = 0
visited = [False] * N
farm_to_region_id = [0] * N


def dfs(current, visited, region_id, farm_to_region_id, region_id_to_farm):
    if visited[current]:
        return
    visited[current] = True
    farm_to_region_id[current] = region_id
    region_id_to_farm[region_id].append(current)
    for next in graph[current]:
        if not visited[next]:
            dfs(next, visited, region_id, farm_to_region_id, region_id_to_farm)


for i in range(N):
    if not visited[i]:
        region_id_to_farm[region_id] = []
        dfs(i, visited, region_id, farm_to_region_id, region_id_to_farm)
        region_id += 1

if len(region_id_to_farm) != 1:
    fout.write("NO\n")
else:
    fout.write("YES\n")

visited = [False] * N

for _ in range(N - 1):
    closed_farm = int(fin.readline().strip()) - 1
    farm_region_id = farm_to_region_id[closed_farm]

    # the closed farm doesn't break an existed region
    farms_in_the_same_region = region_id_to_farm[farm_region_id]
    visited[closed_farm] = True  # Mark the closed farm
    round_visited = visited.copy()
    region_id_to_farm.pop(farm_region_id)  # Remove the region and to create new ones

    for farm in farms_in_the_same_region:
        if not round_visited[farm]:
            region_id_to_farm[region_id] = []
            dfs(farm, round_visited, region_id, farm_to_region_id, region_id_to_farm)
            region_id += 1

    if len(region_id_to_farm) != 1:
        fout.write("NO\n")
    else:
        fout.write("YES\n")

fout.close()
