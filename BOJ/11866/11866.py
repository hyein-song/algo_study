import collections

n, k = map(int, input().split())
a = [i for i in range(1,n+1)]
result = []
nn = n
idx = k-1
result.append(a.pop(idx))
while a:
    if idx + k - 1 < len(a):
        idx += k - 1
        result.append(a.pop(idx))
    else:
        idx = (idx + k-1) % len(a)
        result.append(a.pop(idx))
print('<', end='')
for i in range(n-1):
    print(result[i], end =', ')
print(result[-1],end='>')
