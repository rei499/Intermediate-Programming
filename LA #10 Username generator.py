print("===USERNAME GENERATOR===")

name = input("Enter your full name: ").lower()
birth_year = input("Enter your birth year: ")
full_name = name.split()
if len(full_name) < 2:
    print("Error: Please enter at least a first and last name.")
else:
    first_name = full_name[0]
    last_name = full_name[-1]
    first_name.split()
    last_name.split()
    birth_year.split()
    username = first_name[0:3] + last_name[0:3] + birth_year[-2:]
    print(f"Generated username: {username}")
