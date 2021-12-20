# 0들의 그룹 수를 구한다음
# 1에서 인접한 위치의 그룹 수를 더해줌
import collections
import sys


def bfs(x, y, gid):
    q = collections.deque()
    q.append([x, y])
    cnt = 1
    visited[x][y] = 1
    group[x][y] = gid
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]
            if 0 <= nx < n and 0 <= ny < m and table[nx][ny] == '0' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                q.append([nx,ny])
                group[nx][ny] = gid
    count[gid] = cnt
    return


move = [[0,1],[0,-1],[1,0],[-1,0]]
n, m = map(int, sys.stdin.readline().split())
count = dict()
gid = 1
table = []
for i in range(n):
    table.append(list(sys.stdin.readline().rstrip()))

group = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if table[i][j] == '0' and visited[i][j] == 0:
            bfs(i, j, gid)
            gid += 1
# print('group', group)
# print(count)

for i in range(n):
    for j in range(m):
        calc = 1
        if table[i][j] == '1':
            visited_group = set()
            for k in range(4):
                ni = i + move[k][0]
                nj = j + move[k][1]
                if 0 <= ni < n and 0 <= nj < m and group[ni][nj] !=0:
                    visited_group.add(group[ni][nj])
            for gg in visited_group:
                calc += count[gg]
            print(calc%10, end = '')
        else:
            print(0,end='')
    if i == n-1:
        break
    print()
