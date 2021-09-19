
import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    a,b = map(int, input().split())
    nums.append([a,b])

nums.sort()
for nn in nums:
    print(*nn)