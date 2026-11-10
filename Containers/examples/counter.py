from collections import Counter

sides = Counter(["buy", "sell", "buy", "buy"])
print(sides.most_common(1), sides["flat"])
# [('buy', 3)] 0   missing key -> 0
print(Counter(a=3, b=1) - Counter(a=1, b=2))
# Counter({'a': 2})  negatives dropped

print(sides)