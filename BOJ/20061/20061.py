import sys
input = sys.stdin.readline


def move_blocks(tt, xx, yy):
    # print('origin')
    # print(blue)
    # print(green)
    # blue
    if tt == 1:
        # blue
        for i in range(2,6):
            if blue[xx][i] == 1:
                blue[xx][i-1] = 1
                break
            elif i == 5:
                blue[xx][5] = 1
        # green
        for i in range(2,6):
            if green[i][yy] == 1:
                green[i-1][yy] = 1
                break
            elif i == 5:
                green[5][yy] = 1

    elif tt == 2:
        #blue
        for i in range(2,6):
            if blue[xx][i] == 1:
                blue[xx][i-1] = 1
                blue[xx][i-2] = 1
                break
            elif i == 5:
                blue[xx][5] = 1
                blue[xx][4] = 1
        # green
        for i in range(2,6):
            if green[i][yy] == 1 or green[i][yy+1] == 1:
                green[i-1][yy] = 1
                green[i-1][yy+1] = 1
                break
            elif i == 5:
                green[5][yy] = 1
                green[5][yy + 1] = 1

    elif tt == 3:
        # blue
        for i in range(2,6):
            if blue[xx][i] == 1 or blue[xx+1][i] == 1:
                blue[xx][i-1] = 1
                blue[xx+1][i-1] = 1
                break
            elif i == 5:
                blue[xx][5] = 1
                blue[xx + 1][5] = 1
        # green
        for i in range(2,6):
            if green[i][yy] == 1:
                green[i-1][yy] = 1
                green[i-2][yy] = 1
                break
            elif i==5:
                green[5][yy] = 1
                green[4][yy] = 1
    # print('after')
    # print(blue)
    # print(green)
    return

def delete_one_line():
    global score
    # print('delete one')
    # print(blue)
    # print(green)
    # blue
    cnt_line = 0
    for i in range(5, -1, -1): # 6~0
        c = 0
        for j in range(4):
            if blue[j][i] == 1:
                c += 1
        if c == 4: # 한 열 지워짐
            cnt_line += 1
            score += 1
        else:
            if i == 5 or cnt_line == 0:
                continue
            # 끝 줄이 아니고 i 오른쪽에 지워진 줄이 하나 이상
            for j in range(4):
                blue[j][i + cnt_line] = blue[j][i]

    # green
    cnt_line = 0
    for i in range(5, -1, -1): # 6~0
        c = 0
        for j in range(4):
            if green[i][j] == 1:
                c += 1
        if c == 4: # 한 열 지워짐
            cnt_line += 1
            score += 1
        else:
            if i == 5 or cnt_line == 0:
                continue
            # 끝 줄이 아니고 i 아래쪽에 지워진 줄이 하나 이상
            for j in range(4):
                green[i + cnt_line][j] = green[i][j]
    return

def delete_over_lines():
    # print('delete over')
    # print(blue)
    # print(green)
    # blue
    start_col = 3
    for i in range(1,-1,-1):
        for j in range(4):
            if blue[j][i] == 1:
                start_col = i
                break

    if start_col == 0 or start_col == 1:
        for i in range(5,1,-1):
            for j in range(4):
                blue[j][i] = blue[j][i+start_col-2]
        for i in range(2-start_col):
            print('delete over i',i)
            for j in range(4):
                blue[j][1-i] = 0


    #green
    start_row = 3
    for i in range(1,-1,-1):
        for j in range(4):
            if green[i][j] == 1:
                start_row = i
                break
    if start_row == 0 or start_row == 1:
        for i in range(5,1,-1):
            for j in range(4):
                green[i][j] = green[i+start_row-2][j]

        for i in range(2-start_row):
            for j in range(4):
                green[1-i][j] = 0
    return


n = int(input())
green = [[0 for _ in range(4)] for _ in range(6)]
blue = [[0 for _ in range(6)] for _ in range(4)]
score = 0
for i in range(n):
    t, x, y = map(int, input().split())
    move_blocks(t, x, y)
    delete_one_line()
    delete_over_lines()
    # print(i)
    # print('b',blue)
    # print('g',green)

print(score)
cnt = 0
for i in range(4):
    for j in range(2,6):
        cnt += blue[i][j]
        cnt += green[j][i]
print(cnt)