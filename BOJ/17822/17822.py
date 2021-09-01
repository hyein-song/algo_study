
def move(x,d,k):
    for i in range(x-1,n,x):
        if d: # 빈시계방향
            for _ in range(k):
                tmp = circle[i][0]
                for j in range(1,m):
                    circle[i][j-1] = circle[i][j]
                circle[i][-1] = tmp
        else: # 시계방향
            for _ in range(k):
                tmp = circle[i][-1]
                for j in range(m-1,0,-1):
                    circle[i][j] = circle[i][j-1]
                circle[i][0] = tmp


def delete():
    same = set()
    cnt = 0
    for i in range(n):
        if sum(circle[i]) == 0:
            continue
        for j in range(m):
            if circle[i][j] == 0:
                continue
            if circle[i][j] == circle[i][j-1]:
                same.add((i,j))
                same.add((i,j-1))
                cnt += 1
            if circle[i][j] == circle[i][(j+1)%m]:
                same.add((i, j))
                same.add((i, (j+1)%m))
                cnt += 1
            if i != n-1 and circle[i][j] == circle[i+1][j]:
                same.add((i, j))
                same.add((i+1, j))
                cnt += 1
            if i != 0 and circle[i][j] == circle[i-1][j]:
                same.add((i, j))
                same.add((i-1, j))
                cnt += 1
    if cnt:
        for i,j in list(same):
            circle[i][j] = 0
    else:
        c = 0
        s = 0
        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    s += circle[i][j]
                    c += 1
        try:
            avg = s/c
        except ZeroDivisionError:
            return

        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    if circle[i][j] > avg:
                        circle[i][j] -= 1
                    elif circle[i][j] < avg:
                        circle[i][j] += 1


n, m, t = map(int, input().split())
circle = []
for _ in range(n):
    circle.append(list(map(int, input().split())))
for _ in range(t):
    x, d, k = map(int, input().split())
    move(x, d, k)
    delete()

result = 0
for i in circle:
    result += sum(i)

print(result)