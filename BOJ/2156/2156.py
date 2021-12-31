import sys

n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

if n==1:
    print(nums[0])
    sys.exit(0)

dp = [0] * n
dp[0] = nums[0]
dp[1] = dp[0] + nums[1]
for i in range(2,n):
    dp[i] = max(dp[i-1], dp[i-3]+nums[i-1]+nums[i], dp[i-2]+nums[i])

print(dp[-1])

