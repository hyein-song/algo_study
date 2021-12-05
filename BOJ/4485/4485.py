import collections
import sys

def bfs():
    q = collections.deque()
    q.append([0,0,table[0][0]])
    visited = [[[0,0] for _ in range(n)] for _ in range(n)]
    visited[0][0] = [1,table[0][0]]

    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                n_cnt = table[nx][ny] + cnt
                if visited[nx][ny][0] == 0 or (visited[nx][ny][0] == 1 and n_cnt < visited[nx][ny][1]):
                    visited[nx][ny] = [1,n_cnt]
                    q.append([nx,ny,n_cnt])
    return visited[-1][-1][1]

move = [[-1,0],[1,0],[0,-1],[0,1]]
j = 1
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    table = []
    for i in range(n):
        table.append(list(map(int, sys.stdin.readline().split())))

    result = bfs()
    print('Problem {}: {}'.format(j, result))
    j += 1