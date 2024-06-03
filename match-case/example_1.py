while True:
    command_string = input("enter command :")

    match command_string.lower():
        case "files":
            print("Files commans")
        case "dir":
            print("Dir command")
        case "exit":
            print("Bye")
            exit(0)
        case _:
	        print("Unknown command, try again")
