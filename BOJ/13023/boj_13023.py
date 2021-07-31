# -*- coding: utf-8 -*-
"""BOJ_13023.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gq2CSxozmUHh4uwdqyr59CWN0SZHW7BR
"""

N, M = map(int, input().split())
friends = {i:[] for i in range(N)} 
for i in range(M):
    a, b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

tmp = []
result = 0


def dfs(x):
    global result
    if len(tmp) == 5:
        result = 1
        return 

    if len(friends[x]) == 0 or friends[x] in tmp:
        return

    for val in friends[x]:
        if val in tmp:
            continue
        tmp.append(val)
        dfs(val)
        tmp.pop()

for key in friends.keys():
    if friends[key] is not None:
        tmp.append(key)
        dfs(key)
        tmp.pop()

        if result:
            break

print(result)