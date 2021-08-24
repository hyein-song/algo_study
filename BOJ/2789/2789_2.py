import itertools

n, m = map(int, input().split())
cards = list(map(int, input().split()))

cards_combinations = list(itertools.combinations(cards, 3))
cards_combi_sum = [sum(i) for i in cards_combinations if sum(i)<=m]

cards_combi_sum.sort()
print(cards_combi_sum[-1])

