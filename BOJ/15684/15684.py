import sys
input = sys.stdin.readline

def check():
    for i in range(n):
        row = 0
        col = i
        for _ in range(h):
            if table[row][col] == 1:
                tmp = table[row]
                cnt_1 = sum(tmp[:col+1])
                if cnt_1 % 2 == 1:
                    col += 1
                else:
                    col -= 1
            row += 1

        if i != col:
            return False
    return True


def dfs(a, d):
    global result
    if d == 4:
        return

    if check():
        if result > d:
            result = d
        return

    for i in range(a, h, 1):
        for j in range(n-1):
            if table[i][j] == 0 and table[i][j+1] == 0 and visited[i][j] == 0:
                visited[i][j] = 1
                table[i][j] = 1
                table[i][j+1] = 1
                dfs(i, d+1)
                visited[i][j] = 0
                table[i][j] = 0
                table[i][j + 1] = 0
    return


n, m, h = map(int, input().split())
table = [[0 for _ in range(n)] for _ in range(h)]
visited = [[0 for _ in range(n)] for _ in range(h)]
result = 5
for _ in range(m):
    a, b = map(int, input().split())
    table[a-1][b-1] = 1
    table[a-1][b] = 1

dfs(0, 0)
if result == 5:
    print(-1)
else:
    print(result)

