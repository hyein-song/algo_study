
# 0: 동, 1: 서, 2: 남, 3: 북
def dfs(depth, total_cnt):
    global result

    if depth == len(cctv):
        result = total_cnt if result > total_cnt else result
        return

    cctv_num, a, b = cctv[depth]
    if cctv_num == 5:
        watchable = []
        for i in range(4):
            watchable.append([i,a,b])
        changed, ch_cnt = change(watchable)
        dfs(depth+1, total_cnt-ch_cnt)

    elif cctv_num == 4 or cctv_num == 3 or cctv_num == 2:
        for combi in combis[cctv_num-2]:
            watchable = []
            for i in combi:
                watchable.append([i,a,b])
            changed, ch_cnt = change(watchable)
            dfs(depth + 1, total_cnt - ch_cnt)
            rollback(changed)

    elif cctv_num == 1:
        for i in range(4):
            changed, ch_cnt = change([[i,a,b]])
            dfs(depth + 1, total_cnt - ch_cnt)
            rollback(changed)


def change(w):
    changed = []
    cnt = 0
    while w:
        d, i, j = w.pop()
        ni = i + move[0][d]
        nj = j + move[1][d]
        if 0 <= ni < n and 0 <= nj < m and table[ni][nj] != 6:
            if table[ni][nj] == 0:
                table[ni][nj] = '#'
                changed.append([ni,nj])
                cnt += 1
            w.append([d, ni, nj])
    return changed, cnt

def rollback(c):
    for i, j in c:
        table[i][j] = 0

n, m = map(int, input().split())
table = []
cctv = []
wall = []
move = [[0, 0, 1, -1], [1, -1, 0, 0]]
result = total_cnt = n*m

combis = [[[0,1],[2,3]], [[0,3],[0,2],[1,2],[1,3]], [[0,1,2], [0,1,3], [1,2,3], [0,2,3]]]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 6:
            wall.append([i, j])
            total_cnt -= 1
        elif tmp[j] != 0:
            cctv.append([tmp[j], i, j])
            total_cnt -= 1
    table.append(tmp)

cctv.sort(reverse = True)
dfs(0, total_cnt)

print(result)