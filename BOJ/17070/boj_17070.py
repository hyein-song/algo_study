# -*- coding: utf-8 -*-
"""BOJ_17070.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E0nfacOGGjv2af0pSdTaR1PmALE6My3U
"""

# 시간초과 
def dfs(a, b, s, p):
    global cnt
    global board
    if a > N or b > N or board[a-1][b-1] == 1:
        return 

    if s == 2:
        if board[a-2][b-1] == 1 or board[a-1][b-2] == 1:
            return
    if a == N and b == N:
        cnt += 1
        return
   
    # 가로
    if s == 0:
        #가로
        dfs(a,b+1,0,[[a,b],[a,b+1]])

        # 대각선
        dfs(a+1,b+1,2,[[a,b],[a+1,b+1]])
    # 세로
    elif s == 1:
        # 세로
        dfs(a+1,b,1,[[a,b],[a+1,b]])

        # 대각선 
        dfs(a+1,b+1,2,[[a,b],[a+1,b+1]])

    # 대각선
    else:
        #가로
        dfs(a,b+1,0,[[a,b],[a,b+1]])
        
        #세로
        dfs(a+1,b,1,[[a,b],[a+1,b]])

        #대각선
        dfs(a+1,b+1,2,[[a,b],[a+1,b+1]])

N = int(input())
board = []
cnt = 0
pipe = [[1,1],[1,2]]
shape = 0
for i in range(N):
    board.append(list(map(int, input().split())))

dfs(1, 2, shape, pipe)

print(cnt)

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
dp = [[[0] * (3) for _ in range(n+1)] for _ in range(n+1) ]
dp[1][2][0] =1

for i in range(3,n+1):
    if board[0][i-1] == 0:
        dp[1][i][0] = dp[1][i-1][0]    

for i in range(2,n+1):
    for j in range(3,n+1):
        if board[i-1][j-1] == 0 and board[i-2][j-1] == 0 and board[i-1][j-2] == 0:
            dp[i][j][2]= dp[i-1][j-1][2]+dp[i-1][j-1][1]+dp[i-1][j-1][0]
        if board[i-1][j-1] == 0:
            dp[i][j][0]= dp[i][j-1][2]+dp[i][j-1][0]
            dp[i][j][1]= dp[i-1][j][2]+dp[i-1][j][1]
        

print(dp[n][n][0]+dp[n][n][1]+dp[n][n][2])