phone_book = {
    "Alice": "9876543210",
    "Bob": "9123456789"
}

name = input("Enter name: ")

print(phone_book.get(name, "Contact not found"))