import sys
input = sys.stdin.readline

n = int(input())
table = [[0 for _ in range(n)] for _ in range(n)]
move = [[1,0],[-1,0],[0,1],[0,-1]]
like = dict()
for _ in range(n**2):
    tmp = list(map(int, input().split()))
    student = tmp[0]
    friends = tmp[1:]
    like[student] = friends
    can = []
    for i in range(n):
        for j in range(n):
            if table[i][j] != 0:
                continue
            cnt_like = 0
            cnt_zero = 0
            for k in range(4):
                ni = i + move[k][0]
                nj = j + move[k][1]
                if 0 <= ni < n and 0 <= nj < n:
                    if table[ni][nj] == 0:
                        cnt_zero +=1
                    elif table[ni][nj] in friends:
                        cnt_like += 1
            can.append([cnt_like, cnt_zero,-i,-j])
    can = sorted(can, reverse=True)
    table[-can[0][2]][-can[0][3]] = student

result = 0
for i in range(n):
    for j in range(n):
        student = table[i][j]
        cnt = 0
        for k in range(4):
            ni = i + move[k][0]
            nj = j + move[k][1]
            if 0 <= ni < n and 0 <= nj < n:
                if table[ni][nj] in like[student]:
                    cnt += 1
        if cnt != 0:
            result += 10**(cnt-1)

print(result)