try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")