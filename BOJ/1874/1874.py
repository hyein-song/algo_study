import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
b = 0
for i in range(1, n+1):
    a = int(input())
    if not stack or stack[-1] < a:
        for j in range(b+1,a+1):
            stack.append(j)
            result.append('+')
        stack.pop()
        result.append('-')
        b = a
    elif stack[-1] == a:
        stack.pop()
        result.append('-')
    else:
        break

if i == n:
    for r in result:
        print(r)
else:
    print('NO')