import collections
import copy
import sys
input = sys.stdin.readline


def rotate(s):
    if s == 1:
        return table
    new_table = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(0,m,s):
        for j in range(0,m,s):
            new_split_table = [[0 for _ in range(s)] for _ in range(s)]
            for r in range(s):
                for c in range(s):
                    new_split_table[c][(s-r-1)%s] = table[i+r][j+c]

            for r in range(s):
                for c in range(s):
                    new_table[i+r][j+c] = new_split_table[r][c]
    return new_table


def melt():
    new_table = copy.deepcopy(table)
    for i in range(m):
        for j in range(m):
            if table[i][j] != 0:
                cnt = 0
                for dd in range(4):
                    ni = i + move[dd][0]
                    nj = j + move[dd][1]
                    if 0 <= ni < m and 0 <= nj < m and table[ni][nj] != 0:
                        cnt += 1
                if cnt < 3:
                    new_table[i][j] = table[i][j] - 1
    return new_table


def bfs():
    sum_ice = 0
    visited = [[0 for _ in range(m)] for _ in range(m)]
    max_cnt = 0
    for i in range(m):
        for j in range(m):
            sum_ice += table[i][j]
            if not visited[i][j]:
                q = collections.deque()
                q.append([i, j])
                cnt = 0
                while q:
                    x, y = q.popleft()
                    for dd in range(4):
                        ni = x + move[dd][0]
                        nj = y + move[dd][1]
                        if 0 <= ni < m and 0 <= nj < m and table[ni][nj] != 0 and visited[ni][nj]==0:
                            visited[ni][nj] = 1
                            q.append([ni, nj])
                            cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
    print(sum_ice)
    print(max_cnt)
    return sum_ice, max_cnt


n, q = map(int, input().split())
table = []
m = 2**n
move = [[0,1],[0,-1],[1,0],[-1,0]]
for _ in range(m):
    table.append(list(map(int, input().split())))

L = list(map(int, input().split()))
for i in range(q):
    table = rotate(2**L[i])# 부분 격자 크기
    table = melt()

bfs()
