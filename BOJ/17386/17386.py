import sys


def ccw(x1,y1,x2,y2,x3,y3):
    calc = x1*y2 + x2*y3 + x3*y1 - (y1*x2 + y2*x3 + y3*x1)
    if calc == 0:
        return 0
    elif calc > 0:
        return 1
    else:
        return -1


a1, b1, a2, b2 = map(int, sys.stdin.readline().split())
a3, b3, a4, b4 = map(int, sys.stdin.readline().split())

calc1 = ccw(a1,b1,a2, b2,a3, b3) * ccw(a1,b1,a2, b2, a4, b4)
calc2 = ccw(a3, b3, a4, b4,a1,b1) * ccw(a3, b3, a4, b4, a2, b2)
if calc1 < 0 and calc2 < 0:
    print(1)
else:
    print(0)
