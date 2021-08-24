import collections
import sys
input = sys.stdin.readline


def bfs(shark_size):
    global shark
    q = collections.deque()
    q.append(shark)
    sea[shark[0]][shark[1]] = 0
    dist = 1
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[shark[0]][shark[1]] = 1

    while q:
        can_eat_fish = []
        for _ in range(len(q)):
            a, b = q.popleft()
            for i in range(4):
                na = a + move[0][i]
                nb = b + move[1][i]

                if na < 0 or na >= n or nb < 0 or nb >= n or sea[na][nb] > shark_size or visited[na][nb] == 1:
                    continue
                if 0 < sea[na][nb] < shark_size:
                    can_eat_fish.append([na, nb])
                else:
                    q.append([na, nb])
                visited[na][nb] = 1

        if can_eat_fish:
            f = sorted(can_eat_fish)[0]
            shark = [f[0], f[1]]
            return dist
        dist += 1
    return 0


n = int(input())
sea = []
shark_size = 2
feed_cnt = 0
move = [[0,0,1,-1], [1,-1,0,0]]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 9:
            shark = [i, j]
    sea.append(tmp)

time = 0
feed_cnt = 0
while True:
    d = bfs(shark_size)
    if not d:
        break
    else:
        time += d
        feed_cnt += 1
        if feed_cnt == shark_size:
            shark_size += 1
            feed_cnt = 0

print(time)