# -*- coding: utf-8 -*-
"""BOJ_10800.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-0pV1EfMEx8MYsoIl9swz4eZLwzuYKvU
"""

import copy
import collections
import sys
input = sys.stdin.readline

n = int(input())
ball = [[0,0,0]]

for i in range(n):
    ball.append([i+1]+list(map(int, input().split())))
ball = sorted(ball, key=lambda x: [x[2]])

total = 0
color = collections.defaultdict(int)
j = 0
ans = [[0,0]] * (n+1)
for i in range(1,n+1):
    while ball[i][2] > ball[j][2]:
        total += ball[j][2]
        color[ball[j][1]] += ball[j][2]
        j += 1
    ans[i] = ([ball[i][0]]+ [total-color[ball[i][1]]])

ans = sorted(ans)

for i in range(1,n+1):
    print(ans[i][1])