import collections
import sys


def move_character():
    q = collections.deque()
    q.append([7,0])
    turn = 0
    visited = [[[0 for _ in range(8)]for _ in range(8)] for _ in range(8)]
    # visited[7][0][turn] = 1
    while q:
        can = []
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(9):
                nx = x + move[i][0]
                ny = y + move[i][1]
                if 0 <= nx < 8 and 0 <= ny < 8 and table[nx][ny] == '.' and visited[nx][ny][turn] == 0:
                    if nx == 0 and ny == 7: # 오른쪽 윗칸으로 이동 가능, 종료
                        return 1
                    visited[nx][ny][turn] = 1
                    can.append([nx,ny])

        # print(can)
        move_wall()
        for cx, cy in can:
            if table[cx][cy] == '.':
                q.append([cx,cy])

        turn += 1
        if turn == 8:
            return 1

    return 0


def move_wall():
    for i in range(7,-1,-1):
        for j in range(8):
            if table[i][j] == '#':
                table[i][j] = '.'
                if i != 7:
                    table[i+1][j] = '#'
    return

move = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
table =[]
start = [7,7]
goal = [0,7]
for _ in range(8):
    table.append(list(sys.stdin.readline().strip()))
print(move_character())



