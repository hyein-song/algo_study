import collections
import heapq
import sys

max_val = int(1e9)

def di(start):
    dist = [max_val for _ in range(n+1)]
    dist[start] = 0
    q = []
    heapq.heappush(q,[dist[start],start])

    while q:
        cur_dist, cur_destination = q.pop()

        if cur_dist > dist[cur_destination]:
            continue

        for next_destination, next_dist in graph[cur_destination]:
            distance = next_dist + cur_dist
            if distance < dist[next_destination]:
                dist[next_destination] = distance
                heapq.heappush(q,[distance,next_destination])

    return dist


T = int(sys.stdin.readline().strip())
for _ in range(T):
    n,m,t = map(int, sys.stdin.readline().split())
    s,g,h = map(int, sys.stdin.readline().split())
    graph = collections.defaultdict(list)

    for _ in range(m):
        a,b,d = map(int, sys.stdin.readline().split())
        if (a==g and b==h ) or (a==h and b==g) :
            graph[a].append([b, 2*d-1])
            graph[b].append([a, 2*d-1])
        else:
            graph[a].append([b,2*d])
            graph[b].append([a,2*d])

    result = []
    dist = di(s)
    # print(dist)
    for _ in range(t):
        x = int(sys.stdin.readline().strip())
        if dist[x] % 2 == 1:
            result.append(x)

    result.sort()
    print(*result)


