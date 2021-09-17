

n = int(input())
for _ in range(n):
    s = input()
    stack = []
    f = 1
    for ss in s:
        if ss == '(':
            stack.append(ss)
        elif ss == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                f = 0
                break
    if f and not stack:
        print('YES')
    else:
        print('NO')