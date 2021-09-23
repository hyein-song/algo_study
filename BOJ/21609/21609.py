import collections
import copy
import sys
input = sys.stdin.readline


def bfs(x,y,color):
    q = collections.deque()
    q.append([x,y])
    rainbow = []
    cnt = 0
    all_position = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and (table[nx][ny] == color or table[nx][ny] == 0):
                if table[nx][ny] == 0:
                    rainbow.append([nx, ny])

                q.append([nx, ny])
                visited[nx][ny] = 1
                cnt += 1
                all_position.append([nx, ny, table[nx][ny]])

    for r1,r2 in rainbow:
        visited[r1][r2] = 0
    return all_position, cnt


def select_block_group(positions):
    can = []
    for idx, position in enumerate(positions):
        rainbow = 0
        row = []
        col = []
        for pp in position:
            if pp[2] == 0:
                rainbow += 1
            else:
                row.append(pp[0])
                col.append(pp[1])

        can.append([idx,len(position),rainbow,min(row),min(col)])
    can = sorted(can, key = lambda x: (x[2],x[3],x[4]), reverse=True)

    return positions[can[0][0]]


def gravity():
    for i in range(n):
        bottom = n-1
        for j in range(n-1, -1, -1): # 맨 아래서부터 탐색
            if table[j][i] == -2: # 빈칸
                continue
            elif table[j][i] == -1: # 검정
                bottom = j-1
            else:
                table[bottom][i] = table[j][i]
                if bottom != j:
                    table[j][i] = -2
                    bottom -=1
                else:
                    bottom = j-1

def ccw():
    global table
    new_table = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_table[i][j] = table[j][n-i-1]
    table = copy.deepcopy(new_table)
    return


move = [[0,1],[0,-1],[1,0],[-1,0]]
n,m = map(int, input().split())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

result = 0
while True:
    max_cnt = 2
    max_positions = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and table[i][j] > 0 :
                p, count = bfs(i, j, table[i][j])
                if count > max_cnt:
                    max_positions = [p]
                    max_cnt = count
                elif count == max_cnt:
                    max_positions.append(p)
    len_positions = len(max_positions)
    if len_positions == 0:
        print(result)
        break
    elif len_positions == 1:
        for xx, yy,c in max_positions[0]:
            table[xx][yy] = -2
    else: # 2개 이상
        selected = select_block_group(max_positions)
        for xx, yy,c in selected:
            table[xx][yy] = -2
    result += pow(max_cnt,2)
    gravity()
    ccw()
    gravity()


