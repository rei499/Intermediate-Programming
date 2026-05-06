print("\n===BOOTH BILLING===\n")

booth_name = "TECH HAVEN"
menu = [
    [1, "Phone Stand", 30],
    [2, "USB Cable", 25],
    [3, "Screen Wiper", 15],
    [4, "Earbuds", 45],
    [5, "Webcam Cover", 20],
]

cashier_name = input("Enter cashier name: ")
customer_name = input("Enter customer name: ")
print("\nNOTE: You have THREE slots. Enter 0 to skip.")
print("","_" * 68)
print(f"|{'':>10}{'#':<11}|{'Item':<20}|{'':>10}{'Price':<15}|")
print("","-" * 68)
print(f"|{'':>10}{'1':<11}|{'Phone Stand':<20}|{'':>9}{'₱ 30.00':<16}|")
print(f"|{'':>10}{'2':<11}|{'USB Cable':<20}|{'':>9}{'₱ 25.00':<16}|")
print(f"|{'':>10}{'3':<11}|{'Screen Wiper':<20}|{'':>9}{'₱ 15.00':<16}|")
print(f"|{'':>10}{'4':<11}|{'Earbuds':<20}|{'':>9}{'₱ 45.00':<16}|")
print(f"|{'':>10}{'5':<11}|{'Webcam Cover':<20}|{'':>9}{'₱ 20.00':<16}|")
print("","-" * 68)

total_price = 0.0
purchased_items = []

while True:
    purchased_items = []
    total_price = 0.0
    for selection in range (3):
        order = int(input("Enter item number: "))
        
        if order >= 1 and order <= 5:
            quantity = int(input("Quantity: "))
            print(f"Order: Item {order} ({menu[order - 1][1]}), qty {quantity}")
            subtotal = float(menu[order - 1][2] * quantity)
            purchased_items.append((menu[order - 1][1], quantity, subtotal))
            total_price += subtotal
            print(f"Subtotal: ₱ {subtotal}")
            print(f"TOTAL: ₱ {total_price}\n")


        elif order == 0:
            print("Slot skipped. No item added.\n")
            continue

        else:
            print("Invalid number! Please enter 1-5 or 0 to skip.\n")
            break

    again = input("Would you like to try again? (y/n): ").lower()
    if again == "y":
        continue
    elif again == "n":
        break
    else:
        print("Invalid input.")
        again = input("Would you like to try again? (y/n): ").lower()

discount_text = "None"
final_total = total_price

if total_price >= 100:
    discount_amount = total_price / 10
    final_total = total_price - discount_amount
    discount_text = "10% (Techie Discount)"
    print(f"\nAvailable discount: {discount_text}")

print(f"TOTAL PRICE: ₱ {final_total}\n")
payment = float(input("Enter amount received: ₱ "))
change = payment - final_total

if payment < final_total:
    print(f"Payment is still short of ₱ {final_total - payment}")

print(f"\n{'='*22} RECEIPT {'='*22}")
print(f"|{'Booth Name: ':<11}{booth_name:<39}|")
print(f"|{'Cashier: ':<9}{cashier_name:<42}|")
print(f"|{'Customer: ':<10}{customer_name:<41}|")
print(f"{'-'*53}")

for purchase, item in enumerate(purchased_items):
    name, qty, sub = item
    print(f"|Order {purchase+1}: {name:<13}|Qty: {qty:<4}|Subtotal: ₱{sub:<7}|")

print(f"{'-'*53}")
print(f"|{'Subtotal: ₱':<11}{total_price:<40}|")
print(f"|{'Discount: ':<11}{discount_text:<40}|")
print(f"|{'TOTAL: ₱':<8}{final_total:<43}|")
print(f"|{'Paid: ₱':<7}{payment:<44}|")
print(f"|{'Change: ₱':<9}{change:<42}|")
print(f"{'='*53}")
