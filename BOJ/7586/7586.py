import sys
input = sys.stdin.readline

n = int(input())
p = []
for _ in range(n):
    p.append(list(map(int,input().split())))
cnt = [1] * n

for i in range(n):
    for j in range(i, n):
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            cnt[i] += 1
        elif p[i][0] > p[j][0] and p[i][1] > p[j][1]:
            cnt[j] += 1
print(*cnt)