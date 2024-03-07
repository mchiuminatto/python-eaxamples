# use of exception instances and its associated values

try:
    raise Exception("spam", "eggs")
except Exception as inst:  # inst is the container of the exception
    print(type(inst))
    print(inst.args)       # prints the arguments stored in args
    print(inst)            # __str__ allows args to be printed directly,
                           # but may be overriden in exception subclass
    x, y = inst.args       # upack args
    print("x = ", x)
    print("y = ", y)

# in unhandled exceptions, arguments are printed as last part detail on exception messages

try:
    raise Exception("spam", "eggs")
except ValueError:
    print("Invalid value")
