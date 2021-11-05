import collections
import math
import sys

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]
nums = []
edges = []
for _ in range(n):
    nums.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    x1, y1 = nums[i]
    for j in range(n):
        if i != j:
            x2, y2 = nums[j]
            d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            edges.append([i,j,d])

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges.append([a-1,b-1, 0])

edges = sorted(edges, key=lambda x:x[2])
result = 0
for i in range(len(edges)):
    a, b, c = edges[i]
    if find(a) != find(b):
        union(a, b)
        result += c

print("{:.2f}".format(result))
