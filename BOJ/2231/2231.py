import sys

n = int(input())

for i in range(1, n):
    result = i
    s = i
    while i > 0:
        i, b = divmod(i, 10)
        s += b

    if s == n:
        print(result)
        sys.exit(0)

print(0)
