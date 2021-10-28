import collections
import itertools
import sys


def bfs(w, h, start, target):
    q = collections.deque()
    q.append(start)
    move_cnt = 1
    visited = [[0 for _ in range(w)] for _ in range(h)]
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + move[i][0]
                ny = y + move[i][1]
                if 0 <= nx < h and 0 <= ny < w and table[nx][ny] != 'x' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if [nx,ny] == target:
                        return move_cnt
                    else:
                        q.append([nx,ny])
        move_cnt += 1
    return -1


move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
dirty = dict()
while True:
    w, h = map(int, input().split())
    cnt = 0
    if w == 0 and h == 0:
        break
    table = []
    for i in range(h):
        tmp = list(input())
        for j in range(w):
            if tmp[j] == 'o':
                robot = [i, j]
            elif tmp[j] == '*':
                dirty[cnt] = [i, j]
                cnt += 1
        table.append(tmp)
    # 각 더러운점 사이의 거리를 bfs로 dp에 저장
    dp = [[0 if i == j else sys.maxsize for i in range(cnt)] for j in range(cnt)]
    dist_cleaner = [0 for i in range(cnt)]
    for i in range(cnt):
        dist_cleaner[i] = bfs(w, h, robot, dirty[i])
        for j in range(i+1,cnt):
            if i == j or dp[i][j] != sys.maxsize:
                continue
            d = bfs(w, h, dirty[i], dirty[j])
            dp[i][j] = d
            dp[j][i] = d

    if -1 in dist_cleaner:
        print(-1)
        continue

    # print(dp)
    nums_permu = list(itertools.permutations([i for i in range(cnt)], cnt))
    # print(nums_permu)
    result = sys.maxsize
    for nums in nums_permu:
        f = 1
        nums = list(nums)
        tmp = dist_cleaner[nums[0]]
        for i in range(cnt-1):
            if dp[nums[i]][nums[i+1]] != -1:
                tmp += dp[nums[i]][nums[i+1]]
            else:
                f = 0
                break
        if f:
            result = min(result, tmp)
    print(result)




