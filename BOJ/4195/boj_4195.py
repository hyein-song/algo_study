# -*- coding: utf-8 -*-
"""BOJ_4195.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h43s_w-B_CK3m0qKQbVsg9Wx6FplEWBJ
"""

import collections
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a==b:
        return   
    elif a < b:
        parent[b] = a
        cnt[a] += cnt[b]
    else:
        parent[a] = b
        cnt[b] += cnt[a]

t = int(input())

parent = collections.defaultdict(str)
cnt = {}
for i in range(t):
    f = int(input())
    parent.clear()
    for j in range(f):
        a,b = input().split()
        if a not in parent:
            parent[a] = a
            cnt[a] = 1
        if b not in parent:
            parent[b] = b
            cnt[b] = 1
        union(a,b)
        p_a = find(a)
        print(cnt[p_a])