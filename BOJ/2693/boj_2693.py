# -*- coding: utf-8 -*-
"""BOJ_2693.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qx68xlkXBIR_dVmBDdRTCT3aTbKKehih
"""

t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    a.sort()
    print(a[-3])