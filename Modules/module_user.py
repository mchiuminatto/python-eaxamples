# USING MODULES

import sys
from Fibonacci import fibo         # import fibo module from fibonacci
from Fibonacci import fibo_ratios  # import fibo_ratio from fibonacci
# from Fibonacci import *  # this is an alternative way to import when __all__ is defined on __init__.py

# imported modules names are placed on this module global symbol table

fibo.fib2(10)  # this is the way to invoke a function within a module

numLst = fibo.fib2(10)
print(numLst)

fib = fibo.fib  # we can assign function names to variables
fib(1000)


golden = fibo_ratios.calc_fibo_ratio

print("golden ratio", golden(100), sep=":")

print(__name__)

print(sys.path)  # the imported names search path.

print("this module names", dir())  # dir without arguments shows this  module name
print()
print("fibo module names", dir(fibo))  # dir with moduke name shows all the names thet the module defines

print()
import builtins
print("built in names", dir(builtins))  # show built in names (functions, variables, etc...)
