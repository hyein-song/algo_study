import collections


def largestComponentSize(nums):
    n = len(nums)
    parent = [i for i in range(n)]

    def divisor(num):
        for i in range(2, int(num**(1/2) + 1)):
            if num % i == 0:
                return divisor(num//i) | {i}
        return {num}

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    primes = collections.defaultdict(list)
    for idx, num in enumerate(nums):
        diviso_set = divisor(num)
        for ds in diviso_set:
            primes[ds].append(idx)

    # print(primes)
    for _, indexes in primes.items():
        for i in range(len(indexes)-1):
            union(indexes[i], indexes[i+1])

    return max(collections.Counter([find(i) for i in range(n)]).values())

largestComponentSize([20,50,9,63])
# largestComponentSize([65,35,43,76,15,11,81,22,55,92,31])
largestComponentSize([84,171,548,709,455,967,328,779,79,16,168,675,276,473,697,26,731,668,634,607])