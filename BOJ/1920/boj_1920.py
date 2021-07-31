# -*- coding: utf-8 -*-
"""BOJ_1920.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12ABX-I-sdU30OqCkfCqRexP7leRpPuuP
"""

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))

for i in range(m):
    target = nums[i]
    left = 0
    right = n-1
    f=1
    while left<= right:
        mid = left + (right-left) // 2
        if a[mid] < target:
            left = mid+1
        elif a[mid] > target:
            right = mid-1
        else:
            print(1)
            f = 0
            break
    if f:        
        print(0)

import sys
import bisect
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))

for i in nums:
    index = bisect.bisect_left(a,i)
    print(1 if index < len(a) and a[index] == i else 0)