


def ccw(x1,y1,x2,y2,x3,y3):
    calc = x1*y2 + x2*y3 + x3*y1 - (y1*x2 + y2*x3 + y3*x1)
    return calc / 2

def solution():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(list(map(int, input().split())))

    result = 0
    for i in range(1,n-1):
        result += ccw(nums[0][0],nums[0][1],nums[i][0],nums[i][1],nums[i+1][0],nums[i+1][1])

    print(abs(round(result,1)))

solution()