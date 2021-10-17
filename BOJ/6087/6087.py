import collections
import sys

def bfs():
    x, y = c[0]
    q = collections.deque()
    visited = [[sys.maxsize for _ in range(w)] for _ in range(h)]
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]
        if 0 <= nx < h and 0 <= ny < w and table[nx][ny] != '*':
            q.append([x,y,i,1])
            visited[nx][ny] = 1
    visited[x][y] = 1
    while q:
        x, y, d, val = q.popleft()
        if visited[x][y] != val:
            continue
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]
            if 0 <= nx < h and 0 <= ny < w and table[nx][ny] != '*':
                if d == i:
                    if visited[nx][ny] >= visited[x][y]:
                        visited[nx][ny] = visited[x][y]
                        q.append([nx, ny, i, visited[nx][ny]])
                else:
                    if visited[nx][ny] >= visited[x][y]+1:
                        visited[nx][ny] = visited[x][y]+1
                        q.append([nx, ny, i, visited[nx][ny]])

    return visited[c[1][0]][c[1][1]]-1

move = [[1,0],[-1,0],[0,1],[0,-1]]
w, h = map(int, input().split())
table = []
c = []
for i in range(h):
    tmp = list(input())
    for j in range(w):
        if tmp[j] == 'C':
            c.append([i,j])
    table.append(tmp)
print(bfs())

