name = input("Enter your full name: ")
name_part = name.split()
name_labels = ["first name ", "middle name ", "last name "]

for label, word in zip(name_labels, name_part):
    clean = word.strip()
    length = len(word)

    middle = word[(length - 1) // 2 : length // 2 + 1]
    print(f"The middle character/s of your {label}{word}: {middle}")