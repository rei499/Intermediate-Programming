print("=== MOVIE TICKET SYSTEM ===")

 = input("Day (weekday/weekend): ").lower()
customer = input("Customer type (regular/student/senior): ").lower()
sched = int(input("Show time (9 - 22): "))
if sched < 9 or sched > 22:
    print("Invalid show time. Please enter a time between 9 and 22.")
    exit()
no_of_ticket = int(input("Number of tickets: "))
if no_of_ticket < 1:
    print("Invalid number of tickets.")
    exit()

acknowledgement = "Thank you for your purchase!"

print("\n--- RECEIPT ---")

#Base Price
if day == "weekday":
    base = 200.00
    base_price = base * no_of_ticket
else:
    base = 300.00
    base_price = base * no_of_ticket

#Customer-type Discounts
student_discount = base_price / 5
senior_discount = base_price / 10
    
if customer == "student":
    print(f"Base price: {base} x {no_of_ticket} = {base_price}")
    print(f"Student discount (20%): -{student_discount}")
    student_price = base_price - student_discount
    if sched < 12:
        matinee_discount = base_price / 10
        print(f"Matinee discount (10%): -{matinee_discount}")
        stumat_price = student_price - matinee_discount
        if no_of_ticket >= 5:
            group_discount = stumat_price / 5
            print(f"Group discount (5%): -{group_discount}")
            final_price = base_price - group_discount
            print(f"\nTOTAL: {final_price}")
            print(acknowledgement)
        else:
            print(f"\nTOTAL: {stumat_price}")
            print(acknowledgement)
    elif no_of_ticket >= 5:
        group_discount = student_price / 5
        print(f"Group discount (5%): -{group_discount}")
        final_price = student_price - group_discount
        print(f"\nTOTAL: {final_price}")
        print(acknowledgement)
    else:
        print(f"\nTOTAL: {student_price}")
        print(acknowledgement)

elif customer == "senior":
    print(f"Base price: {base} x {no_of_ticket} = {base_price}")
    print(f"Senior discount (10%): -{senior_discount}")
    senior_price = base_price - senior_discount
    if sched < 12:
        matinee_discount = senior_price / 10
        print(f"Matinee discount (10%): -{matinee_discount}")
        senmat_price = senior_price - matinee_discount
        if no_of_ticket >= 5:
            group_discount = senmat_price / 5
            print(f"Group discount (5%): -{group_discount}")
            final_price = senmat_price - group_discount
            print(f"\nTOTAL: {final_price}")
            print(acknowledgement)
        else:
            print(f"\nTOTAL: {senmat_price}")
            print(acknowledgement)
    elif no_of_ticket >= 5:
        group_discount = senior_price / 5
        print(f"Group discount (5%): -{group_discount}")
        final_price = senior_price - group_discount
        print(f"\nTOTAL: {final_price}")   
        print(acknowledgement) 
    else:
        print(f"\nTOTAL: {senior_price}")
        print(acknowledgement)
    
elif customer == "regular":
    print(f"Base price: {base} x {no_of_ticket} = {base_price}")
    if sched < 12:
        matinee_discount = base_price / 10
        print(f"Matinee discount (10%): -{matinee_discount}")
        regmat_price = base_price - matinee_discount
        if no_of_ticket >= 5:
            group_discount = regmat_price / 5
            print(f"Group discount (5%): -{group_discount}")
            final_price = regmat_price - group_discount
            print(f"\nTOTAL: {final_price}")
            print(acknowledgement)
        else:
            print(f"\nTOTAL: {regmat_price}")
            print(acknowledgement)
    elif no_of_ticket >= 5:
        group_discount = base_price / 5
        print(f"Group discount (5%): -{group_discount}")
        final_price = base_price - group_discount
        print(f"\nTOTAL: {final_price}")
        print(acknowledgement)
    else:
        print(f"\nTOTAL: {base_price}")
        print(acknowledgement)

else:
    print("Invalid customer type.")