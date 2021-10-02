

def dfs(depth, total):
    global max_val
    # print('------------')
    # print(depth,total)
    if depth == 10:
        # print(h,total)
        return

    for i in range(4):
        h_count, h_direction = h[i]
        calc = h_count + nums[depth]
        tmp = h[i][:]
        # print('origin')
        # print(i,h[i],calc)
        if h_direction == 0 and calc <= 20: # 게임판 안넘어가는
            if calc == 20:
                if [3,4] in h:
                    continue
                new_total = total + 40
                h[i] = [3, 4]
            else:
                if calc % 5 == 0:
                    new_direction = calc // 5
                    if [calc, new_direction] in h:
                        continue
                    new_total = total + 2 * calc
                    h[i] = [calc, new_direction]
                else:
                    if [calc, 0] in h:
                        continue
                    new_total = total + 2 * calc
                    h[i] = [calc, 0]

        elif h_direction == 1 and calc <= 12:
            if calc == 12:
                if [3,4] in h:
                    continue
                h[i] = [3, 4]
                new_total = total + 40

            elif calc >= 9:
                if [calc-9, 4] in h:
                    continue
                h[i] = [calc - 9, 4]
                new_total = total + maps[3][calc-9]
            else:
                if [calc, 1] in h:
                    continue
                h[i] = [calc,1]
                new_total = total + maps[0][calc-6]

        elif h_direction == 2 and calc <= 16:
            if calc == 16:
                if [3,4] in h:
                    continue
                new_total = total + 40
                h[i] = [3, 4]
            elif calc >= 13:
                if [calc-13, 4] in h:
                    continue
                h[i] = [calc - 13, 4]
                new_total = total + maps[3][calc-13]
            else:
                if [calc,2] in h:
                    continue
                h[i] = [calc,2]
                new_total = total + maps[1][calc - 11]

        elif h_direction == 3 and calc <= 22:
            if calc == 22:
                if [3,4] in h:
                    continue
                h[i] = [3, 4]
                new_total = total + 40
            elif calc >= 19:
                if [calc-19, 4] in h:
                    continue
                h[i] = [calc - 19, 4]
                new_total = total + maps[3][calc-19]
            else:
                if [calc,3] in h:
                    continue
                h[i] = [calc,3]
                new_total = total + maps[2][calc - 16]
        elif h_direction == 4 and calc <=3:
            if calc == 3:
                if [3,4] in h:
                    continue
                h[i] = [3, 4]
                new_total = total + 40
            elif [calc,4] in h:
                continue
            else:
                h[i] = [calc,4]
                new_total = total + maps[3][calc]
        else:
            h[i] = [4, 4]
            new_total = total

        # print('new',depth,i,h,calc,new_total)
        if new_total > max_val:
            max_val = new_total

        dfs(depth + 1, new_total)
        h[i] = tmp[:]
    return


nums = list(map(int, input().split()))
max_val = 0
h = [[0,0], [0,0], [0,0], [0,0]] # count, 방향

maps = [[13,16,19],
        [22,24],
        [28,27,26],
        [25,30,35,40]]

dfs(0,0)
print(max_val)