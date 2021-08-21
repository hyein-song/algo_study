import collections

wheel = []
for _ in range(4):
    wheel.append(list(input()))
k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    turn = [0, 0, 0, 0]
    Q = collections.deque()
    Q.append([a, b])
    attached = [wheel[0][2], wheel[1][6], wheel[1][2], wheel[2][6], wheel[2][2], wheel[3][6]]
    while Q:
        a, b = Q.popleft()
        turn[a-1] = 1

        if a == 1:
            if not turn[1] and attached[0] != attached[1]:
                Q.append([a+1, -b])

        elif a == 2:
            if not turn[0] and attached[0] != attached[1]:
                Q.append([a-1, -b])
            if not turn[2] and attached[2] != attached[3]:
                Q.append([a+1, -b])

        elif a == 3:
            if not turn[1] and attached[2] != attached[3]:
                Q.append([a-1, -b])
            if not turn[3] and attached[4] != attached[5]:
                Q.append([a+1, -b])

        elif a == 4:
            if not turn[2] and attached[4] != attached[5]:
                Q.append([a-1, -b])

        new_wheel = []
        if b == 1:
            for i in range(8):
                new_wheel.append(wheel[a-1][(i - 1) % 8])
        else:
            for i in range(8):
                new_wheel.append(wheel[a-1][(i + 1) % 8])

        wheel[a-1] = new_wheel

ans = 0
for idx, w in enumerate(wheel):
    if w[0] == '1':
        ans += (2**idx)

print(ans)
