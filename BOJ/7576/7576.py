import collections
import sys
input = sys.stdin.readline


def bfs(all_tomato):
    q = collections.deque()
    q.extend(tomato)
    cnt = 1

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + move[i][0]
                ny = y + move[i][1]
                if 0 <= nx < n and 0 <= ny < m and table[nx][ny] == 0:
                    table[nx][ny] = 1
                    all_tomato -= 1
                    if all_tomato == 0:
                        return cnt
                    q.append([nx, ny])
        cnt += 1
    return -1


m, n = map(int, input().split())
all_tomato = 0
table = []
tomato = []
move = [[1,0],[-1,0],[0,1],[0,-1]]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 0:
            all_tomato += 1
        elif tmp[j] == 1:
            tomato.append([i, j])
    table.append(tmp)

if all_tomato == 0:
    print(0)
else:
    print(bfs(all_tomato))
