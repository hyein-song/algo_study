
#https://programmers.co.kr/learn/courses/30/lessons/42586
import collections

def solution(progresses, speeds):
    days = collections.deque()
    for p, s in zip(progresses, speeds):
        a, b = divmod(100 - p, s)
        if b == 0:
            days.append(a)
        else:
            days.append(a + 1)

    n = len(days)
    left = days.popleft()
    cnt = 1
    result = []
    for i in range(n - 1):
        x = days.popleft()

        if left < x:
            result.append(cnt)
            cnt = 1
            left = x
        else:
            cnt += 1
    result.append(cnt)

    return result