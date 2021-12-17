import sys


def ccw(x1,y1,x2,y2,x3,y3):
    calc = x1*y2 + x2*y3 + x3*y1 - (y1*x2 + y2*x3 + y3*x1)
    if calc == 0:
        return 0
    elif calc > 0:
        return 1
    else:
        return -1

def solution():
    a1, b1, a2, b2 = map(int, sys.stdin.readline().split())
    a3, b3, a4, b4 = map(int, sys.stdin.readline().split())

    calc1 = ccw(a1, b1, a2, b2, a3, b3) * ccw(a1, b1, a2, b2, a4, b4)
    calc2 = ccw(a3, b3, a4, b4, a1, b1) * ccw(a3, b3, a4, b4, a2, b2)

    mx1, my1, mx2, my2 = min(a1,a2), min(b1,b2), max(a1,a2), max(b1,b2)
    mx3, my3, mx4, my4 = min(a3, a4), min(b3, b4), max(a3, a4), max(b3, b4)
    # 평행
    if calc1 == 0 and calc2 == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return 1
    else:
        if calc1 <= 0 and calc2 <= 0:
            return 1
    return 0

print(solution())


