username = "Sandy_P"
password = "BSITSE1A"

name_attempt = input("Enter your username: ")


if name_attempt == username:
    pass_attempt = input("Enter your password: ")
    if pass_attempt == password:
        print("Welcome! Login successful.")
    else:
        print("Incorrect password.")
else:
    print("User not found.")
