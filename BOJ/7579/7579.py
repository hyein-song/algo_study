import sys

n, m = map(int, sys.stdin.readline().split())
memories = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))
sum_costs = sum(costs)
dp = [[0 for _ in range(sum_costs+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(sum_costs+1):
        if j >= costs[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-costs[i-1]]+memories[i-1])
        else:
            dp[i][j] = dp[i - 1][j]
# for d in dp:
#     print(d)
for i in range(sum_costs+1):
    if dp[n][i] >= m:
        print(i)
        break


