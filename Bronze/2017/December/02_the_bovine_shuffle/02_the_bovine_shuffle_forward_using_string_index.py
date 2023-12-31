"""
ID: mck15821
LANG: PYTHON3
PROG: shuffle
"""
fin = open('shuffle.in', 'r')
fout = open("shuffle.out", "w")

N = int(fin.readline().strip())
shuffles = list(map(int, fin.readline().strip().split()))

# [1, 3, 4, 5, 2] -> [0, 2, 3, 4, 1]
for i in range(len(shuffles)):
    shuffles[i] -= 1
print(shuffles)

# [0, 2, 3, 4, 1] -> [0, 4, 1, 2, 3], meaning value on location i comes from location nums[i]
reversed_shuffles = [0 for i in range(N)]
for i in range(N):
    reversed_shuffles[i] = shuffles.index(i)

ids = fin.readline().strip().split()

for _ in range(3):
    new_ids = [-1 for _ in range(N)]
    for origin in range(N):
        # id of origin moving to reversed_shuffles[origin]
        new_ids[reversed_shuffles[origin]] = ids[origin]
    ids = new_ids.copy()

for i in range(N):
    fout.write(f"{ids[i]}\n")

fout.close()
