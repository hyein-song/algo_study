# -*- coding: utf-8 -*-
"""BOJ_2805.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CQnfD2w3q9bLyGNqThJfCVb4D76Kn92E
"""

n , m = map(int, input().split())
trees = sorted(list(map(int, input().split())))

result = left = 0
right = trees[-1]


while left <= right:
    mid = left + (right-left) // 2
    total = sum([t-mid for t in trees if t > mid])
    
    if total < m:
        right = mid-1
    else:
        result = max(mid, result)
        left = mid+1

print(result)