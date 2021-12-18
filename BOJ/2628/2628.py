


c,r = map(int, input().split())
n = int(input())
rows = [0,r]
cols = [0,c]

for _ in range(n):
    a, b = map(int,input().split())
    if a == 0: # 가로로 자르기
        rows.append(b)
    else:
        cols.append(b)

rows.sort()
cols.sort()

max_row = 0
max_col = 0
for i in range(len(rows)-1):
    max_row = max(max_row, rows[i+1] - rows[i])

for i in range(len(cols)-1):
    max_col = max(max_col, cols[i+1] - cols[i])

print(max_row*max_col)




