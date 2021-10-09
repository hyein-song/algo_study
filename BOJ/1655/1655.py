# 구글링
import heapq
import sys

n = int(sys.stdin.readline())
left = []
right = []
for i in range(n):
    a = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left, -a)
    else:
        heapq.heappush(right, a)

    if right and -left[0] > right[0]:
        min_ = heapq.heappop(right)
        max_ = -heapq.heappop(left)
        heapq.heappush(left, -min_)
        heapq.heappush(right, max_)

    print(-left[0])