import sys


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    d = list(map(int, sys.stdin.readline().split()))
    time_list = d[:]

    buildings = {i: [] for i in range(n)}
    cnt_parent = [0 for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        buildings[x-1].append(y-1)
        cnt_parent[y-1] += 1

    w = int(sys.stdin.readline().strip())
    stack = []
    for i in range(n):
        if cnt_parent[i] == 0:
            stack.append(i)

    while stack:
        x = stack.pop()
        for j in buildings[x]:
            time_list[j] = max(time_list[j], time_list[x]+d[j])
            cnt_parent[j] -= 1
            if cnt_parent[j] == 0:
                stack.append(j)

    print(time_list[w-1])

