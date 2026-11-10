from collections import defaultdict


# grouping example
by_ccy = defaultdict(list)

for pair in ["EURUSD", "GBPUSD", "EURJPY"]:
    by_ccy[pair[:3]].append(pair)

print(dict(by_ccy))


