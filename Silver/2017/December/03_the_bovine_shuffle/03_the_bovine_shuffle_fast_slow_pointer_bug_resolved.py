"""
ID: mck15821
LANG: PYTHON3
PROG: shuffle
"""
# This is 2 times faster than v3 as v3 scan another N to mark
# http://www.usaco.org/index.php?page=viewproblem2&cpid=764
fin = open('shuffle.in', 'r')
fout = open("shuffle.out", "w")
N = int(fin.readline().strip())
shuffles = list(map(int, fin.readline().strip().split()))
shuffles.insert(0, 0)  # match 1-base index

visited = [False] * (N + 1)


def find_cycle(start):
    slow = shuffles[start]
    fast = shuffles[shuffles[start]]
    while slow != fast:
        if visited[slow]:
            return 0
        visited[slow] = True
        # No cycle
        if fast == shuffles[fast]:
            return 0
        fast = shuffles[shuffles[fast]]
        slow = shuffles[slow]

    # BUG resolved: for a single point cycle, the slow and fast are the same, but need to check visit first
    if visited[slow]:
        return 0

    # Found a cycle
    count = 1
    visited[slow] = True
    fast = shuffles[fast]
    while fast != slow:
        visited[fast] = True
        fast = shuffles[fast]
        count += 1
    return count


result = 0
# Find cycle and the length of all cycles are the answer
for i in range(1, N + 1):
    if not visited[i]:
        result += find_cycle(i)
        visited[i] = True

fout.write(str(result))
fout.close()
