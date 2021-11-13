import collections
import heapq
import sys
max_val = sys.maxsize


def di(start):
    dist = {i: max_val for i in range(1,n+1)}
    dist[start] = 0
    q = []
    heapq.heappush(q,[dist[start],start])

    while q:
        cur_dist, cur_destination = heapq.heappop(q)

        if dist[cur_destination] > cur_dist:
            continue

        for new_destination, new_dist in graph[cur_destination]:
            distance = cur_dist + new_dist
            if distance < dist[new_destination]:
                dist[new_destination] = distance
                heapq.heappush(q, [distance,new_destination])
    # print(dist)

    cnt =  time = 0
    for k,v in dist.items():
        if v != max_val:
            cnt += 1
            time = max(time,v)
    return cnt,time


t = int(sys.stdin.readline().strip())

for _ in range(t):
    n,d,c = map(int, sys.stdin.readline().split())
    graph = collections.defaultdict(list)
    for _ in range(d):
        x,y,z = map(int, sys.stdin.readline().split())
        # graph[x].append([y,z])
        graph[y].append([x,z])
    print(*di(c))







