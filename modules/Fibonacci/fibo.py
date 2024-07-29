# USING MODULES
# modules are files containing python definitions and statements
# can be imported from other modules

# module statements are executed when the module is imported
# so they are used to initialize the module

# each module has its own symbol table, which is defined as global
# symbol table by all its functions, so module global variables
# won't clash with other module's

print("Name is", __name__)  # the module name


def fib(n):  # write fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b
        print()


def fib2(n):  # return fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result





