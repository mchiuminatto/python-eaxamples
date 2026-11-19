"""
Defining equal seth __hash__ to none if not explicitly defined.

"""

from decimal import Decimal
from datetime import datetime

class Tick:
    def __init__(self, bid: float, ask: float, time: datetime):
        self.bid: Decimal = Decimal(bid)
        self.ask: Decimal = Decimal(ask)
        self.time = time    


    def __eq__(self, value):
        return (self.bid == value.bid) and (self.ask == value.ask) and (self.time==value.time)




t1 = Tick(1.080, 1.081, "2026-10-01")
t2= Tick(1.080, 1.081, "2026-10-01")

assert t1 == t2


consistency_check = {}


print (t1.__hash__)

