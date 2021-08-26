import collections

def check(table):
    result = 0
    for i in range(n):
        fill = [0] * n
        end = 0
        for j in range(n - 1):
            v = []
            if abs(table[i][j] - table[i][j + 1]) > 1:
                end = 1
                break

            if table[i][j] - table[i][j + 1] == 0:
                continue

            elif table[i][j] - table[i][j + 1] == -1:
                for k in range(j, j-l, -1):
                    if k >= 0 and table[i][k] == table[i][j] and fill[k] == 0:
                        v.append(k)
                    else:
                        end = 1
                        break
                if end:
                    break

            elif table[i][j] - table[i][j + 1] == 1:
                for k in range(j+1, j+l+1):
                    if k < n and table[i][k] == table[i][k] and fill[k] == 0:
                        v.append(k)
                    else:
                        end = 1
                        break
                if end:
                    break

            for vv in v:
                fill[vv] = 1
            v.clear()

        if not end:
            result += 1

    return result


n, l = map(int, input().split())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

cols = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(table[j][i])
    cols.append(tmp)

result = 0
result += check(table)
result += check(cols)

print(result)