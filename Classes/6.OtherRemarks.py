# OTHER REMARKS

# A class can use ecternally defined functions


def f1(self, x, y):
    return min(x, x+y)


class C:
    f = f1;

    def g(self):
        return "hello world"

    h = g

x = C()
print(x.f(1, 2))
print(x.g())
print(x.h())


# methods calling other class's methods


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

b = Bag()
print(b.data)
b.addtwice(2)
print(b.data)

