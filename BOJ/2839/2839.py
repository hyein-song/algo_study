import sys

n = int(sys.stdin.readline().strip())
a, b = divmod(n,5)
if b == 0:
    print(a)
    sys.exit(0)
else:
    for i in range(a,-1,-1):
        c,d = divmod(b, 3)
        if d == 0:
            print(i+c)
            sys.exit(0)
        else:
            b += 5
    print(-1)


