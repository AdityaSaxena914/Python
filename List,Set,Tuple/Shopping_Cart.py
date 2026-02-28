cart = []
total = 0

print("----- Welcome to shopping cart-----\n")
print("Press E to add food item in cart")
print("Press Q to quit\n")
while True:
    choice = input("Type here: ").lower()
    if choice == "e":
        food = (input("Enter food item: "))
        price = float((input("Enter food price: $")))
        cart.append(f"{food}: ${price}")
        total += price
        print()
    elif choice == "q":
        if len(food) != 0:
            print("----- Cart -----")
            for x in cart:
                print(x)
        else:
            print("Your cart is empty!!")
        print(f"Total: {total}")
        print("\nThanks for choosing us...")
        break
    else:
        print("Press E or Q")