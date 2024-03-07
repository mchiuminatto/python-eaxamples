# use of else clause
# it is recommended to use when it is needed
# to add code after try, but it isn't relevant
# it is not relevant to be protected by a try
# exception clause

myList = [ "u", 1,2,3,4,5,6]
acc = 0
count = 0
mva = 0
for num in myList:
    try:
        acc = acc + int(num)
    except ValueError:
        print("Invalid number")
    else:
        count = count + 1
        mva = acc/count

print("MVA :" + str(mva))