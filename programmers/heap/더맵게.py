
#https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    cnt = 0
    while True:
        if len(scoville) == 1:
            return -1

        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)

        if a == 0 and b == 0:
            return -1

        heapq.heappush(scoville, a + b * 2)
        c = heapq.heappop(scoville)
        cnt += 1
        if c >= K:
            break
        else:
            heapq.heappush(scoville, c)
    return cnt
