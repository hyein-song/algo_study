# -*- coding: utf-8 -*-
"""BOJ_10870.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FkiQ-rTtPvydW3lzPfnqCw0SK8CNx2jB
"""

def fibo(x):
    if len(f) <= x:
        f.append(fibo(x-1) + fibo(x-2))
    return f[x]

n = int(input())
f = [0,1]
print(fibo(n))