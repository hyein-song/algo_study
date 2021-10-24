import collections
import heapq
import sys
max_val = sys.maxsize


def di(start, end):
    dist = [max_val for _ in range(n)]
    visited_cities = [-1 for _ in range(n)]
    dist[start] = 0
    q = []
    heapq.heappush(q, [dist[start], start])

    while q:
        cur_distance, cur_destination = heapq.heappop(q)

        if dist[cur_destination] < cur_distance:
            continue

        for new_destination, new_distance in graph[cur_destination]:
            distance = new_distance + cur_distance
            if distance < dist[new_destination]:
                # print(cur_distance, cur_destination,new_destination, new_distance,distance)
                dist[new_destination] = distance
                visited_cities[new_destination] = cur_destination
                heapq.heappush(q,[distance,new_destination])
    print(dist[end])
    result = [end+1]
    tmp = end
    while True:
        a = visited_cities[tmp]
        if a == -1:
            break
        result.append(a+1)
        tmp = a
    result.reverse()
    print(len(result))
    print(*result)


n = int(sys.stdin.readline())
graph = collections.defaultdict(list)
m = int(sys.stdin.readline())
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1].append([b-1,c])
# print(graph)
x, y = map(int, sys.stdin.readline().split())
di(x-1,y-1)
