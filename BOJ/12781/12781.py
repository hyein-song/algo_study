import sys

def ccw(x1,y1,x2,y2,x3,y3):
    calc = x1*y2 + x2*y3 + x3*y1 - (y1*x2 + y2*x3 + y3*x1)
    if calc == 0:
        return 0
    elif calc > 0:
        return 1
    else:
        return -1


nums = list(map(int, sys.stdin.readline().split()))

c1 = ccw(nums[0],nums[1],nums[2],nums[3],nums[4],nums[5])
c2 = ccw(nums[0],nums[1],nums[2],nums[3],nums[6],nums[7])
c3 = ccw(nums[4],nums[5],nums[6],nums[7],nums[0],nums[1])
c4 = ccw(nums[4],nums[5],nums[6],nums[7],nums[2],nums[3])
if c1*c2 < 0 and c3*c4 < 0:
    print(1)
else :
    print(0)


