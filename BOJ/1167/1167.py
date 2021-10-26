import collections
import sys


def dfs(x, r):
    global result
    c = 0
    for v, dist in graph[x]:
        if v not in tmp:
            c += 1
            tmp.append(v)
            dfs(v, r+dist)
            tmp.pop()

    if c == 0:
        if result[1] < r:
            result = [x, r]

    return


n = int(sys.stdin.readline())
graph = collections.defaultdict(list)
result = [0,0]
tmp = []
for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    i = nums[0]
    for j in range(1,len(nums)-1, 2):
        graph[i].append([nums[j], nums[j+1]])

tmp.append(1)
dfs(1, 0)
tmp.pop()

result[1] = 0

tmp.append(result[0])
dfs(result[0], 0)
tmp.pop()

print(result[1])


