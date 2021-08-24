import sys
input=sys.stdin.readline

def spread():
    new_room = [[0 for _ in range(c)]for _ in range(r)]
    for cl in cleaner:
        new_room[cl[0]][cl[1]] = -1

    while dust:
        i, j = dust.pop()
        origin_dust = room[i][j]
        if origin_dust < 5:
            new_room[i][j] += origin_dust
            continue
        spread_dust = origin_dust // 5
        cnt = 0
        for k in range(4):
            ni = i + move[k][0]
            nj = j + move[k][1]
            if 0 <= ni < r and 0 <= nj < c and room[ni][nj] != -1:
                new_room[ni][nj] += spread_dust
                cnt += 1
        new_room[i][j] += origin_dust - spread_dust*cnt

    return new_room

def air_cleaner():
    upper = cleaner[0]
    lower = cleaner[1]
    ccw = []
    cw = []
    # ccw
    start = upper[:]
    for d in [2,1,0,3]:
        while True:
            ni = start[0] + move[d][0]
            nj = start[1] + move[d][1]
            if ni < 0 or ni > upper[0] or nj <0 or nj >=c or room[ni][nj]==-1:
                break
            ccw.append([ni, nj])
            start = [ni, nj]

    for i in range(len(ccw)-1):
        room[ccw[i][0]][ccw[i][1]] = room[ccw[i+1][0]][ccw[i+1][1]]

    room[ccw[-1][0]][ccw[-1][1]] = 0

    # cw
    start = lower[:]
    for d in range(4):
        while True:
            ni = start[0] + move[d][0]
            nj = start[1] + move[d][1]
            if ni < lower[0] or ni >= r or nj < 0 or nj >= c or room[ni][nj] == -1:
                break
            cw.append([ni, nj])
            start = [ni, nj]
    for i in range(0, len(cw) - 1):
        room[cw[i][0]][cw[i][1]] = room[cw[i + 1][0]][cw[i + 1][1]]

    room[cw[-1][0]][cw[-1][1]] = 0


def check_dust():
    for i in range(r):
        for j in range(c):
            if room[i][j] != 0 and room[i][j] != -1:
                dust.append([i,j])

r, c, t = map(int, input().split())
room = []
cleaner = []
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dust = []
for i in range(r):
    tmp = list(map(int, input().split()))
    for j in range(c):
        if tmp[j] == -1:
            cleaner.append([i,j])
        elif tmp[j] != 0:
            dust.append([i,j])
    room.append(tmp)

for _ in range(t):
    room = spread()
    # room = [i[:] for i in new_room]
    air_cleaner()
    check_dust()

result = 2
for i in room:
    result += sum(i)
print(result)
