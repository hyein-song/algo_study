import collections


def moved():
    for i in fire.keys():
        if fire[i]:
            r, c, mm, s, d = fire[i]
            table[r][c].remove(i)

            move_cnt = s % n
            new_r = r + move[d][0] * move_cnt
            new_c = c + move[d][1] * move_cnt

            if new_r >= n:
                new_r -= n
            elif new_r < 0:
                new_r += n
            if new_c >= n:
                new_c -= n
            elif new_c < 0:
                new_c += n

            fire[i] = [new_r, new_c, mm, s, d]
            table[new_r][new_c].append(i)


def merged():
    global m
    for i in range(n):
        for j in range(n):
            len_table_ij = len(table[i][j])
            if len_table_ij >= 2:
                sum_mm = sum_s = check_d = 0
                for kk in table[i][j]:
                    sum_mm += fire[kk][2]
                    sum_s += fire[kk][3]
                    if fire[kk][4] % 2 == 0:
                        check_d += 1
                    fire[kk] = []

                new_mm = sum_mm // 5
                new_s = sum_s // len_table_ij
                table[i][j] = []
                m -= len_table_ij
                if new_mm == 0:
                    continue

                m += 4
                cnt = 0
                if check_d == len_table_ij or check_d == 0:
                    new_d = 0
                else:
                    new_d = 1

                for l in range(m):
                    if not fire[l]:
                        fire[l] = [i, j, new_mm, new_s, new_d]
                        table[i][j].append(l)
                        new_d += 2
                        cnt += 1
                        if cnt == 4:
                            break


n, m, k = map(int, input().split())
move = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
table = [[[] for _ in range(n)]for _ in range(n)]
fire = collections.defaultdict(list)
for i in range(m):
    t = list(map(int, input().split()))
    table[t[0]-1][t[1]-1] = [i]
    fire[i] = [t[0]-1,t[1]-1,t[2],t[3],t[4]]

for _ in range(k):
    moved()
    merged()

result = 0
for values in fire.values():
    if values:
        result += values[2]
print(result)