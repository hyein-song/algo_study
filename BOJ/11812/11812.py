import sys


def tracking(start):
    tmp = [start]
    x = start
    root = 1
    depth = 0
    while True:
        calc = k**depth
        if root + calc > x:
            break
        root += calc
        depth += 1

    p, idx = divmod((x - root), k)
    while depth > 0:
        depth -= 1
        root -= k**depth
        parent = root + p
        tmp.append(parent)
        p, idx = divmod((parent - root), k)

    return tmp


def dist(x,y):
    x_list = tracking(x)
    y_list = tracking(y)

    x_depth = len(x_list)
    y_depth = len(y_list)

    x_idx = y_idx = 0
    result = 0

    if x_depth < y_depth:
        y_idx = y_depth - x_depth
        result += y_idx
    elif x_depth > y_depth:
        x_idx = x_depth - y_depth
        result += x_idx

    for i in range(min(x_depth,y_depth)):
        if x_list[x_idx+i] == y_list[y_idx+i]:
            result += i*2
            break

    print(result)
    return


n, k, q = map(int, sys.stdin.readline().split())
for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())
    if k == 1:
        print(abs(x-y))
    else:
        dist(x,y)



