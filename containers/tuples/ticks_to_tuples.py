import random
from datetime import datetime as dt
from datetime import timedelta as td


rng = random.Random()
print(rng)  

init_bid= 1.1300
timestamp = dt.strptime("2026-11-01 00:00:00", "%Y-%m-%d %H:%M:%S")

price_time_series = []

for i in range(1000):
    bid = init_bid + round(rng.gauss(0, 0.0002), 4)
    spread = abs(round(rng.gauss(0, 0.0008), 4))
    ask = round((bid + spread), 4)
    time_delta = rng.gauss(0, 2)
    timestamp += td(0, time_delta)
    tick_row = (timestamp, bid, ask)
    price_time_series.append(tick_row)
    init_bid = bid


print(price_time_series)