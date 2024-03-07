while True:
        try:
            x = int(input("Please enter a valid number "))

        except ValueError:
            print("Oops! That was not a valid number. Try again")
        except KeyboardInterrupt:
            print("This is the end")
            break
# if no exception matches the exception clauses, then execution
# continues on an outer try if exists. If it isn't, then it is
# an unhandled exception
