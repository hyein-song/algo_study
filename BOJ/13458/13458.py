import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
result = n
for i in range(n):
    a[i] -= b
    if a[i] <= 0:
        continue

    x, y = divmod(a[i], c)
    result += x
    if y != 0:
        result += 1

print(result)