

def dfs(depth):
    global table
    global result
    if depth == 5:
        for i in range(n):
            for j in range(n):
                if table[i][j] > result:
                    result = table[i][j]
        return

    origin_t = [i[:] for i in table]

    for i in range(4):
        move_tile(i)
        dfs(depth+1)
        table = [i[:] for i in origin_t]

    return


def move_tile(d):
    global table
    if d == 0:
        for i in range(n):
            j = 0
            k = -1
            f = 1 # new_row[k]가 0이면  f == 1 아니면 f == 0
            while j < n and k < n:
                if table[i][j] != 0:
                    if f:
                        k += 1
                        table[i][k] = table[i][j]
                        f = 0
                    else:
                        if table[i][j] == table[i][k]:
                            table[i][k] += table[i][j]
                            f = 1
                        else:
                            k += 1
                            table[i][k] = table[i][j]
                j += 1
            for j in range(k+1, n):
                table[i][j] = 0
    elif d == 1:
        for i in range(n):
            j = n-1
            k = n
            f = 1
            while j >= 0 and k >= 0:
                if table[i][j] != 0:
                    if f:
                        k -= 1
                        table[i][k] = table[i][j]
                        f = 0
                    else:
                        if table[i][j] == table[i][k]:
                            table[i][k] += table[i][j]
                            f = 1
                        else:
                            k -= 1
                            table[i][k] = table[i][j]
                j -= 1
            for j in range(0, k):
                table[i][j] = 0

    elif d == 2:
        for i in range(n):
            j = 0
            k = -1
            f = 1
            while j < n and k < n:
                if table[j][i] != 0:
                    if f:
                        k += 1
                        table[k][i] = table[j][i]
                        f = 0
                    else:
                        if table[j][i] == table[k][i]:
                            table[k][i] += table[j][i]
                            f = 1
                        else:
                            k += 1
                            table[k][i] = table[j][i]
                j += 1
            for j in range(k+1, n):
                table[j][i] = 0
    elif d == 3:
        for i in range(n):
            j = n-1
            k = n
            f = 1
            while j >= 0 and k >= 0:
                if table[j][i] != 0:
                    if f:
                        k -= 1
                        table[k][i] = table[j][i]
                        f = 0
                    else:
                        if table[j][i] == table[k][i]:
                            table[k][i] += table[j][i]
                            f = 1
                        else:
                            k -= 1
                            table[k][i] = table[j][i]
                j -= 1
            for j in range(0, k):
                table[j][i] = 0


n = int(input())
table = []
move = [[0, 1], [0, -1], [-1, 0], [1, 0]]
result = 0
for _ in range(n):
    table.append(list(map(int, input().split())))

dfs(0)
print(result)