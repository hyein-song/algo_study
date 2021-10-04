


n, k = map(int, input().split())
arr = list(map(int, input().split()))
robot = [0 for _ in range(n)]
cnt = 0
result = 0
while cnt < k :
    result += 1
    # 1
    arr = [arr[-1]] + arr[0:-1]
    robot = [0] + robot[0:-2] + [0]

    # 2
    for i in range(n-2,-1,-1):
        if robot[i] == 1:
            if arr[i+1] > 0 and robot[i+1] == 0:
                robot[i] = 0
                robot[i + 1] = 1
                arr[i + 1] -= 1
                if arr[i + 1] == 0:
                    cnt += 1
    robot[-1] = 0
    # 3
    if arr[0] != 0:
        arr[0] -=1
        if arr[0] == 0:
            cnt += 1
        robot[0] = 1

print(result)