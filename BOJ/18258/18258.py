import collections
import sys


def push(x):
    queue.append(x)


def pop():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.popleft())


def size():
    print(len(queue))


def empty():
    if len(queue) != 0:
        print(0)
    else:
        print(1)


def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])


def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])


n = int(input())
queue = collections.deque()

for _ in range(n):
    a = sys.stdin.readline().strip()
    if a == 'pop':
        pop()
    elif a == 'size':
        size()
    elif a == 'empty':
        empty()
    elif a == 'front':
        front()
    elif a == 'back':
        back()
    else:
        b, c = a.split()
        push(int(c))
