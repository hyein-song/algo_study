import sys


p = 1000000003
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
# if n//2 < k:
#     print(0)
#     sys.exit(0)

for i in range(n+1):
    dp[i][0] = 1
    dp[i][1] = i

for i in range(2,n+1):
    for j in range(1,k+1):
        dp[i][j] = (dp[i-2][j-1] + dp[i-1][j]) % p

print((dp[n-3][k-1] + dp[n-1][k]) % p)
