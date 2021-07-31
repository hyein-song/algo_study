# -*- coding: utf-8 -*-
"""BOJ_1038.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sJdT3mCAFqBDt-Hr6pQNuo95txTboRKD
"""

n = int(input())
result = []

def dfs(x):
    if len(x) == 1:
        result.append(int(x))
    
    if len(x) == 10 :
        return

    for i in range(int(x[0])+1, 10):
        new_x = str(i)+x
        result.append(int(new_x))
        dfs(new_x)
    return

for i in range(0,10):
    dfs(str(i))

result.sort()
if n > len(result)-1:
    print('-1')
else:
    print(result[n])
