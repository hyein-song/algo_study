# -*- coding: utf-8 -*-
"""BOJ_11657.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gnEY425josVMed-Cay3rJslvOkEhRIB4
"""

import collections
import sys

max_value = sys.maxsize
N , M = map(int,input().split())

graph = {i:[] for i in range(1, N+1)}
cycle = False
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])

dist = {i:max_value for i in graph}
dist[1] = 0

for _ in range(len(graph)-1):
    for node in graph:
        for destination, time in graph[node]:
            if dist[node] != max_value and dist[destination] > dist[node]+time:
                dist[destination] = dist[node]+time

for node in graph:
    for destination, time in graph[node]:
        if dist[destination] != max_value and dist[destination] > dist[node]+time :
            cycle = True
 
if cycle:
    print(-1)
else:
    for dest, time in dist.items():
        if dest == 1:
            continue
        elif time == max_value:
            print(-1)
        else:
            print(time)