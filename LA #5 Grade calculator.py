score = int(input("Enter your score (0-100): "))

if score >= 60 and score <= 100:
    if score < 65:
        print(f"Score: {score} → Grade: D- - Needs Improvement")
    elif score < 70:
        print(f"Score: {score} → Grade: D+ - Pass")
    elif score < 75:
        print(f"Score: {score} → Grade: C- - Fair")
    elif score < 80:
        print(f"Score: {score} → Grade: C+ - Good")
    elif score < 85:
        print(f"Score: {score} → Grade: B- - Very Good")
    elif score < 90:
        print(f"Score: {score} → Grade: B+ - Satisfactory")
    elif score < 95:
        print(f"Score: {score} → Grade: A- - Very Satisfactory")
    else:
        print(f"Score: {score} → Grade: A+ - Outstanding")
else:
    print(f"Score: {score} → Failed")
