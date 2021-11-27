




x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

calc = (x1*y2 + x2* y3 + x3*y1 - (y1*x2 + y2 * x3 + y3*x1))
if calc > 0:
    print(1)
elif calc < 0:
    print(-1)
else:
    print(0)
