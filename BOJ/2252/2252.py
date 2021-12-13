import collections
import sys

n, m = map(int, sys.stdin.readline().split())
cnt = [0] * (n+1)
graph = {i:[] for i in range(1,n+1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    cnt[b] += 1
    graph[a].append(b)


q = collections.deque()
for i in range(1,n+1):
    if cnt[i] == 0:
        q.append(i)

result = []
while q:
    x = q.popleft()
    result.append(x)
    for next_idx in graph[x]:
        cnt[next_idx] -= 1
        if cnt[next_idx] == 0:
            q.append(next_idx)

print(*result)