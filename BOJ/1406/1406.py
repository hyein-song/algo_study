import collections
import sys

input_str = collections.deque(sys.stdin.readline().strip())
str_right = collections.deque()
n = int(sys.stdin.readline().strip())
len_str = len(input_str)
for i in range(n):
    order = sys.stdin.readline().strip()
    if order[0] == 'L' and input_str:
        str_right.appendleft(input_str.pop())

    elif order[0] == 'D' and str_right:
        input_str.append(str_right.popleft())
    elif order[0] == 'B' and input_str:
        input_str.pop()

    elif order[0] == 'P':
        input_str.append(order[2])

print(''.join(input_str+str_right))