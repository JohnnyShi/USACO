"""
ID: mck15821
LANG: PYTHON3
PROG: Redistributing Gifts
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1206
N = int(input())
preferences = [[]]
for _ in range(N):
    preferences.append(list(map(int, input().strip().split())))

visited = [False] * (N + 1)
result = [-1] * (N + 1)
# pre-assign top choice
for i in range(1, N + 1):
    # if the assigned gift is the top choice
    if preferences[i][0] == i:
        visited[i] = True
        result[i] = i

print("before backtrack")
print(visited)
print(result)

for line in preferences:
    print(line)

# use backtrack
def backtrack(current, temp):
    print(current)
    print(temp)
    print(visited)
    print()
    if current > N:
        # All visited
        if sum(visited) == N:
            for i in range(1, N + 1):
                print(temp[i])
            exit(0)
        return
    visited[current] = True

    # pick a preferred gift
    for next in preferences[current]:
        # can pick this gift
        if next not in temp:
            temp[current] = next
            for i in range(current + 1, N + 2):
                backtrack(i, temp)
            temp[current] = -1

        # cannot accept preference later than current
        if next == current:
            break

    visited[current] = False

# for each index cow, try to find a preferred gift than the assigned one
for i in range(1, N + 1):
    if not visited[i]:
        backtrack(i, result)
