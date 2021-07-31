# -*- coding: utf-8 -*-
"""BOJ_1976.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nM_blyzER5rkrrmdTSpiVe0Y7NGgbzBR
"""

import sys

def find(x):
    if parent[x] == x:
        return x
    else:
        u = find(parent[x])
        parent[x] = u
    return u

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
parent = {i:i for i in range(1,n+1)}

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] == 1:
            union(i+1,j+1)

plan = list(map(int,input().split()))
result = set()

for p in plan:
    parent_p = find(p)
    result.add(parent_p)
    if len(result) > 1:
        print('NO')
        sys.exit(0)
    
print('YES')