"""
Each objes has its identity
A variable name is a label on that identity, so assignment never copies an object by default
"""

ticks =  [1.0841, 1.0843, 1.0840]
print(f"`ticks` is the first label on {id(ticks)}, -> {ticks}")
window = ticks
print(f"`window` is the second label on {id(window)}, -> {window}")
assert id(ticks) == id(window)

other = [1.0841, 1.0843, 1.0840, 1.0845]
print (f"other has the same values that ticks but is a different object ticks {id(ticks)} != {id(other)}")

# Rebinding moves the label but does not touch the object
print("")
print("------- rebinding -------")
print (f"Before rebinding {id(window)}")
window = window + [1.0850]  # builds a new list rthen rebinds `window'
print (f"After rebinding {id(window)}")

# The operator += does not rebinds, just extends
print("")
print("------- Extending -------")
print (f"Before extending {id(window)}")
window += [1.0850]
print (f"After extending {id(window)}")


# Extending with append
print("")
print("------- Extending with append-------")
print (f"Before extending {id(window)}")
window.append(1.0850)
print (f"After extending {id(window)}")


