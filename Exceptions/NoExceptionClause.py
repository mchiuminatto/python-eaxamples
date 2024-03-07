# using exception clause with no exception

while True:
    try:
        x = int(input("Please enter a number"))
        b = 4/x
        if b < 1:
            raise Warning
    except KeyboardInterrupt:
        print("This is the end")
        break
    except ZeroDivisionError:
        print("Division by zero tried")
    except ValueError:
        print("Wrong data type")
    except:
        print("Something else has happened")
        raise
    
# an except clause with no exception may be used
# but carefully
