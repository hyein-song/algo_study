import sys


def dfs(x,y,depth):
    global len_word
    if depth == len_word:
        return 1

    if dp[x][y][depth] != -1:
        return dp[x][y][depth]

    dp[x][y][depth] = 0

    for i in range(1,k+1):
        for j in range(4):
            nx = x + move[j][0] * i
            ny = y + move[j][1] * i
            if 0 <= nx < n and 0 <= ny < m and table[nx][ny] == word[depth]:
                dp[x][y][depth] += dfs(nx,ny,depth+1)

    return dp[x][y][depth]


move = [[0,1],[0,-1],[1,0],[-1,0]]
n, m, k = map(int, sys.stdin.readline().split())

table = []
for _ in range(n):
    table.append(list(sys.stdin.readline().strip()))

word = sys.stdin.readline().strip()
len_word = len(word)
dp = [[[-1 for _ in range(len_word)]for _ in range(m)] for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        if word[0] == table[i][j]:
            result += dfs(i,j,1)

print(result)
for i in range(n):
    for j in range(m):
        for l in range(len_word):
            if dp[i][j][l] != -1:
                print(i,j,l)
                print(dp[i][j][l])