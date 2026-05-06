print("\n===Student Expense Tracker===\n")

student_name = input("Enter your name: ")
weekly_budget = int(input("Enter your weekly budget: "))

print(student_name)
print(weekly_budget)

while True:
    print("","_" * 65)
    print(f"|  #  | {'Category':<20} | {'Example Expenses':<34} |")
    print("","-" * 65)
    print(f"|  1  | {'Food & Drinks':<20} | {'e.g. Lunch, snacks, coffee':<34} |")
    print(f"|  2  | {'Transportation':<20} | {'e.g. Bus, jeepney, ride-share':<34} |")
    print(f"|  3  | {'Mobile / Internet':<20} | {'e.g. Load, data plan, WiFi, top-up':<34} |")
    print(f"|  4  | {'School Supplies':<20} | {'e.g. Notebook, pen, bond paper':<34} |")
    print(f"|  5  | {'Entertainment':<20} | {'e.g. Games, movies, hangout':<34} |")
    print("","-" * 65)


