"""
ID: mck15821
LANG: PYTHON3
PROG: Rotate and Shift
"""
# http://usaco.org/index.php?page=viewproblem2&cpid=1325
N, K, T = map(int, input().split())
pos = [str(i) for i in range(N)]
A = list(map(int, input().split()))


def rotate_and_shift(pos, A):
    # rotate
    t = pos[A[-1]]  # temp for the last value
    for i in range(len(A) - 1, -1, -1):
        pos[A[i]] = pos[A[i - 1]]
    pos[A[0]] = t

    # shift
    A = [(i + 1) % N for i in A]
    return pos, A


period = 0
visited = set()
while period < T:
    if tuple(pos) in visited:
        # print("visited")
        # print(pos)
        # print(period)
        break
    visited.add(tuple(pos))
    pos, A = rotate_and_shift(pos, A)
    period += 1
    # print(pos)
    # print(A)

T %= period
while T > 0:
    pos, A = rotate_and_shift(pos, A)
    T -= 1
print(" ".join(pos))
