# -*- coding: utf-8 -*-
"""BOJ_2609.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AnHsgUIyxI4LWUYWjwFEV8uxIAYkkv-U
"""

a, b = map(int, input().split())
c = a*b
if a < b:
    a, b = b, a

while b!=0:
    a, b = b, a%b

print(a)
print(c // a)

import math

a, b = map(int, input().split())
r = math.gcd(a,b)
print(r)
print(a*b//r)

import math

a, b = map(int, input().split())
print(math.gcd(a,b))
print(math.lcm(a,b)) # 3.9 이상