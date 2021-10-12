import sys
max_val = sys.maxsize
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[0 if i == j else max_val for i in range(v)] for j in range(v)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c

# 플로이드 와샬
for i in range(v):
    for j in range(v):
        for k in range(v):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

result = max_val
for i in range(v):
    for j in range(v):
        if i != j and graph[i][j] != max_val and graph[j][i] != max_val:
            result = min(result, graph[i][j]+graph[j][i])

if result == max_val:
    print(-1)
else:
    print(result)
