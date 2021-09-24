


while True:
    s = input()
    f = 1
    if s == '.':
        break
    stack = []
    for ss in s:
        if ss in ['(','[']:
            stack.append(ss)
        elif ss == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                f = 0
                break
        elif ss == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                f = 0
                break
    if f and not stack:
        print('yes')
    else:
        print('no')