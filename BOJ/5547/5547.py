import collections

w, h = map(int, input().split())
table = [[0]*(w+2)]
for i in range(h):
    tmp = [0] + list(map(int, input().split())) + [0]
    table.append(tmp)
table.append([0]*(w+2))
answer = 0

# x가 홀
move1 = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[0,-1]]
# x 가 짝
move2 = [[-1,-1],[-1,0],[0,1],[1,0],[1,-1],[0,-1]]

visited = [[0 for _ in range(w+2)] for _ in range(h+2)]

q = collections.deque()
q.append([0,0])

while q:
    x, y = q.popleft()
    if x % 2 == 1:
        m = move1
    else:
        m = move2
    for i in range(6):
        nx = x + m[i][0]
        ny = y + m[i][1]

        if nx < 0 or ny < 0 or nx >= h+2 or ny >= w+2:
            continue

        if not visited[nx][ny] and table[nx][ny] == 0:
            q.append([nx,ny])
            visited[nx][ny] = 1


for x in range(1,h+1):
    for y in range(1,w+1):
        if table[x][y] == 0:
            continue
        if x % 2 == 1:
            m = move1
        else:
            m = move2

        for i in range(6):
            nx = x + m[i][0]
            ny = y + m[i][1]

            if visited[nx][ny] == 1:
                answer += 1

print(answer)
