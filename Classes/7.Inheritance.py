# INHERITANCE

# a class can inherit from the same scope and from {
# other scope

import random


class Position:

    def __init__(self, sl, tp, price, direction):
        self.sl = sl
        self.tp = tp
        self.price = price
        self.direction = direction
        self.pos_id =0

    def __open(self, sl, tp, price, direction):
        print("position " + self.direction + " opened at " + str(self.price))
        self.pos_id = random.randint(0, 10000)

    def __close(self):
        print("position " + str(self.pos_id) + " closed")

    def trail(self, pips):
        return pips


class SMATrail(Position):

    def __init__(self, sl, tp, price, direction):
        super().__init__(sl, tp, price, direction)

    def __open(self):  # this method extends the Base Class's
        print("Calling base class method")
        Position.__open(self, self.sl, self.tp, self.price, self.direction)

    def close(self):  # this method replaces the base class's
        print("SMA Trail position " + str(self.pos_id) + " is now closed")


newPos = SMATrail(10, 20, 101.4, "buy")
newPos.open()
newPos1 = SMATrail(20, 40, 102, "sell")
newPos1.open()
newPos1.close()
newPos.close()


print(isinstance(newPos, SMATrail))
print(isinstance(newPos, Position))
print(issubclass(SMATrail, Position))



