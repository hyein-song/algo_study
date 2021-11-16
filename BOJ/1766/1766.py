import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(n)}
nums = [0 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    nums[b-1] += 1

can = []
for i in range(n):
    if nums[i] == 0:
        can.append(i)


heapq.heapify(can)
result = []
while can:
    x = heapq.heappop(can)
    result.append(x+1)
    for i in graph[x]:
        nums[i] -= 1
        if nums[i] == 0:
            heapq.heappush(can,i)

print(*result)

