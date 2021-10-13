import collections
import copy


def breaking(d, a):
    if d == 0:
        for i in range(c):
            if cave[r-a][i] == 'x':
                cave[r-a][i] = '.'
                return 0
    else:
        for i in range(c-1,-1,-1):
            if cave[r-a][i] == 'x':
                cave[r-a][i] = '.'
                return 0
    return 1


def bfs(x,y):
    q = collections.deque()
    q.append([x,y])
    cluster = [[x,y]]
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]
            if 0 <= nx < r and 0 <= ny < c and cave[nx][ny] == 'x' and visited[nx][ny]==0:
                visited[nx][ny] = 1
                q.append([nx,ny])
                cluster.append([nx,ny])
    return cluster


def down(cluster):
    cnt = down_cnt(cluster)
    cluster = sorted(cluster, reverse=True)
    for a, b in cluster:
        cave[a][b] = '.'
        cave[a+cnt][b] = 'x'


def down_cnt(cluster):
    tmp = 0
    cc = copy.deepcopy(cluster)
    while True:
        for idx, c in enumerate(cc):
            a, b = c
            na = a + 1
            if na >= r or (cave[na][b] != '.' and [na, b] not in cluster):
                return tmp
            cc[idx][0] = na
        tmp += 1


move = [[1,0],[-1,0],[0,1],[0,-1]]
r, c = map(int, input().split())
cave = []
for i in range(r):
    cave.append(list(input()))
n = int(input())
height = list(map(int, input().split()))
for i in range(n):
    a = height[i]
    d = i % 2 # 0 오른쪽, 1 왼쪽
    if breaking(d, a):
        continue

    visited = [[0 for _ in range(c)] for _ in range(r)]
    clusters = []
    for x in range(r-1,-1,-1):
        for y in range(c-1,-1,-1):
            if cave[x][y] == 'x' and visited[x][y] == 0:
                clusters.append(bfs(x, y))

    for k in range(len(clusters)):
        f = 1
        for c1, c2 in clusters[k]:
            if c1 == r-1:
                f = 0
                break
        if f:
            down(clusters[k])
            break

for i in range(r):
    for j in range(c):
        print(cave[i][j], end='')
    if i != r-1:
        print()