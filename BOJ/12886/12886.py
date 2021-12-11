import collections


def bfs(a,b,c):
    q = collections.deque()
    q.append([a, b])
    visited = [[0 for _ in range(1501)] for _ in range(1501)]
    visited[a][b] = 1
    total = a+b+c
    while q:
        a, b = q.popleft()
        c = total - a - b
        if a ==b==c:
            return 1
        for x,y in ((a,b),(b,c),(a,c)):
            if x == y :
                continue
            if x < y:
                y -= x
                x += x
            elif x > y:
                x -= y
                y += y
            z = total - x - y
            a = min(x,y,z)
            b = max(x,y,z)
            if visited[a][b] == 0:
                visited[a][b] = 1
                q.append([a,b])

    return 0


a, b, c = map(int, input().split())
if (a+b+c) % 3 != 0:
    print(0)
else:
    print(bfs(a,b,c))
