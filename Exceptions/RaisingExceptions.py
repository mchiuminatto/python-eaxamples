# Raising exceptions
# raise <exception class | instance>(arguments)

try:
    raise NameError("Ho there")
except NameError:
    print("An exception flew by!!")
    raise  # re-rise exception in order to delegate is handling






