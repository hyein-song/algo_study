import collections
import sys


def bfs(s, target):
    global g
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[s[0]][s[1]] = 1
    q = collections.deque()
    q.append(s)
    distances = []
    cnt = 1
    for j in target:
        if s[0] == j[0] and s[1] == j[1]:
            return [0, s[0], s[1]]

    while q and target:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x+move[0][i]
                ny = y+move[1][i]
                if 0 <= nx < n and 0 <= ny < n and table[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    for j in target:
                        if nx == j[0] and ny == j[1]:
                            distances.append([cnt, nx, ny])
                            break

                    q.append([nx, ny])
        if distances:
            distances.sort()
            g -= distances[0][0]
            if g < 0:
                return -1
            return distances[0]
        cnt += 1

    return -1


n, m, g = map(int, input().split())
move = [[0,0,1,-1],[1,-1,0,0]]
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

a,b = list(map(int, input().split()))
start = [a-1, b-1]
passenger = []
for _ in range(m):
    a,b,c,d = list(map(int, input().split()))
    passenger.append([a-1,b-1,c-1,d-1])

destination = []
for _ in range(m):
    selected_p = bfs(start, passenger)
    if selected_p == -1:
        print(-1)
        sys.exit(0)
    for p in passenger:
        if p[0] == selected_p[1] and p[1] == selected_p[2]:
            destination = p[2:]
            passenger.remove(p)

    d = bfs(selected_p[1:3], [destination])
    if d == -1:
        print(-1)
        sys.exit(0)

    g += d[0] * 2
    start = d[1:]

print(g)