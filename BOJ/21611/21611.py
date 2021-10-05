import sys
input = sys.stdin.readline


def beads_orders():
    k = 2
    d = 0
    cnt = 0
    now = shark[:]
    for i in range(1, n):
        if i == n - 1:
            k = 3
        for _ in range(k):
            for _ in range(i):
                nx = now[0] + direction[d][0]
                ny = now[1] + direction[d][1]
                now = [nx, ny]
                beads_order.append(now)
                order_dict[cnt] = now
                position_dict[(nx,ny)] = cnt
                cnt += 1
            d = (d + 1) % 4


def move(zero):
    global count
    global beads_flatten
    i = count-1
    z_idx = len(zero)-1
    while i >= 0:
        if beads_flatten[i] == 0:
            beads_flatten = beads_flatten[:i-zero[z_idx]+1] + beads_flatten[i+1:] + [0]*zero[z_idx]
            i -= zero[z_idx]+1
            z_idx -= 1
            if z_idx < 0:
                break
        i -= 1
    count -= sum(zero)
    # print('move')
    # print(count)
    # print(beads_flatten)
    # print(len(beads_flatten))


def explosion():
    global count
    global result
    global beads_flatten
    f = 0
    tmp_list = set()
    zero_cnt = []
    for i in range(count-1):
        if beads_flatten[i] == beads_flatten[i+1]:
            tmp_list.add(i)
            tmp_list.add(i+1)
        else:
            if len(tmp_list) >= 4:
                f = 1
                color = beads_flatten[i]
                for t in list(tmp_list):
                    beads_flatten[t] = 0
                result += len(tmp_list) * color
                zero_cnt.append(len(tmp_list))
            tmp_list.clear()
    if tmp_list:
        if len(tmp_list) >= 4:
            f = 1
            color = beads_flatten[i]
            for t in list(tmp_list):
                beads_flatten[t] = 0
            result += len(tmp_list) * color
            zero_cnt.append(len(tmp_list))
        tmp_list.clear()

    # beads_flatten.extend([0]*(n**2-count))
    # print('explosion')
    # print(count)
    # print(beads_flatten)
    # print(len(beads_flatten))
    return f, zero_cnt


def change():
    global count
    global beads_flatten
    tmp_list = set()
    new_flatten = []
    for i in range(count):
        if beads_flatten[i] == beads_flatten[i + 1]:
            tmp_list.add(i)
            tmp_list.add(i + 1)
        else:
            if len(tmp_list) >= 2:
                new_flatten.append(len(tmp_list))
            else:
                new_flatten.append(1)
            new_flatten.append(beads_flatten[i])
            tmp_list.clear()
    count = len(new_flatten)
    l = n**2 -1

    if count <= l:
        beads_flatten = new_flatten[:] + [0]*(n**2-count-1)
    else:
        beads_flatten = new_flatten[:l]
        count = l
    # print('change')
    # print('count',count)
    # print(beads_flatten, len(beads_flatten))


n, m = map(int, input().split())
beads_color = []
beads_order = []
beads_flatten = []
order_dict = dict() # 순서, 좌표
position_dict = dict() # 좌표, 순서
mid = n//2
shark = [mid, mid]
direction = [[0,-1], [1,0], [0,1], [-1,0]]
d_dict = {1:3 , 2:1 , 3:0 , 4:2}
result = 0
beads_orders()
for _ in range(n):
    beads_color.append(list(map(int, input().split())))

count = 0
for a,b in beads_order:
    if beads_color[a][b] != 0:
        count += 1
    beads_flatten.append(beads_color[a][b])

for kk in range(m):
    d, s = map(int, input().split())
    # 구슬 파괴
    x = y = mid
    tmp = 0
    for i in range(s):
        x += direction[d_dict[d]][0]
        y += direction[d_dict[d]][1]
        if beads_flatten[position_dict[(x,y)]] != 0:
            tmp += 1
            beads_flatten[position_dict[(x,y)]] = 0

    move([1]*tmp)
    while True:
        f, z_list = explosion()
        if f == 0:
            break
        move(z_list)
    change()


print(result)

