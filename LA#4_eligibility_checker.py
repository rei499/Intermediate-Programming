age = int(input("What is your age? "))
valid_id = input("Do you have a valid ID? (yes/no): ").upper()

if valid_id == "YES":
    valid_id = True
elif valid_id == "NO":
    valid_id = False
else:
    print("Invalid input.")

if age >= 18 and valid_id == True:
    print("Eligible!")
    if age >= 60:
        print("Senior discount applied!")
else:
    print("Not eligible")