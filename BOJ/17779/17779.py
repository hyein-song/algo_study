import collections
import sys
input = sys.stdin.readline

def line(x,y,d1,d2):
    new_table = [[0 for _ in range(n)] for _ in range(n)]
    l_dict = collections.defaultdict(set)
    global total_people
    global result
    sum_people = [0,0,0,0,0]

    for i in range(d1+1):
        for j in range(d2+1):
            l_dict[x+i].add(y-i)
            l_dict[x + j].add(y + j)
            l_dict[x + i+j].add(y - i+j)
            l_dict[x + i+j].add(y + j-i)

    for a, b in l_dict.items():
        b = sorted(list(b))
        for i in range(b[0], b[-1]+1):
            new_table[a][i] = 5

    for i in range(x+d1):
        for j in range(y+1):
            if new_table[i][j] != 5:
                new_table[i][j] = 1

    for i in range(x+d2+1):
        for j in range(y+1, n):
            if new_table[i][j] != 5:
                new_table[i][j] = 2

    for i in range(x+d1,n):
        for j in range(y-d1+d2):
            if new_table[i][j] != 5:
                new_table[i][j] = 3

    for i in range(x+d2+1,n):
        for j in range(y-d1+d2,n):
            if new_table[i][j] != 5:
                new_table[i][j] = 4

    for i in range(n):
        for j in range(n):
            sum_people[new_table[i][j]-1] += table[i][j]

    r = max(sum_people) - min(sum_people)
    if result > r:
        result = r


n = int(input())
table = []
total_people = 0

for _ in range(n):
    tmp = list(map(int, input().split()))
    table.append(tmp)
    total_people += sum(tmp)

result = total_people

for x in range(n):
    for y in range(n):
        for d1 in range(1, y+1):
            for d2 in range(1, n-y):
                if 2 <= d1+d2 < n-x:
                    line(x, y, d1, d2)


print(result)