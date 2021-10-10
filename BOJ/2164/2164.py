import collections
import sys

n = int(sys.stdin.readline())
a = collections.deque([i for i in range(1,n+1)])

for i in range(n-1):
    a.popleft()
    a.append(a.popleft())

print(a[0])