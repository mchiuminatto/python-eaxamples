# ODDS AND ENDS

# using empty classes as data structures

# alternative 1 - predefining the structure


class Employee():
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.phone=""

e1 = Employee()

e1.name = "Marcello"
e1.last_name = "Chiuminatto"
e1.phone = "77574559"

print(e1.name + " " + e1.last_name + " " + e1.phone)

# second alternative, empty class


class Employee1():
    pass

me = Employee1()

me.name = "Marcello"
me.last_name = "Chiuminatto"
me.phone = "77574559"


print(me.name + " " + me.last_name + " " + me.phone)


