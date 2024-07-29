# Iterator Example (Using Class)
class Count:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            num = self.current
            self.current += 1
            return num
        


# Using the Iterator
itr = Count(1, 3)
for num in itr:
    print(num)


next(itr)