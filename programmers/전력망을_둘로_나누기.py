# 프로그래머스 전력망을 둘로 나누기

import collections

def solution(n, wires):
    answer = 100

    # 유니온파인드
    def find(x):
        if x == parent[x]:
            return x
        else:
            parent[x] = find(parent[x])
            return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    for i in range(n-1):
        parent = [i for i in range(n)]
        for j in range(n-1):
            if j != i:
                union(wires[j][0]-1, wires[j][1]-1)

        # 중요!! 순차적으로 유니온 파인드 하는것이기 때문에 처음부터 한번 더 해줘야 함
        for i in range(n):
            parent[i] = find(i)

        counter = list(collections.Counter(parent).values())
        answer = min(answer, abs(counter[0]-counter[1]))

    return answer

# 테스트 케이스
n = 5
arr = []
for i in range(1,n):
    arr.append([i,i+1])
arr[0] = [1,n]

solution(n,	arr)
