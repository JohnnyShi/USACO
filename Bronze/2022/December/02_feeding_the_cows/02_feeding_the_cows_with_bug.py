"""
ID: mck15821
LANG: PYTHON3
PROG: Feeding The Cows
"""
# http://usaco.org/index.php?page=viewproblem2&cpid=1252
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    cows = input()
    patches = ["."] * N
    for i in range(len(cows)):
        for j in range(max(0, i - K), i):
            if patches[j] == cows[i]:
                break
        else:
            patches[i] = cows[i]
    patches = "".join(patches)
    print(N - patches.count("."))
    print(patches)
