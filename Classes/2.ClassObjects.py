# When a class is created a new namespace is created and used as local scope
# When a normal class definition is created, a new CLASS OBJECT is created.

# CLASS OBJECTS
# Supports two kind of operations:
#   attribute reference
#   instantiation


class MyClass:
    """ A simple example of class"""
    i = 12345

    def f(self):
        return "hello world"

print("MyClass class object after class creation")
print("")
print("MyClass.i ", MyClass.i)
print("MyClass.f ", MyClass.f)  # returns a function object, that points to a class function
print("MyClass.__doc__ ",MyClass.__doc__)
print("")
print("Creating an object x of MyClass")
x = MyClass()
print("x.i ", x.i)
print("x.f ", x.f)
print("x.f() ", x.f())
print("x.__doc__ ", x.__doc__)


class Complex:
    def __init__(self, realpart, imagpart):  # in the init method you create all instance data attributes
        self.r = realpart
        self.i = imagpart
print()
print("Complex class with init method")
y = Complex(3.0, -4.5)
print(" r, i ", y.r, y.i)



