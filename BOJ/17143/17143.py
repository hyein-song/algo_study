import sys
input = sys.stdin.readline

def select():
    for s in sharks:
        if s[1] == now:
            return s
    return False


def move():
    global M
    shark_dict = dict()
    while sharks:
        r,c,s,d,z = sharks.pop()
        origin_s = s
        while s > 0 :
            if d == 1:
                if s <= r:
                    r = r-s
                    s = 0
                else:
                    d = 2
                    s -= r
                    r = 0

            elif d == 2:
                if s <= R-1-r:
                    r = r + s
                    s = 0
                else:
                    d = 1
                    s -= R - 1 - r
                    r = R-1

            elif d == 3:
                if s <= C-1-c:
                    c = c+s
                    s = 0
                else:
                    d = 4
                    s -= C - 1 - c
                    c = C-1


            else:
                if s <= c:
                    c = c-s
                    s = 0
                else:
                    d = 3
                    s -= c
                    c = 0

        if (r, c) in shark_dict.keys():
            if shark_dict[(r, c)][4] < z:
                shark_dict[(r, c)] = [r, c, origin_s, d, z]
        else:
            shark_dict[(r, c)] = [r, c, origin_s, d, z]
    # print(shark_dict)
    for s_d in shark_dict.values():
        sharks.append(s_d)


R,C,M = map(int, input().split())
now = -1
sharks = []
for _ in range(M):
    t1,t2,t3,t4,t5 = map(int, input().split())
    sharks.append([t1-1,t2-1,t3,t4,t5])

get = 0
for jj in range(C):
    now += 1
    sharks = sorted(sharks, key=lambda x: (x[0], x[1]))
    selected_shark = select()
    if selected_shark:
        get += selected_shark[4]
        sharks.remove(selected_shark)
        M -= 1

    move()


print(get)


