a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Largest number is:", largest)