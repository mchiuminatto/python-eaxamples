# LOOPING TECHNIQUES OVER DATA STRUCTURES

# looping over a dictionary we can retrieve at the same time the key and the value using item method
risk = dict(EURUSD=10, AUDUSD=12, GBPUSD=15, USDCAD=9, USDJPY=10)
for k, v in risk.items():
    print(k, v)

# looping over sequences we can retrieve the index and the value at the same time using enumerate method
print("\n")
instruments = ["EURUSD", "USDCAD", "AUDUSD", "USDJPY"]
for k, v in enumerate(risk):
    print(k, v)

# pairing two sets with zip()

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print("What is your {0}? It is {1}".format(q, a))

# loop over a sequence in reverse order, specify the sequene in forward direction,
# then reverse
for i in reversed(range(1, 10, 2)):
    print(i)

# loop over a sorted order, use the sort function which returns a new sorted copy
# leaving the original list intact

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for v in sorted(basket):
    print(v)

