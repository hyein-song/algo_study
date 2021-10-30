import collections
import sys


def bfs():
    q = collections.deque()
    q.append([0,0,0])
    visited = [[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    dist = 1
    while q:
        for _ in range(len(q)):
            x, y, cnt = q.popleft()

            for i in range(4):
                nx = x + move[i][0]
                ny = y + move[i][1]
                if 0 <= nx < n and 0 <= ny < m:
                    if nx == n - 1 and ny == m - 1:
                        return dist + 1
                    if table[nx][ny] == 1 and cnt < k and visited[nx][ny][cnt] == 0:
                            q.append([nx, ny, cnt + 1])
                            visited[nx][ny][cnt] = 1

                    elif table[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                        visited[nx][ny][cnt] = 1
                        q.append([nx,ny,cnt])
        dist += 1

    return -1

move = [[0,1],[0,-1],[1,0],[-1,0]]
n, m, k = map(int, sys.stdin.readline().split())
table = []
for _ in range(n):
    input_nums = sys.stdin.readline().strip()
    tmp = []
    for i in input_nums:
        tmp.append(int(i))
    table.append(tmp)

if n == 1 and m == 1:
    print(1)
else:
    print(bfs())
