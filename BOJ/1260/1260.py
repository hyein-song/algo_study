import collections

def dfs(x):

    len_graph = len(graph[x])

    if len_graph == 0:
        return

    vals = sorted(graph[x])

    for next_val in vals:
        if visited[next_val]==0:
            visited[next_val] = 1
            dfs_result.append(next_val)
            dfs(next_val)

    return

def bfs(v):
    visited = {i:0 for i in range(1,n+1)}
    visited[v] = 1
    q = collections.deque()
    q.append(v)
    result = []
    while q:
        v = q.popleft()
        result.append(v)
        vals = sorted(graph[v])
        for next_val in vals:
            if visited[next_val] == 0:
                visited[next_val] =1
                q.append(next_val)

    return result


n,m,v = map(int, input().split())
graph = collections.defaultdict(list)
visited = {i:0 for i in range(1,n+1)}
dfs_result = [v]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[v]=1
dfs(v)
print(*dfs_result)

print(*bfs(v))