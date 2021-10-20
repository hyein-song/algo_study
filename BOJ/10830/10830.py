import copy
import sys
input = sys.stdin.readline

def matrix_exp(arr1, arr2):
    global cnt
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += arr1[i][k] * arr2[k][j]
            result[i][j] = tmp % 1000
    return result

n, b = map(int, input().split())
arr = []
nb = bin(b)[2:]
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 단위 행렬
r = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

cnt = 1
for i in range(len(nb)):
    if nb[-i-1] == '1':
        # 2의 i 제곱만큼 행렬곱 그걸 result에 곱함
        tmp = copy.deepcopy(arr)
        while i != 0:
            tmp = matrix_exp(tmp, tmp)
            i -= 1
        r = matrix_exp(r,tmp)
for rr in r:
    print(*rr)





# 첫번째
# for i in range(n):
#     for j in range(n):
#         tmp = 0
#         for k in range(n):
#             # print(i,k, k,j)
#             # print(arr[i][k],arr[k][j])
#             tmp += arr[i][k]*arr[k][j]
#         result[i][j] = tmp
#
# # print(result)
# new_result = [[0 for _ in range(n)] for _ in range(n)]
# for _ in range(b-2):
#     for i in range(n):
#         for j in range(n):
#             tmp = 0
#             for k in range(n):
#                 # print(i, k, k, j)
#                 # print(result[i][k], arr[k][j])
#                 tmp += result[i][k] * arr[k][j]
#             new_result[i][j] = tmp % 1000
#     result = copy.deepcopy(new_result)
#     # print(result)