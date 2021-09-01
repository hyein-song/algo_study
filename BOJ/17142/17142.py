import collections
import itertools
import sys


def bfs(start, to):
    t = [i[:] for i in table]
    move = [[0,1],[0,-1],[1,0],[-1,0]]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = collections.deque()
    for i in start:
        q.append(i)
        visited[i[0]][i[1]] = 1
    cnt = 1
    while q:
        for _ in range(len(q)):
            a, b = q.popleft()
            for i in range(4):
                na = a + move[i][0]
                nb = b + move[i][1]
                if 0 <= na < n and 0 <= nb < n and visited[na][nb] == 0 and t[na][nb] != 1:
                    visited[na][nb] = 1
                    if t[na][nb] == 0:
                        to -= 1
                    if to == 0:
                        return cnt
                    q.append([na, nb])
                    t[na][nb] = 2
        cnt += 1
    return -1


n, m = map(int, input().split())
table = []
virus = []
total = n*n
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] == 2:
            virus.append([i,j])
            total -= 1
        elif tmp[j] == 1:
            total -= 1
    table.append(tmp)

if total == 0:
    print(0)
    sys.exit(0)

selected = (itertools.combinations(virus, m))
result = []
for se in selected:
    r = bfs(se, total)
    if r != -1:
        result.append(r)

if result:
    print(min(result))
else:
    print(-1)


