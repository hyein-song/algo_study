import sys

a = input()

stack = []
for i in a:
    if i == '(' or i== '[':
        stack.append(i)
    elif stack:
        if i == ")":
            if stack[-1] == "(":
                stack[-1] = 2
            else:
                tmp = 0
                for j in range(len(stack)):
                    if stack[-1] == "(":
                        stack[-1]= tmp*2
                        break
                    elif stack[-1] == "[":
                        print(0)
                        sys.exit(0)
                    else:
                        tmp+=stack[-1]
                        stack.pop()
        if i == "]":
            if stack[-1] == "[":
                stack[-1] = 3
            else:
                tmp = 0
                for j in range(len(stack)):
                    if stack[-1] == "[":
                        stack[-1] = tmp * 3
                        break
                    elif stack[-1] == "(":
                        print(0)
                        sys.exit(0)
                    else:
                        tmp += stack[-1]
                        stack.pop()
    else:
        break
if "(" in stack or "[" in stack or ")" in stack or "]" in stack:
    print(0)
else:
    print(sum(stack))
