# -*- coding: utf-8 -*-
"""BOJ_11085.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tkaeZnP0PkVjC3h38_VFqGT54oc7vkTq
"""

import collections

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

p, w = map(int, input().split())
c, v  = map(int, input().split())

parent = [i for i in range(p)]

graph = []

for _ in range(w):
    start, end, width = map(int, input().split())
    graph.append([start, end, width])
graph = sorted(graph, key = lambda x : x[2], reverse=True)

for g in graph:
    union(g[0], g[1])
    if find(c) == find(v):
        print(g[2])
        break