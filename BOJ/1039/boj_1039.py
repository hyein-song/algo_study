# -*- coding: utf-8 -*-
"""BOJ_1039.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17oyZyoGmf5KNUuaYVrW6M8_Iq5bk8aX0
"""

import collections

N, K = input().split()
K = int(K)
Q = collections.deque()
Q.append(N)

while Q:
    tmp = set()
    for i in range(len(Q)):
        value = Q.popleft()
       
        for i in range(len(value)):
            for j in range(i+1,len(value)):
                new_value = list(value)
                new_value[i], new_value[j] = new_value[j], new_value[i]
                if new_value[0] != '0' :
                    tmp.add(''.join(new_value))
    
    for i in tmp:
        Q.append(i)
    K -= 1
    if K == 0 and Q:
        print(''.join(max(Q)))
        break

if K != 0 or not Q:
    print(-1)

