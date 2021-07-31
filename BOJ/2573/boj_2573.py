# -*- coding: utf-8 -*-
"""BOJ_2573.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LCA9GHVlJovsVDrwzkGmW7_CreKCp4fa
"""

from collections import deque

def bfs(x,y):
    queue.append([x,y])

    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            if b[nx][ny]!=0:
                b[nx][ny]=0
                queue.append([nx,ny]) 

def height():
    for i in range(1,N-1):
        for j in range(1,M-1):
            if a[i][j] == 0:
                continue

            w = 0
            for k in range(4):
                ni = i + mx[k]
                nj = j + my[k]

                if a[ni][nj]==0:
                    w += 1

            if a[i][j]- w > 0 :
                b[i][j] = a[i][j]- w 

# N, M = map(int, input().split())
N, M = 5,7
# a = []

# for i in range(N):
#     a.append(list(map(int, input().split())))

# print(a)
a = [[0, 0, 0, 0, 0, 0, 0], 
     [0, 2, 4, 5, 3, 0, 0], 
     [0, 3, 0, 2, 5, 2, 0], 
     [0, 7, 6, 2, 4, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0]]
# b = [i for i in a[:]] # deepcopy
b = [item[:] for item in a]
cnt = 0
f = 0

mx = [1,-1,0,0]
my = [0,0,1,-1]

queue = deque()

while True :
    f = 0

    # 처음 발견한 얼음의 빙산을 모두 0으로 만듬
    for i in range(1,N-1):
        for j in range(1,M-1):
            if b[i][j]==0:
                continue
            bfs(i,j)
            f = 1
            break
        if f :
            break

    b_element = [e for row in b for e in row if e==0]
    if len(b_element) != (N*M):
        break

    height()
    cnt += 1 
    a = [item[:] for item in b]

    # 얼음이 전부 0인지 확인
    b_element = [e for row in b for e in row if e ==0]
    if len(b_element) == (N*M):
        break
    
    
if len(b_element) == N*M:
    print('0')
else:
    print(cnt)