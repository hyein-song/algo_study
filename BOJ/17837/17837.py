import collections


def game():
    for cnt in range(1, 1001):
        for i in range(1, k+1):
            index = 0
            x, y, d = pieces[i]
            nx = x + move[d-1][0]
            ny = y + move[d-1][1]
            if 0 <= nx < n and 0 <= ny < n and color[nx][ny] != 2:
                if color[nx][ny] == 0:
                    len_now = len(board[(x, y)])
                    for j in range(len_now):
                        if board[(x, y)][j] == i:
                            index = j
                            break
                    for j in board[(x, y)][index:]:
                        board[(nx, ny)].append(j)
                        tmp = pieces[j]
                        pieces[j] = [nx, ny, tmp[2]]

                    board[(x, y)] = board[(x, y)][:index]

                elif color[nx][ny] == 1:
                    len_now = len(board[(x, y)])
                    for j in range(len_now):
                        if board[(x, y)][j] == i:
                            index = j
                            break
                    for _ in range(len_now-index):
                        j = board[(x, y)].pop()
                        board[(nx, ny)].append(j)
                        tmp = pieces[j]
                        pieces[j] = [nx, ny, tmp[2]]

            else:
                if d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 4
                elif d == 4:
                    d = 3

                nx = x + move[d - 1][0]
                ny = y + move[d - 1][1]
                if 0 <= nx < n and 0 <= ny < n and color[nx][ny] != 2:
                    if color[nx][ny] == 0:
                        len_now = len(board[(x, y)])
                        for j in range(len_now):
                            if board[(x, y)][j] == i:
                                index = j
                                break
                        for j in board[(x, y)][index:]:
                            board[(nx, ny)].append(j)
                            tmp = pieces[j]
                            pieces[j] = [nx, ny, tmp[2]]

                        board[(x, y)] = board[(x, y)][:index]

                    elif color[nx][ny] == 1:
                        len_now = len(board[(x, y)])
                        for j in range(len_now):
                            if board[(x, y)][j] == i:
                                index = j
                                break
                        for _ in range(len_now - index):
                            j = board[(x, y)].pop()
                            board[(nx, ny)].append(j)
                            tmp = pieces[j]
                            pieces[j] = [nx, ny, tmp[2]]

                else:
                    nx = x
                    ny = y

            pieces[i] = [nx, ny, d]
            if len(board[(nx, ny)]) >= 4:
                return cnt

    return -1


n, k = map(int, input().split())
move = [[0,1],[0,-1],[-1,0],[1,0]]
color = []
pieces = dict() # 말 숫자 : 좌표, 방향
board = collections.defaultdict(list) # 좌표 : 말 숫자
for _ in range(n):
    color.append(list(map(int, input().split())))

for i in range(1, k+1):
    a,b,c = list(map(int, input().split()))
    pieces[i] = [a-1,b-1,c]
    board[(a-1,b-1)].append(i)

result = game()
print(result)


