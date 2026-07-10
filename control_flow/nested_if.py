age = int(input("Enter age: "))
citizen = input("Are you an Indian citizen? (yes/no): ")

if age >= 18:
    if citizen.lower() == "yes":
        print("Eligible to vote")
    else:
        print("Citizenship required")
else:
    print("Not eligible")