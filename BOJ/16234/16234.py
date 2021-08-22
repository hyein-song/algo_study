import collections
import sys
input = sys.stdin.readline

def bfs(i, j):
    union = set()
    union.add((i, j))
    union_sum = table[i][j]
    union_cnt = 1
    Q = collections.deque()
    Q.append([i, j])

    while Q:
        i, j = Q.popleft()
        for k in range(4):
            ni = i + move[0][k]
            nj = j + move[1][k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and L <= abs(table[i][j] - table[ni][nj]) <= R:
                visited[ni][nj] = 1
                union_sum += table[ni][nj]
                union_cnt += 1
                union.add((ni, nj))
                Q.append([ni, nj])

    if union_cnt > 1:
        new_people = union_sum // union_cnt
        for k, l in union:
            table[k][l] = new_people
        return True
    return False


n, L, R = map(int, input().split())
move = [[0, 0, 1, -1], [1, -1, 0, 0]]
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

total_table = [[i,j] for i in range(n) for j in range(n)]

cnt = 0
while True:
    visited = [[0 for _ in range(n)]for _ in range(n)]
    t = 0
    for i, j in total_table:
        if not visited[i][j]:
            visited[i][j] = 1
            if bfs(i, j):
                t += 1
    if t == 0:
        break
    cnt += 1

print(cnt)