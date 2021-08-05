# -*- coding: utf-8 -*-
"""BOJ_16562.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1POqhdwPdV91apWRr0gtObBsD98M69dMA
"""

import sys
input = sys.stdin.readline


def find(x):
    if parent[x]==x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if want[a] < want[b]:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int, input().split())
want = [0] + list(map(int, input().split()))
parent = [i for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    union(a, b)

set_parent = set()
result = 0
for i in range(1,n+1):
    set_parent.add(find(i))

for i in set_parent:
    result += want[i]

if result <= k:
    print(result)
else:
    print("Oh no")