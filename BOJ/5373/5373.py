import copy


def turn(direction):
    a, b = direction
    if b == '+': # cw
        cnt = 1
    else:        # ccw
        cnt = 3

    if a == 'U':
        for _ in range(cnt):
            cw(0)
            tmp = cube[3][0][:]
            cube[3][0] = cube[4][0]
            cube[4][0] = cube[2][0]
            cube[2][0] = cube[5][0]
            cube[5][0] = tmp[:]

    elif a == 'D':
        for _ in range(cnt):
            cw(1)
            tmp = cube[3][2][:]
            cube[3][2] = cube[5][2]
            cube[5][2] = cube[2][2]
            cube[2][2] = cube[4][2]
            cube[4][2] = tmp[:]

    elif a == 'F':
        for _ in range(cnt):
            cw(2)
            tmp = cube[0][2][:]
            for i in range(3):
                cube[0][2][i] = cube[4][2-i][2]
            for i in range(3):
                cube[4][i][2] = cube[1][0][i]
            for i in range(3):
                cube[1][0][i] = cube[5][2-i][0]
            for i in range(3):
                cube[5][2 - i][0] = tmp[2-i]

    elif a == 'B':
        for _ in range(cnt):
            cw(3)
            tmp = cube[0][0][:]
            for i in range(3):
                cube[0][0][i] = cube[5][i][2]
            for i in range(3):
                cube[5][i][2] = cube[1][2][2-i]
            for i in range(3):
                cube[1][2][i] = cube[4][i][0]
            for i in range(3):
                cube[4][i][0] = tmp[2-i]

    elif a == 'L':
        for _ in range(cnt):
            cw(4)
            tmp = [cube[0][0][0],cube[0][1][0],cube[0][2][0]]
            for i in range(3):
                cube[0][i][0] = cube[3][2-i][2]
            for i in range(3):
                cube[3][2 - i][2] = cube[1][i][0]
            for i in range(3):
                cube[1][i][0] = cube[2][i][0]
            for i in range(3):
                cube[2][i][0] = tmp[i]

    elif a == 'R':
        for _ in range(cnt):
            cw(5)
            tmp = [cube[0][0][2],cube[0][1][2],cube[0][2][2]]
            for i in range(3):
                cube[0][i][2] = cube[2][i][2]
            for i in range(3):
                cube[2][i][2] = cube[1][i][2]
            for i in range(3):
                cube[1][i][2] = cube[3][2-i][0]
            for i in range(3):
                cube[3][2-i][0] = tmp[i]
    return

def cw(color):
    global cube
    face = copy.deepcopy(cube[color])
    new_f = [[0 for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            new_f[i][j] = face[2-j][i]

    cube[color] = copy.deepcopy(new_f)
    return


n = int(input())
# 0: U, 1: D, 2: F, 3:B, 4:L, 5:R
row = 0
col = 1

# w, y, r, o, g, b
cube_origin =  [[['w','w','w'],
                 ['w','w','w'],
                 ['w','w','w']],
                [['y','y','y'],
                 ['y','y','y'],
                 ['y','y','y']],
                [['r','r','r'],
                ['r','r','r'],
                ['r','r','r']],
                [['o','o','o'],
                ['o','o','o'],
                ['o','o','o']],
                [['g','g','g'],
                ['g','g','g'],
                ['g','g','g']],
                [['b','b','b'],
                 ['b','b','b'],
                 ['b','b','b']]]

for _ in range(n):
    cube = copy.deepcopy(cube_origin)
    a = int(input())
    l = list(input().split(' '))
    for i in range(a):
        turn(l[i])
    for i in range(3):
        print(''.join(cube[0][i]))