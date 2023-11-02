"""
ID: mck15821
LANG: PYTHON3
PROG: Stamp Grid
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1300

T = int(input())


def rotate_stamp(stamp):
    new_stamp = []
    N = len(stamp)
    for i in range(N):
        new_stamp.append(["."] * N)
    for i in range(N):
        for j in range(N):
            # *.*      .**
            # **.  ->  .*.
            # ...      ..*
            new_stamp[i][j] = stamp[N - 1 - j][i]
    return new_stamp


def paint(target_graph, paint_graph, stamp, row_start, column_start):
    N = len(stamp)
    for i in range(N):
        for j in range(N):
            if target_graph[row_start + i][column_start + j] == "." and stamp[i][j] == "*":
                return
    for i in range(N):
        for j in range(N):
            if stamp[i][j] == "*":
                paint_graph[row_start + i][column_start + j] = "*"


for _ in range(T):
    # I/O
    input()
    graph_width = int(input())
    target_graph = []
    painted_graph = []
    for i in range(graph_width):
        target_graph.append(list(input()))
        painted_graph.append(["."] * graph_width)
    stamp_width = int(input())
    stamp = []
    for i in range(stamp_width):
        stamp.append(list(input()))

    # rotate 4 times
    for angle in range(4):
        for row_start in range(graph_width - stamp_width + 1):
            for column_start in range(graph_width - stamp_width + 1):
                paint(target_graph, painted_graph, stamp, row_start, column_start)

        if target_graph == painted_graph:
            print("YES")
            break
        stamp = rotate_stamp(stamp)
    else:
        print("NO")
