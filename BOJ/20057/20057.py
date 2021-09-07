





n = int(input())
mid = n // 2
now = [mid,mid]

move = [[[-1,0,7],[1,0,7],[-2,0,2],[2,0,2],[1,1,1],[-1,1,1],[-1,-1,10],[1,-1,10],[0,-2,5]],
        [[0,-1,7],[0,1,7],[0,-2,2],[0,2,2],[1,1,10],[1,-1,10],[-1,1,1],[-1,-1,1],[2,0,5]],
        [[-1,0,7],[1,0,7],[-2,0,2],[2,0,2],[-1,-1,1],[1,-1,1],[-1,1,10],[1,1,10],[0,2,5]],
        [[0,-1,7],[0,1,7],[0,-2,2],[0,2,2],[-1,1,10],[-1,-1,10],[1,1,1],[1,-1,1],[-2,0,5]]]
directions = [[0,-1],[1,0],[0,1],[-1,0]]
sand = []
for _ in range(n):
    sand.append(list(map(int, input().split())))

result = 0
k = 2
d = 0
for i in range(1,n):
    if i == n-1:
        k = 3
    for _ in range(k):
        for _ in range(i):
            nx = now[0] + directions[d][0]
            ny = now[1] + directions[d][1]
            now = [nx, ny]
            origin = sand[nx][ny]

            for m in move[d]:
                nnx = nx + m[0]
                nny = ny + m[1]
                add_sand = int(sand[nx][ny]*(m[2]/100))
                origin -= add_sand
                if 0 <= nnx < n and 0 <= nny < n:
                    sand[nnx][nny] += add_sand
                else:
                    result += add_sand
            # 알파

            nnx = nx + directions[d][0]
            nny = ny + directions[d][1]
            if 0 <= nnx < n and 0 <= nny < n:
                sand[nnx][nny] += origin
            else:
                result += origin
            sand[nx][ny] = 0
        d = (d + 1) % 4
print(result)