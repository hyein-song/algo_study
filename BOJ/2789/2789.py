import itertools

n, m = map(int, input().split())
cards = list(map(int, input().split()))

cards_combinations = list(itertools.combinations(cards, 3))

min_diff = m
result = 0
for i in cards_combinations:
    card_sum = sum(i)
    calc = m-card_sum
    if 0 <= calc <= min_diff:
        min_diff = calc
        result = card_sum

print(result)
