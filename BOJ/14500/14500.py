


def dfs(i,j,d,cnt):
    global max_val
    if cnt + table_max * (4-d) <= max_val:
        return

    if d == 4:
        max_val = max(max_val, cnt)
        return

    for k in range(4):
        ni = i + move[0][k]
        nj = j + move[1][k]
        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0:
            if d == 2:
                visited[ni][nj] = 1
                dfs(i, j, d + 1, cnt + table[ni][nj])
                visited[ni][nj] = 0

            visited[ni][nj] = 1
            dfs(ni, nj, d+1, cnt+table[ni][nj])
            visited[ni][nj] = 0


n, m = map(int, input().split())
table = []
move = [[0,0,1,-1],[1,-1,0,0]]
visited = [[0 for _ in range(m)] for _ in range(n)]
max_val = 0
for _ in range(n):
    table.append(list(map(int, input().split())))
table_max = max(max(*table))
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,1,table[i][j])
        visited[i][j] = 0

print(max_val)