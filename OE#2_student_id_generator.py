# Part A - Collect Student Information
full_name = input("Enter your full name: ")
full_name = full_name.split()
if len(full_name) < 2:
    print("Error: Please enter at least a first and last name.")
else:
    course_code = input("Enter your course code (e.g., CS101): ")
    # if course_code == "" 