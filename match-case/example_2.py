while True:
    command_number = int(input("enter command :"))

    match command_number:
        case 1:
            print("Files commans")
        case 2:
            print("Dir command")
        case 3:
            print("Bye")
            exit(0)
