
def dfs(d,m):
    global result
    if d == n+1:
        result = max(result, m)
        return
    if d+works[d][0] <= n+1:
        dfs(d+works[d][0], m+works[d][1])
    if works[d][0] != 1:
        dfs(d+1, m)

n = int(input())
works = [[]]
result = 0
for _ in range(n):
    works.append(list(map(int, input().split())))
dfs(1,0)
print(result)