"""
A trade blotter is a list of trades, each a tuple (trade_id, pair, side, qty, price). 
Write nine small functions that answer the questions a desk asks every day. 
Each one needs only what you saw today; the docstrings say which tool to reach for.
The grader at the bottom of the file checks every function, including that you do not modify the input list.
"""


"""Trade blotter basics: list, tuple, dict and set only.
Each trade is a tuple: (trade_id, pair, side, qty, price).
Fill in every TODO, then run this file: the grader at the bottom must pass."""

from collections import Counter

def pairs_traded(trades):
    """Distinct pairs, sorted alphabetically, as a list."""

    instruments = list({trade[1] for trade in trades})
    instruments.sort()
    return instruments

def count_by_pair(trades):
    """{pair: number of trades}, pairs in first-seen order."""
    instruments = list([trade[1] for trade in trades])
    count = Counter(instruments)
    return dict(count)

def buys(trades):
    """Only the trades whose side is "buy", in their original order."""
    buy_trades = list([trade for trade in trades if trade[2]=="buy"])
    return buy_trades

def last_n(trades, last_n):
    """The last n trades as a list. last_n(trades, 0) must be []."""
    if last_n == 0:
        return []
    last_trades = trades[-last_n:]
    return last_trades


def by_id(trades):
    """{trade_id: trade} for fast lookup by id."""
    trade_by_id= {trade[0]: trade for trade in trades}
    return trade_by_id

def biggest(trades):
    """The trade with the largest qty."""
    trades_sorted_by_amount = sorted(trades, key=lambda t: t[3], reverse=True)
    return trades_sorted_by_amount[0]
    
def total_notional(trades):
    """Sum of qty * price over all trades."""
    return  sum([t[3]*t[4] for t in trades])
    
def net_qty(trades):
    """{pair: bought qty minus sold qty}."""
    pairs = pairs_traded(trades)

    summary = dict.fromkeys(pairs, 0)

    for t in trades:
        summary[t[1]] += t[3] if t[2]=="buy" else -t[3]

    return summary




def summary(trades):
    """(number of trades, number of distinct pairs, total notional rounded to 2 dp)."""
    raise NotImplementedError            # TODO: a tuple built from the functions above

# ---------------- grader: run this file; every assert must pass ----------------
TRADES = [  # (trade_id, pair, side, qty, price)
    ("T1", "EURUSD", "buy", 100_000, 1.0840),
    ("T2", "GBPUSD", "sell", 50_000, 1.2650),
    ("T3", "EURUSD", "sell", 40_000, 1.0850),
    ("T4", "USDJPY", "buy", 20_000, 151.20),
    ("T5", "EURUSD", "buy", 10_000, 1.0845),
]

assert pairs_traded(TRADES) == ["EURUSD", "GBPUSD", "USDJPY"]
assert count_by_pair(TRADES) == {"EURUSD": 3, "GBPUSD": 1, "USDJPY": 1}
assert [t[0] for t in buys(TRADES)] == ["T1", "T4", "T5"]
assert last_n(TRADES, 2) == TRADES[3:] and last_n(TRADES, 0) == []
assert by_id(TRADES)["T3"] == ("T3", "EURUSD", "sell", 40_000, 1.0850)
assert biggest(TRADES) == TRADES[0]
assert round(total_notional(TRADES), 2) == 3_249_895.0
assert net_qty(TRADES) == {"EURUSD": 70_000, "GBPUSD": -50_000, "USDJPY": 20_000}
assert summary(TRADES) == (5, 3, 3_249_895.0)
assert summary([]) == (0, 0, 0.0)
assert TRADES[0] == ("T1", "EURUSD", "buy", 100_000, 1.0840), "do not modify the input"
print("all checks passed")