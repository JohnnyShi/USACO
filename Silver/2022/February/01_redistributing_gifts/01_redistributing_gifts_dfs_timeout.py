"""
ID: mck15821
LANG: PYTHON3
PROG: Redistributing Gifts
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1206
# Time complexity: N^4
N = int(input())
preferences = [[]]
for _ in range(N):
    preferences.append(list(map(int, input().strip().split())))


# backtrack to fill
def backtrack(arrangement, bank):
    # check exit criteria
    if len(bank) == 0:
        return True
    for i in range(1, N + 1):
        if arrangement[i] < 0:
            for p in preferences[i]:
                # This gift can be given
                if p in bank:
                    bank.remove(p)
                    arrangement[i] = p
                    if backtrack(arrangement, bank):
                        return True

                    # backtrack
                    arrangement[i] = -1
                    bank.add(p)
                if p == i:
                    return False
    return False


# Use greedy approach, assign the first preferred gift;
# if can fulfill requirements for other cows, then this gift is the best gift the cow can get
for i in range(1, N + 1):
    for p in preferences[i]:
        arrangement = [-1] * (N + 1)
        arrangement[i] = p

        # the rest of gift to give
        bank = set([j for j in range(1, N + 1)])
        bank.remove(p)

        if backtrack(arrangement, bank):
            print(p)
            break

        # cannot fill preference larger than i
        if p == i:
            break
