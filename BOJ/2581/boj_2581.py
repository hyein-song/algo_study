# -*- coding: utf-8 -*-
"""BOJ_2581.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RyJMZIFW0n00WTOWRh70Dfh4ItlPwCGL
"""

# 아라토스테네스의 체
m = int(input())
n = int(input())
b = list()

first_list = [1]*(n+1)
sqrt_n = int(n ** 0.5)

for i in range(2, sqrt_n+1):
    if first_list[i] == 1: 
        for j in range(i+i,n+1,i):
            first_list[j] = 0  

for i in range(m,n+1):
    if (first_list[i] == 1) & (i > 1):
        b.append(i)

if len(b) == 0:
    print('-1')
else:          
    print(sum(b))
    print(min(b))