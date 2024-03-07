# DICTIONARIES
# a dictionary is a set of key:value pairs

TFMin = {}  # creates an empty dictionary
print(TFMin)
TFMin = {"m1": 1, "m5": 5, "m15": 15}  # creates a dictionary with elements
print(TFMin["m1"])

del TFMin["m1"]  # deletes m1"
print(TFMin)

print(list(TFMin.keys()))  # list the dictionary keys
print(sorted(TFMin.keys()))  # list the keys sorted

print("m15" in TFMin)  # check if the key is in the dictionary

# alternatives to create dictionaries
risk = dict([("EURUSD", 10), ("USDJPY", 8), ("AUDUSD", 9)])
print(risk)

# with keywords
pipCost = dict(EURUSD=10, GBPUSD=10, USDJPY=9, EURGBP=12)
print(pipCost)


