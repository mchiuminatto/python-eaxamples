def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Division bty zero")
    else:
        print("The result is ", result)
    finally:
        print("executing finally clause")

divide(1,2)
divide(1,0)

# predefinde clean up actions

#with open("myfile.txt", "w") as f:
#    f.write("header1, header2")
# f.write("end")
