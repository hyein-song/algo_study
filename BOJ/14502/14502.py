import collections

def spread_virus(table, walls, cnt_safe):
    new_table = [i[:] for i in table]
    for w in walls:
        new_table[blank[w][0]][blank[w][1]] = 1

    Q = collections.deque(virus)
    while Q:
        i, j = Q.popleft()
        for x in range(4):
            ni = i + move[0][x]
            nj = j + move[1][x]
            if 0<= ni < n and 0 <= nj < m and new_table[ni][nj]== 0:
                new_table[ni][nj] = 2
                cnt_safe -= 1
                Q.append([ni, nj])
    return cnt_safe

n, m = map(int, input().split())
move = [[0, 0, -1, 1], [1, -1, 0, 0]]
table = []
blank = []
virus = []
result = 0

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(m):
        if tmp[j] == 0:
            blank.append([i, j])
        elif tmp[j] == 2:
            virus.append([i, j])
    table.append(tmp)

len_blank = len(blank)

for i in range(len_blank-2):
    for j in range(i+1,len_blank-1):
        for k in range(j+1,len_blank):
            cnt_safe = spread_virus(table, [i,j,k], len_blank - 3)
            result = max(result, cnt_safe)

print(result)
