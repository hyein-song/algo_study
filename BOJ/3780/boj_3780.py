# -*- coding: utf-8 -*-
"""BOJ_3780

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZfdcBeAL1KiLnOejqSwnVJh5tDVWlwW-
"""

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    else:
        tmp = find(parent[x])
        dist[x] += dist[parent[x]]
        parent[x] = tmp
        return parent[x]

t = int(input())

for i in range(t):
    n = int(input())
    dist = [0] * (n+1)
    parent = [i for i in range(n+1)]
    center = 0
    while True:
        line = list(input().split())
        if line[0] == 'E':
            t = int(line[1])
            find(t)
            print(dist[t])
        elif line[0] == 'I':
            a,b = int(line[1]), int(line[2])
            parent[a] = b
            dist[a] = abs(a-b) % 1000
        elif line[0] == 'O':
            break