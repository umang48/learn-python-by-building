cart = []

while True:
    item = input("Add item (or 'done'): ")

    if item.lower() == "done":
        break

    cart.append(item)

print("Shopping Cart:")
for item in cart:
    print("-", item)