n = int(input())
nums = [0 for i in range(10)]
p = 1
while n != 0:
    while n % 10 != 9:
        for i in str(n):
            nums[int(i)] += p
        n -= 1
    if n < 10:
        for i in range(n + 1):
            nums[i] += p
        nums[0] -= p
        break
    else:
        for i in range(10):
            nums[i] += (n // 10 + 1) * p
    nums[0] -= p
    p *= 10
    n //= 10
for i in nums:
    print(i, end=' ')