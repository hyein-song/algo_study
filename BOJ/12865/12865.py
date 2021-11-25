




n, k = map(int, input().split())
items = []
for _ in range(n):
    items.append(list(map(int, input().split())))

table = [0 for _ in range(k+1)]

for i in range(1, n+1):
    for j in range(k,0,-1):
        if items[i-1][0] <=j:
            table[j] = max(table[j],table[j-items[i-1][0]] + items[i-1][1])

print(table[k])
