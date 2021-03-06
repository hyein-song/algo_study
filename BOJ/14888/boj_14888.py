# -*- coding: utf-8 -*-
"""BOJ_14888.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dGpp2z5m78bTmF2fiJ6RTQLdaZqlqWUn
"""

import itertools
import sys
# input = sys.stdin.readline

n = int(input())
nums = list(input().split())
tmp = list(map(int, input().split()))
o = ['+','-','*','/']
operator = []
for i in range(4):
    for j in range(tmp[i]):
        operator.append(o[i])
op = set(map(''.join, itertools.permutations(operator)))

results = []
for o in op:
    s = []
    for i in range(n-1):
        s.append(nums[i])
        s.append(o[i])
    s.append(nums[n-1])
    while len(s) > 1:
        tmp = str(int(eval(''.join(s[:3]))))
        del s[:3]
        s.insert(0,tmp)
    results.append(int(s[0]))

print(max(results))
print(min(results))