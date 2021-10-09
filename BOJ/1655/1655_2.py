# 내가 꾸역꾸역
import heapq
import sys

n = int(sys.stdin.readline())
hq_min = []
hq_max = []
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
if n == 1:
    print(l[0])
    sys.exit(0)
a = l[0]
if l[0] <= l[1]:
    heapq.heappush(hq_min, -a)
else:
    heapq.heappush(hq_max, a)
mid = a
print(mid)
for i in range(1,n):
    # print('first', hq_min, hq_max)
    a = l[i]
    if mid >= a:
        heapq.heappush(hq_min, -a)
    else:
        heapq.heappush(hq_max, a)

    # print('after push', hq_min, hq_max)
    if len(hq_min) >= len(hq_max):
        while len(hq_min) >= len(hq_max):
            # print(hq_min, hq_max)
            mid = -heapq.heappop(hq_min)
            heapq.heappush(hq_max, mid)
    else:

        while len(hq_min) < len(hq_max):
            # print(hq_min, hq_max)
            mid = heapq.heappop(hq_max)
            heapq.heappush(hq_min, -mid)
    print(mid)
    # print('end',hq_min,hq_max)