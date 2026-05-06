print("===RECEIPT GENERATOR===")
item_name = input("Enter the item name: ")
quantity = int(input("Enter the quantity: "))
unit_price = float(input("Enter the unit price: "))
price = quantity * unit_price

print("\n--- RECEIPT ---")
print(f"|{'Item':<15}|{'Qty':>5}|{'Price':>15}|")
print(f"|{item_name:<15}|{quantity:>5}|{unit_price:>15,.2f}|")
print(f"|{'-'*37}|")
print(f"|{'Total Price:':<13}₱{price:<23,.2f}|")
