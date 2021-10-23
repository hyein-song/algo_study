import sys


n = int(sys.stdin.readline().rstrip())
dp = [[0 for _ in range(n)] for _ in range(n)]
a = list(sys.stdin.readline().split())

for dif in range(n):
    for st in range(n-dif):
        end = dif+st
        if st == end:
            dp[st][end] = 1
            continue
        elif st+1 == end:
            if a[st] == a[end]:
                dp[st][end] = 1
            else:
                dp[st][end] = 0
            continue
        elif a[st] == a[end] and dp[st+1][end-1]==1:
            dp[st][end] = 1
        else:
            dp[st][end] = 0

m = int(sys.stdin.readline().rstrip())

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    print(dp[x-1][y-1])
