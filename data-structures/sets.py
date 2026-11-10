# USING SETS

mySet = set()  # empty set
set1 = {}  # this creates a dictionary not a set

mySet1 = {1, 2, 7,  3, 4, 5, 2, 3}
print(mySet1)  # note that set eliminates duplicates and sort ascending the elements

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print("orange" in basket)  # with in we test element membership
print("plumcot" in basket)

a = set("abracadabra")  # creates the set and each element is a letter
b = set ("alacazam")

print(a)
print(b)
print("difference", a - b)  # removes from a all that is in b (set difference operation)
print("union", a | b)  # union: all that is in a or b
print("intersection", a & b)  # intersection: letters that ar in both a and b
print("exclusive union", a ^ b)  # letters that are in a or be but not in both (exclusive union)

# set comprehensions are also supported
a = {x for x in "abracadabra" if x not in "abc"}


