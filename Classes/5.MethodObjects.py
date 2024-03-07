# METHOD OBJECTS

# a method object is an abstract object that packages
# together an instance object and a function object
# that belongs to it before to be executed


class MyClass:
    """ A simple example of class"""
    i = 12345

    def f(self):
        return "hello world"


x = MyClass()
print("x,f()")
print(x.f())

# storing a method object (a function can be assigned)
xf = x.f;
print()
print("print(xf)")
print(xf)
print()
print("xf()")
print(xf())
print()
print("MyClass.f(x)")
print(MyClass.f(x))

