import collections
import sys


def find(x):
    if x == parent[x]:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]


def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, sys.stdin.readline().split())
parent = [i for i in range(v)]
edges = []

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append([a-1,b-1,c])

edges = sorted(edges, key= lambda x:x[2])
result = 0
for i in range(len(edges)):
    a,b,c = edges[i]
    if find(a) != find(b):
        union(a,b)
        result += c
print(result)

