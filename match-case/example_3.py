lunch_order = input("What would you like for lunch? ")

match lunch_order:
# --snip--
    case 'salad' | 'soup':  # list of accepted values for this option
        print('Eating healthy, eh?')
    case order:  # fall back but captures the value
        print(f"Enjoy your {order}.")

