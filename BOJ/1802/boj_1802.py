# -*- coding: utf-8 -*-
"""BOJ_1802.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QNE8IUEaS0XFGBg6jBnUwSBmSlbsS8Sj
"""

t = int(input())

for _ in range(t):
    case = input()
    flag = True
    n = len(case)
    if n >= 3:
        while n >= 1:
            mid = n // 2
            L_case = case[:mid]
            R_case = case[mid+1:]
            for i in range(mid):
                if L_case[i] == R_case[-i-1]:
                    flag = False
                    break
            if not flag:
                break
            case = L_case
            n = mid
    if flag:
        print('YES')
    else:
        print('NO')