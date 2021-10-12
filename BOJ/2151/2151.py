import collections


def bfs():
    q = collections.deque()
    for i in range(4):
        q.append([doors[0][0],doors[0][1],i,0])
    # visited = [[0 for _ in range(n)] for _ in range(n)]
    while q:
        i, j, d, cnt = q.popleft()

        while True:
            i += move[d][0]
            j += move[d][1]
            if i < 0 or i >= n or j < 0 or j >= n or table[i][j] == '*':
                break
            if table[i][j] == '!':
                table[i][j] = '.'
                if d == 0 or d == 2:
                    q.append([i, j, 1, cnt + 1])
                    q.append([i, j, 3, cnt + 1])
                elif d == 1 or d == 3:
                    q.append([i, j, 2, cnt + 1])
                    q.append([i, j, 0, cnt + 1])
            elif [i, j] == doors[1]:
                return cnt
    return -1


move = [[1,0],[0,-1],[-1,0],[0,1]]
n = int(input())
table = []
doors = []
for i in range(n):
    tmp = list(input())
    for j in range(n):
        if tmp[j] == '#':
            doors.append([i,j])
    table.append(tmp)
print(bfs())

