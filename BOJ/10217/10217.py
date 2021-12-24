import collections
import sys
max_val = sys.maxsize

def di(graph,n,m):
    dp = [[max_val for _ in range(m+1)] for _ in range(n+1)]
    dp[1][0] = 0
    q = collections.deque()
    q.append([1, 0, 0])

    while q:
        cur_destination, cur_cost, cur_distance = q.popleft()
        if cur_distance > dp[cur_destination][cur_cost]:
            continue

        for new_destination, new_cost, new_dist in graph[cur_destination]:
            distance = cur_distance + new_dist
            total_cost = cur_cost + new_cost
            if total_cost > m:
                continue
            if distance < dp[new_destination][total_cost]:
                for i in range(total_cost,m+1):
                    if distance < dp[new_destination][i]:
                        dp[new_destination][i] = distance
                    else:
                        break
                q.append([new_destination,total_cost,distance])

    return min(dp[-1])

def main():
    t = int(sys.stdin.readline().rstrip())
    graph = collections.defaultdict(list)
    for _ in range(t):
        n, m, k = map(int, sys.stdin.readline().split())

        for _ in range(k):
            u, v, c, d = map(int, sys.stdin.readline().split())
            graph[u].append([v, c, d])

        #다익스트라
        result = di(graph,n,m)
        if result == max_val:
            print('Poor KCM')
        else:
            print(result)
        graph.clear()

main()












