import collections
import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()
print(round(sum(nums)/n))
print(nums[n//2])

count = collections.Counter(nums).most_common()
if len(count) > 1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])

print(nums[-1]-nums[0])