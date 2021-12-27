
#https://programmers.co.kr/learn/courses/30/lessons/42587
import collections
import heapq


def solution(priorities, location):
    q = collections.deque()

    for idx, p in enumerate(priorities):
        q.append([p, idx])

    cnt = 1
    while q:
        q_val, q_idx = q.popleft()
        max_in_q = 0
        for qq, _ in q:
            max_in_q = max(max_in_q, qq)

        if max_in_q > q_val:
            q.append([q_val, q_idx])
        else:
            if q_idx == location:
                return cnt
            else:
                cnt += 1
    return cnt