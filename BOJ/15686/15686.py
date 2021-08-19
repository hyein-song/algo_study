import itertools
import sys
input = sys.stdin.readline

def distance(chickens):
    global min_distance
    city_distance = 0
    for h in house:
        tmp = 2*n
        for s_c in chickens:
            d = abs(h[0]-s_c[0]) + abs(h[1]-s_c[1])
            tmp = d if tmp > d else tmp

        city_distance += tmp
    min_distance = city_distance if min_distance > city_distance else min_distance


house = []
chicken = []
n, m = map(int, input().split())
min_distance = 10e6

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1:
            house.append([i, j])
        elif tmp[j] == 2:
            chicken.append([i, j])

selected_chicken = list(itertools.combinations(chicken, m))

for c in selected_chicken:
    distance(c)

print(min_distance)
