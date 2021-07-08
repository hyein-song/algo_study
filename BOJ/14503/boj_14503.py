# -*- coding: utf-8 -*-
"""BOJ_14503.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14-J2BKLtwL9gVA68omdkgAM43T__ZzQe
"""

N, M = map(int, input().split())
r,c,d = map(int,input().split())
a = []

for i in range(N):
    a.append(list(map(int, input().split())))

mx_left = [0,-1,0,1]
my_left = [-1,0,1,0]
mx_back = [1,0,-1,0]
my_back = [0,-1,0,1]

def dfs(x,y,d):
    global cnt
    global cnt2
    
    f_d = d
  
    #1 현재 위치 청소
    if a[x][y] == 0:
        a[x][y] = 2

    # a 
    nx = x+mx_left[d]
    ny = y+my_left[d]
    if a[nx][ny] == 0:
        d = (d+3) % 4
        cnt = 0
        dfs(nx,ny,d)
    else: #b
        cnt +=1
        d = (d+3) % 4
        if cnt != 4:
            dfs(x,y,d)
    
    if cnt == 4:
        cnt = 0
        nx_back = x+mx_back[d]
        ny_back = y+my_back[d]
        if a[nx_back][ny_back] != 1: # c
            cnt2 = 0 
            dfs(nx_back,ny_back,d)
        else:
            cnt2 +=1
    if cnt2 == 4: #d
        return

   
cnt = 0
cnt2 = 0
dfs(r,c,d)
count_wash = [e for row in a for e in row if e ==2]
print(len(count_wash))