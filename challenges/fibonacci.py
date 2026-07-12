terms = int(input("Enter number of terms: "))

first = 0
second = 1

print("Fibonacci Series:")

for _ in range(terms):
    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number