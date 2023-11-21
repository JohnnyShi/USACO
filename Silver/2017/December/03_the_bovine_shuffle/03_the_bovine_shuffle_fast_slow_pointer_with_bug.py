"""
ID: mck15821
LANG: PYTHON3
PROG: shuffle
"""
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
        # no cycle
        if fast == shuffles[fast]:
            # Mark
            while slow != fast:
                visited[slow] = True
                slow = shuffles[slow]
            visited[slow] = True
            return 1
        if visited[slow]:
            return 0
        visited[slow] = True
        fast = shuffles[shuffles[fast]]
        slow = shuffles[slow]
    # BUG: did not do visit check so may double count
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
