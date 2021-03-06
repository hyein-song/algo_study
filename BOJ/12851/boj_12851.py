# -*- coding: utf-8 -*-
"""BOJ_12851.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14iMrvCcYUiBh2SllYCoYuAt0__e9Z_pM
"""

from collections import deque

def bfs(x):
    q.append(x)
    m[x] = 0
    fast[x] = 1
    cnt = 0

    while q:
        x = q.popleft()
        
        if 0 <= x-1 <= 100000:
            if m[x-1] >= m[x]+1 :
                m[x-1] = m[x]+1
                fast[x-1] += 1
                q.append(x-1)

        if 0 <= x+1 <= 100000:
            if m[x+1] >= m[x]+1 :
                m[x+1] = m[x]+1
                fast[x+1] += 1
                q.append(x+1)

        if 0 <= 2*x <= 100000:
            if m[2*x] >= m[x]+1:
                m[2*x] = m[x]+1
                fast[2*x] += 1
                q.append(2*x)

N, K = map(int, input().split())

m = [100000]*100001
fast = [0]*100001
q = deque()

bfs(N)

print(m[K])
print(fast[K])