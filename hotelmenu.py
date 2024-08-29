# Define the menu of the restaurant
menu = {
    'pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80
}

# Greet 
print("Welcome To Python Restaurant")
print("Menu:")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

# Initialize order total
order_total = 0

# Take the first order
item_1 = input("Enter the name of the item you want to order: ")

# Check if the item is in the menu
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available yet!")

# Ask for another order
another_order = input("Do you want to add another item? (Yes/No): ").lower()

# If the customer wants to order another item
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available.")

# Display the total amount
print(f"The total amount for your order is Rs{order_total}.")

