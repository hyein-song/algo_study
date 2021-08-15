import sys


def col_swap(x, n):
    global max_val
    for i in range(n):
        for j in range(2):
            ny = x + move[j]
            if 0 <= ny < n:
                board[i][x], board[i][ny] = board[i][ny], board[i][x]
                new_lines = []
                new_lines.append([board[m][x] for m in range(n)])
                new_lines.append([board[m][ny] for m in range(n)])
                new_lines.append(board[i])
                max_val = max(max_val, cnt_one_line_candy(new_lines))
                board[i][x], board[i][ny] = board[i][ny], board[i][x]


def row_swap(x, n):
    global max_val
    for i in range(n):
        for j in range(2):
            nx = x + move[j]
            if 0 <= nx < n:
                board[x][i], board[nx][i] = board[nx][i], board[x][i]
                new_lines = []
                new_lines.append(board[x])
                new_lines.append(board[nx])
                new_lines.append([board[m][i] for m in range(n)])

                max_val = max(max_val, cnt_one_line_candy(new_lines))
                board[x][i], board[nx][i] = board[nx][i], board[x][i]


def cnt_one_line_candy(lines):
    global max_val
    candy = {'C': 1,
             'P': 1,
             'Z': 1,
             'Y': 1}
    for one_line in lines:
        for key in candy.keys():
            candy[key] = 1

        for i in range(n - 1):
            if one_line[i] == one_line[i + 1]:
                candy[one_line[i + 1]] += 1
            else:
                max_val = max(max_val, candy[one_line[i + 1]])
                candy[one_line[i + 1]] = 1

        max_val = max(max_val, max(candy.values()))

    return max_val

n = int(input())
board = []
move = [-1, 1]
for _ in range(n):
    board.append(list(input()))

max_val = 0
max_val = max(max_val, cnt_one_line_candy(board))
for i in range(n):
    col_swap(i, n)
    row_swap(i, n)

print(max_val)
