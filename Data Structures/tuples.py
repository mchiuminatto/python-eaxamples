# using tuples

t1 = "EUR", "USD", "CAD"
print(t1)
t2 = "GBP", "AUD", "NZD"
print(t2)
instruments = []
for i in t1:
    for j in t2:
        instruments.append(i +"/"+ j)
print(instruments)
t = ("USDOLLAR", ), *instruments
print(t)
