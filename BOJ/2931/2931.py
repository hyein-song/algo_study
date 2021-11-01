import collections
import sys

def bfs(x,y,pipe):
    q = collections.deque()
    q.append([x,y,pipe])
    visited[x][y] = 1
    while q:
        x, y, pipe = q.popleft()

        for i in can[pipe]:
            nx = x + move[i][0]
            ny = y + move[i][1]
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if table[nx][ny] == '.':
                    # print('bfs',nx,ny)
                    return [nx,ny]
                else:
                    q.append([nx,ny,table[nx][ny]])

def select_pipe(x,y):
    # print(x,y)
    p = set()
    z_tmp = []
    m_tmp = []
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]
        if 0 <= nx < r and 0 <= ny < c and table[nx][ny] != '.':
            if table[nx][ny] == 'Z':
                z_tmp.append(i)
            elif table[nx][ny] == 'M':
                m_tmp.append(i)
            elif i == 0 and table[nx][ny] in ['-', '+', '3', '4']:
                p.add(i)
            elif i == 1 and table[nx][ny] in ['|', '+', '2', '3']:
                p.add(i)
            elif i == 2 and table[nx][ny] in ['|', '+', '1', '4']:
                p.add(i)
            elif i == 3 and table[nx][ny] in ['-', '+', '1', '2']:
                p.add(i)
    # print(p)
    # if len(p) == 0:
    #     p.add(m_tmp[0])
    #     p.add(z_tmp[0])
    if len(p) == 1:
        if z_tmp:
            p.add(z_tmp[0])
        else:
            p.add(m_tmp[0])
    p = tuple(p)
    return x+1, y+1, reverse_can[p]

r, c = map(int, input().split())
table = []
marking = [[0 for _ in range(c)] for _ in range(r)]
can = {'|': [1, 2], '-': [0, 3], '+': [0, 1, 2, 3], '1': [0, 1], '2': [0, 2], '3': [2, 3], '4': [1, 3]}
reverse_can = dict()
for k, v in can.items():
    reverse_can[tuple(v)] = k
visited = [[0 for _ in range(c)] for _ in range(r)]

M = Z = []
for i in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j] == 'M':
            M = [i, j]
            visited[i][j] = 1
        elif tmp[j] == 'Z':
            Z = [i, j]
    table.append(tmp)

move = [[0,1],[1,0],[-1,0],[0,-1]]
start = []
result = []
f = 1
for i in range(4):
    nx = M[0] + move[i][0]
    ny = M[1] + move[i][1]
    if 0 <= nx < r and 0 <= ny < c:
        if table[nx][ny] != '.':
            if i == 0 and table[nx][ny] in ['-','+','3','4']:
                nnx, nny = bfs(nx, ny, table[nx][ny])
                result = select_pipe(nnx,nny)
                f = 0
            elif i == 1 and table[nx][ny] in ['|','+','2','3']:
                nnx, nny = bfs(nx, ny, table[nx][ny])
                result = select_pipe(nnx, nny)
                f = 0
            elif i == 2 and table[nx][ny] in ['|', '+', '1', '4']:
                nnx, nny = bfs(nx, ny, table[nx][ny])
                result = select_pipe(nnx, nny)
                f = 0
            elif i == 3 and table[nx][ny] in ['-', '+', '1', '2']:
                nnx, nny = bfs(nx, ny, table[nx][ny])
                result = select_pipe(nnx, nny)
                f = 0
                # 결과 출력 부분 작성

if f:
    # M 바로 옆이 지워진 파이프
    p = set()
    tmp = []
    x, y = M
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]
        nx2 = x + move[i][0] * 2
        ny2 = y + move[i][1] * 2
        if 0<=nx2<r and 0<= ny2 < c and table[nx2][ny2]!='.':
            if table[nx][ny] == 'M' or table[nx][ny] == 'Z':
                tmp.append(i)
            elif i == 0 and table[nx][ny] in ['-', '+', '3', '4']:
                p.add(i)
            elif i == 1 and table[nx][ny] in ['|', '+', '2', '3']:
                p.add(i)
            elif i == 2 and table[nx][ny] in ['|', '+', '1', '4']:
                p.add(i)
            elif i == 3 and table[nx][ny] in ['-', '+', '1', '2']:
                p.add(i)
        np = p.copy()
        if len(tmp) == 2 and len(p) != 0:
            for t in tmp:
                p.discard(t)
            if len(p) == 0:
                p = np.copy()
        else:
            for t in tmp:
                p.add(t)

        p = tuple(p)
        result = x + 1, y + 1, reverse_can[p]

for r in result:
    print(r,end=' ')