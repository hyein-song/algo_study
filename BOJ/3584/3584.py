import collections
import sys

def tracking_tree(start):

    tracking = [start]
    s = start
    while graph[s] != 0:
        tracking.append(graph[s])
        s = graph[s]

    return tracking

def LCA(x,y):
    x_list = tracking_tree(x)
    y_list = tracking_tree(y)

    x_depth = len(x_list)
    y_depth = len(y_list)

    x_idx = 0
    y_idx = 0

    if x_depth < y_depth:
        y_idx = (y_depth-x_depth)
    elif x_depth > y_depth:
        x_idx = (x_depth-y_depth)

    for i in range(min(x_depth, y_depth)):
        if x_list[x_idx+i] == y_list[y_idx+i]:
            return x_list[x_idx+i]


T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    graph = collections.defaultdict(int)

    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        graph[b] = a

    x, y = map(int, sys.stdin.readline().split())
    print(LCA(x, y))