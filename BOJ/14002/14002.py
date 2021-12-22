import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

max_dp = max(dp)
print(max_dp)
result = []
for i in range(n-1,-1,-1):
    if dp[i] == max_dp:
        max_dp-= 1
        result.append(nums[i])

result.reverse()
print(*result)

