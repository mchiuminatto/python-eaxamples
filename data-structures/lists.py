fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print("banana", fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting a position 4

fruits.reverse()
print(fruits)
fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())
print(fruits)

prices = [100, 3,5,89,6, 5, 6]
print("max", max(prices))

price2 = prices.copy()
print("price 2", price2)
prices[3] = 15
print("price 2", price2)
price2[3] = 15
print("price 2", price2)

# using del statement
del price2[0]
print("price 2", price2)
del price2[1:4]
print("price 2", price2)




