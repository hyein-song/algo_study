import collections
import copy
import sys


def move(total):
    global table
    # 현재 자리에 냄새 뿌리기
    for key, value in sharks.items():
        if value:
            smell[value[0]][value[1]] = [key, k]
    # print('smell',smell)
    # 다음 방향 선택 후 상어 옮김
    new_table = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m, 0, -1):
        if sharks[i]:
            # print('shark num',i)
            x, y, d = sharks[i]
            # print(x,y,d)
            can_go = [[], []] # 아무냄새 없을때, 자신의 냄새
            for j in range(1,5):
                nx = x + directions[j][0]
                ny = y + directions[j][1]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if smell[nx][ny] == 0:
                    can_go[0].append(j)
                elif smell[nx][ny][0] == i:
                    can_go[1].append(j)
            # print('cango',can_go)
            if can_go[0]:
                if len(can_go[0]) >= 2:
                    for s_d in sharks_d[i-1][d-1]:
                        if s_d in can_go[0]:
                            new_d = s_d
                            break
                else:
                    new_d = can_go[0][0]
            elif can_go[1]:
                if len(can_go[1]) >= 2:
                    for s_d in sharks_d[i-1][d-1]:
                        if s_d in can_go[1]:
                            new_d = s_d
                            break
                else:
                    new_d = can_go[1][0]
            # print('new_d',new_d)
            nx = x + directions[new_d][0]
            ny = y + directions[new_d][1]
            # print('nx,ny',nx,ny)
            if new_table[nx][ny] != 0:
                total -= 1
                sharks[new_table[nx][ny]] = []
            new_table[nx][ny] = i
            # smell[nx][ny] = [i, k]
            sharks[i] = [nx, ny, new_d]
        table = copy.deepcopy(new_table)

    # 이전 냄새들 -1
    for i in range(n):
        for j in range(n):
            if smell[i][j]:
                shark_num, cnt = smell[i][j]
                if cnt - 1 == 0:
                    smell[i][j] = 0
                else:
                    smell[i][j] = [shark_num, cnt - 1]
    # print('after smell',smell)
    return total


# def move_first():
#     global table
#     for key, value in sharks.items():
#         smell[value[0]][value[1]] = [key, k]
#
#     new_table = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(m - 1, -1, -1):
#         if sharks[i]:
#             x, y, d = sharks[i]
#             nx = x + directions[d][0]
#             ny = y + directions[d][1]
#
#             if new_table[nx][ny] != 0:
#                 sharks[new_table[nx][ny]] = []
#             new_table[nx][ny] = i
#             smell[nx][ny] = [i, k]
#             sharks[i] = [nx, ny, d]
#     table = copy.deepcopy(new_table)
#
#     for i in range(n):
#         for j in range(n):
#             if smell[i][j]:
#                 shark_num, cnt = smell[i][j]
#                 if cnt - 1 == 0:
#                     smell[i][j] = 0
#                 else:
#                     smell[i][j] = [shark_num, cnt - 1]
#     return


n,m,k = map(int, input().split())
total = m
directions = [[],[-1,0],[1,0],[0,-1],[0,1]]
table = [[0 for _ in range(n)] for _ in range(n)]
smell = []
sharks = dict()
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] != 0:
            sharks[tmp[j]] = [i, j]
    smell.append(tmp)

sharks_first_d = list(map(int, input().split()))
for i in range(1,m+1):
    sharks[i].append(sharks_first_d[i-1])

sharks_d = []
for i in range(m):
    tmp = []
    for j in range(4):
        tmp.append(list(map(int, input().split())))
    sharks_d.append(tmp)

# print('start')
# print(sharks)
for result in range(1,1001):
    total = move(total)
    # print(result)
    # print(sharks)
    # print(table)
    if total == 1:
        print(result)
        sys.exit(0)

print(-1)

