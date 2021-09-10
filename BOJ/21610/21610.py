import collections
import sys
input = sys.stdin.readline

def move(d,s):
    add_water = []
    c_dict = collections.defaultdict(int)
    for _ in range(len(cloud)):
        x, y = cloud.popleft()
        nx = (x + directions[d][0]*s) % n
        ny = (y + directions[d][1]*s) % n
        table[nx][ny] += 1
        c_dict[(nx,ny)] = 1

    for nx,ny in c_dict.keys():
        cnt = 0
        for i in range(1, 8, 2):
            nnx = nx + directions[i][0]
            nny = ny + directions[i][1]
            if 0 <= nnx < n and 0 <= nny < n and table[nnx][nny] != 0:
                cnt += 1
        add_water.append([nx, ny, cnt])

    for x,y,c in add_water:
        table[x][y] += c

    for i in range(n):
        for j in range(n):
            if table[i][j] >= 2 and (not c_dict[(i,j)]):
                cloud.append([i,j])
                table[i][j] -= 2
    return


n, m = map(int, input().split())
cloud = collections.deque()
cloud.extend([[n-1,0],[n-1,1],[n-2,0],[n-2,1]])
directions = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

for _ in range(m):
    d,s = map(int, input().split())
    move(d-1,s)

result = 0
for i in range(n):
    for j in range(n):
        result += table[i][j]

print(result)