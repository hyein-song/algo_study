# -*- coding: utf-8 -*-
"""BOJ_10818.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wRt-s0dyZxC9Mp-kPN7Dxlvaho9bYHH3
"""

n = int(input())
a = list(map(int, input().split()))

print(min(a), max(a))

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums[0],nums[-1])