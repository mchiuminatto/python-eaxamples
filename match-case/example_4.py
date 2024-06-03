lunch_order = input("What would you like for lunch? ")

if ' ' in lunch_order:
    lunch_order = lunch_order.split(maxsplit=1)

print("Order captured", lunch_order)

match lunch_order:
    case (flavor, 'ice cream'):  # this tuple pass the value matched to flavor variable
        print(f"Here's your very grown-up {flavor}...lunch.")
# --snip--