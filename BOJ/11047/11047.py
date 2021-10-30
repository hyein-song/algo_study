import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().strip()))

result = 0
for i in range(n-1,-1,-1):
    if k >= coins[i]:
        a, b = divmod(k,coins[i])
        result += a
        k = b
        if k == 0:
            break
print(result)







