

def spring_and_summer():
    for i in range(n):
        for j in range(n):
            if tree[i][j] == []:
                continue
            trees = tree[i][j]
            trees = sorted(trees)
            new_trees = []
            die = 0
            for t in trees:
                if ground[i][j] - t >= 0:
                    ground[i][j] -= t
                    new_trees.append(t+1)
                else:
                    die += (t//2)
            ground[i][j] += die
            tree[i][j] = new_trees[:]


def fall():
    for i in range(n):
        for j in range(n):
            trees = tree[i][j]
            breed = 0
            for t in trees:
                if t != 0 and t % 5 == 0:
                    breed += 1

            if breed > 0:
                for k in range(8):
                    ni = i + move[0][k]
                    nj = j + move[1][k]
                    if 0 <= ni < n and 0 <= nj < n:
                        for _ in range(breed):
                            tree[ni][nj].append(1)

def winter():
    for i in range(n):
        for j in range(n):
            ground[i][j] += food[i][j]


def count_trees():
    cnt = 0
    for i in range(n):
        for j in range(n):
            for t in range(len(tree[i][j])):
                if tree[i][j][t] != 0:
                    cnt += 1
    return cnt


n, m, k = map(int,input().split())
move = [[-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]]

ground = [[5 for _ in range(n)]for _ in range(n)]
tree = [[[]for _ in range(n)] for _ in range(n)]
food = []
for _ in range(n):
    food.append(list(map(int, input().split())))

for _ in range(m):
    a, b, c = map(int, input().split())
    tree[a-1][b-1].append(c)

for i in range(k):
    spring_and_summer()
    fall()
    winter()

result = count_trees()
print(result)
