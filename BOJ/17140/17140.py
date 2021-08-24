import collections
import sys
input = sys.stdin.readline

r,c,k = map(int, input().split())
table = []
for _ in range(3):
    table.append(list(map(int, input().split())))
num = [3, 3] # row, col
cnt = 0
while cnt <= 100:
    if 0<=r-1<num[0] and 0<=c-1<num[1] and table[r-1][c-1] == k:
        print(cnt)
        sys.exit(0)

    if num[0] >= num[1]:
        max_row = 0
        new_table = []
        for i in range(num[0]):
            new_row = []
            row = table[i]
            tmp = collections.Counter(row).most_common()
            counter = sorted([j for j in tmp if j[0] > 0], key=lambda x: (x[1], x[0]))
            for a, b in counter:
                new_row.extend([a, b])
            max_row = max(max_row, len(new_row))
            new_table.append(new_row)

        for idx, ro in enumerate(new_table):
            calc = max_row - len(ro)
            if calc > 0 :
                new_table[idx] += [0]*calc
        num = [len(new_table), max_row]
    else:
        max_col = 0
        new_col_table = []
        for i in range(num[1]):
            new_col = []
            col = [table[j][i] for j in range(num[0])]
            tmp = collections.Counter(col).most_common()
            counter = sorted([j for j in tmp if j[0] > 0], key=lambda x: (x[1], x[0]))

            for a, b in counter:
                new_col.extend([a, b])

            max_col = max(max_col, len(new_col))
            new_col_table.append(new_col)

        for idx, co in enumerate(new_col_table):
            calc = max_col - len(co)
            if calc > 0 :
                new_col_table[idx] += [0]*calc

        new_table = [[0 for _ in range(len(new_col_table))] for _ in range(max_col)]

        for a in range(max_col):
            for b in range(len(new_col_table)):
                new_table[a][b] = new_col_table[b][a]
        num = [max_col, len(new_col_table)]

    table = [i[:] for i in new_table]
    cnt += 1

print(-1)