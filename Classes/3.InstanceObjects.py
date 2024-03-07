# INSTANCE OBJECTS

# Instance objects understand only one kind of operation:
# attribute reference.
# There are two kinds of references that can be done:
#   * Data attribute reference
#   * Method attribute reference


class MyClass:
    """ A simple example of class"""
    i = 12345

    def f(self):
        return "hello world"

# creates the instance object x
x = MyClass()

# adds tha data attribute counter to the instance object
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2;
# prints the instance object's attribute counter
print(x.counter)

print(dir(x))
# delete the instance object's attribute
del x.counter
print(dir(x))

