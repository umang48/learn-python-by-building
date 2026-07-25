import csv

rows = [
    ["Name", "Age"],
    ["Umang", 30],
    ["Rahul", 25]
]

with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("CSV created")