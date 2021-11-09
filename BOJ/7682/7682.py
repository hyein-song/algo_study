import operator


def ttt(nums):
    num_o = 0
    num_x = 0
    for i in range(9):
        if nums[i] == 'O':
            num_o += 1
        elif nums[i] == 'X':
            num_x += 1
    if num_x - num_o > 1 or num_x < num_o:
        # print('갯수 차이')
        return False

    table = []
    for i in range(3):
        tt = []
        for j in range(3):
            tt.append(nums[i*3+j])
        table.append(tt)

    # print(table)
    char = ['O', 'X']
    check = [0, 0]

    # 한사람이 한 줄 다 써서 통과
    for i in range(3):
        for j in range(3):
            for m in range(2):
                if (i == 0 or j == 0) and table[i][j] == char[m]:
                    for k in range(8):
                        ni = i
                        nj = j
                        cnt = 0
                        for l in range(2):
                            ni += move[k][0]
                            nj += move[k][1]
                            if 0 <= ni < 3 and 0 <= nj < 3 and table[ni][nj] == char[m]:
                                cnt += 1
                            else:
                                break
                        if cnt == 2:
                            check[m] = 1
                            # if m == 0: # O
                            #     if num_o < num_x:
                            #         check[m] = 0
                            #     else:
                            #         check[m] = 1
                            # else:
                            #     check[m] = 1
    # print(check)
    if check[0] and check[1]:
        return False
    elif check[0] == 1:
        if num_x > num_o:
            return False
        else:
            return True
    elif check[1] == 1:
        if num_x == num_o:
            return False
        else:
            return True
    elif check[0] ==0 and check[1] == 0:
        if num_x+num_o == 9:
            return True
        else:
            return False

    return True


move = [[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]]
kk = 1
while True:
    tmp = input()
    if tmp == 'end':
        break
    # print(kk)
    if ttt(list(tmp)):
        print('valid')
    else:
        print('invalid')
    kk += 1