# CLASS AND INSTANCE VARIABLES


class Dog:
    # put here the class variables
    kind = "canine"

    def __init__(self, name):
        # place here the instance variables
        self.name = name

d = Dog("Fido")
e = Dog("Buddy")

print("e.kind", e.kind)
print("d.kind", d.kind)
print("d.name", d.name)
print("e.name", e.name)


class Dog1:
    kind = "canine"
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d1 = Dog1("Bobby")
e1 = Dog1("Pillin")
# this trick will be added for canines not just for Bobby
# because is a class variable
d1.add_trick("Jump")
print(d1.name, d1.kind, d1.tricks)
print(e1.name, e1.kind, e1.tricks)

# class with trick list fixed


class Dog2:
    kind = "canine"

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

print()
d2 = Dog2("Bobby")
e2 = Dog2("Pillin")
# this trick will be added only for bobby
# because is a class variable
d2.add_trick("Jump")
print(d2.name, d2.kind, d2.tricks)
print(e2.name, e2.kind, e2.tricks)
