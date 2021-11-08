import heapq
import math
import sys


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a,b):
    a = find(a)
    b = find(b)
    if a > b :
        parent[a] = b
    else:
        parent[b] = a


n = int(sys.stdin.readline().strip())
stars = []
for _ in range(n):
    stars.append(list(map(float, sys.stdin.readline().split())))

dist = []
for i in range(n):
    for j in range(i+1,n):
        calc = math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
        dist.append([i,j,calc])

dist = sorted(dist, key= lambda x : x[2])
# print(dist)
parent = [i for i in range(n)]
result = 0
for a,b,c in dist:
    if find(a) != find(b):
        union(a, b)
        result += c

print(round(result,2))








