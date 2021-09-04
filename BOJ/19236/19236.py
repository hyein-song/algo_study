import copy


def dfs(x, y, d, total):
    global table
    global fish
    global result
    for i in range(1, 4):
        nx = x + move[d][0] * i
        ny = y + move[d][1] * i
        if 0 <= nx < 4 and 0 <= ny < 4:
            if table[nx][ny][0] != 0:
                origin_table = copy.deepcopy(table)
                tmp = table[nx][ny][0]
                nd = table[nx][ny][1]
                table[nx][ny][0] = 0
                origin_fish = copy.deepcopy(fish)
                fish[tmp] = []
                fish_move(nx, ny)
                dfs(nx, ny, nd, total + tmp)
                table = copy.deepcopy(origin_table)
                fish = copy.deepcopy(origin_fish)
            else:
                continue
        else:
            if total > result:
                result = total
            return

    return


def fish_move(shark_x,shark_y):
    global table
    for i in range(1, 17):
        if fish[i]:
            x, y, d = fish[i]
            for j in range(8):
                nd = (d+j) % 8
                nx = x + move[nd][0]
                ny = y + move[nd][1]
                if 0 <= nx < 4 and 0 <= ny < 4 and [nx, ny] != [shark_x, shark_y]:
                    if table[nx][ny][0] == 0:
                        table[x][y][1] = nd
                        table[x][y], table[nx][ny] = table[nx][ny], table[x][y]
                        fish[i] = [nx, ny, nd]
                    else:
                        swap_fish = table[nx][ny][0]
                        table[x][y][1] = nd
                        fish[i][2] = nd
                        table[x][y], table[nx][ny] = table[nx][ny], table[x][y]
                        fish[i][0], fish[swap_fish][0] = fish[swap_fish][0], fish[i][0]
                        fish[i][1], fish[swap_fish][1] = fish[swap_fish][1], fish[i][1]
                    break

        else:
            continue


move = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
table = [[0 for _ in range(4)] for _ in range(4)]
result = 0
fish = dict()
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(0,8,2):
        table[i][j//2] = [tmp[j], tmp[j+1]-1]
        fish[tmp[j]] = [i, j//2, tmp[j+1]-1] # i, j, d


result += table[0][0][0]
fish[table[0][0][0]] = []
table[0][0][0] = 0
fish_move(0, 0)
dfs(0, 0, table[0][0][1], result)

print(result)