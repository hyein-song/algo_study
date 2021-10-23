import sys

max_val = sys.maxsize
n = int(sys.stdin.readline())
costs =[[]]
result = max_val
for i in range(n):
    costs.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(3)] for _ in range(n+1)]

for i in range(3):
    for j in range(3):
        if i == j:
            dp[1][j] = costs[1][j]
        else:
            dp[1][j] = max_val
    for j in range(2,n+1):
        dp[j][0] = costs[j][0] + min(dp[j-1][1],dp[j-1][2])
        dp[j][1] = costs[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = costs[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    for j in range(3):
        if i != j:
            result = min(result, dp[n][j])

print(result)



