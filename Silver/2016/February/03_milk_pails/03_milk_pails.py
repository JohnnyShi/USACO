"""
ID: mck15821
LANG: PYTHON3
PROG: pails
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=620
fin = open('pails.in', 'r')
fout = open("pails.out", "w")
X, Y, K, M = map(int, fin.readline().strip().split())
state = (0, 0)
q = set()
q.add(state)
count = 0
while len(q) > 0:
    size_of_q = len(q)
    next = set()
    while size_of_q > 0:
        size_of_q -= 1
        state = q.pop()
        next.add((0, state[1]))
        next.add((X, state[1]))
        next.add((state[0], 0))
        next.add((state[0], Y))
        if state[0] == 0:
            if state[1] < X:
                next.add((state[1], 0))  # pour all state[1] to state[0]
            else:
                next.add((X, state[1] - X))  # fill state[0] with state[1]
        elif state[1] == 0:
            if state[0] < Y:
                next.add((0, state[0]))  # pour all state[0] to state[1]
            else:
                next.add((state[0] - Y, Y))  # fill state[1] with state[0]
        else:
            if state[0] + state[1] <= X:
                next.add((state[0] + state[1], 0))
            else:
                next.add((X, state[1] - (X - state[0])))
            if state[0] + state[1] <= Y:
                next.add((0, state[0] + state[1]))
            else:
                next.add((state[0] - (Y - state[1]), Y))
    q = q.union(next)
    count += 1
    if count == K:
        break

result = float("inf")
for state in q:
    if abs(state[0] + state[1] - M) < result:
        result = abs(state[0] + state[1] - M)
fout.write(f"{result}")
fout.close()
