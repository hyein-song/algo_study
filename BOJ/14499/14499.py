def check_bound(new_now):
    if 0 <= new_now[0] < n and 0 <= new_now[1] < m:
        return True
    return False


n, m, x, y, k = map(int, input().split())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

now = [x, y]
dice = [0,0,0,0,0,0] # top,left,bottom,right,front,back
move = [[0,0,-1,1],[1,-1,0,0]]

for d in directions:

    new_now = [now[0] + move[0][d-1], now[1] + move[1][d-1] ]
    if not check_bound(new_now):
        continue
    now = new_now

    if d == 1:
        pre = dice[:]
        dice = [pre[1], pre[2], pre[3], pre[0], pre[4], pre[5]]

    elif d == 2:
        pre = dice[:]
        dice = [pre[3], pre[0], pre[1], pre[2], pre[4], pre[5]]

    elif d == 3:
        pre = dice[:]
        dice = [pre[4], pre[1], pre[5], pre[3], pre[2], pre[0]]

    elif d == 4:
        pre = dice[:]
        dice = [pre[5], pre[1], pre[4], pre[3], pre[0], pre[2]]


    if table[now[0]][now[1]] != 0:
        dice[2] = table[now[0]][now[1]]
        table[now[0]][now[1]] = 0
    else:
        table[now[0]][now[1]] = dice[2]

    print(dice[0])