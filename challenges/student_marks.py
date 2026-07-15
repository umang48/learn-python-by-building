students = {
    "Rahul": 90,
    "Priya": 95,
    "Amit": 82
}

highest = max(students, key=students.get)

print(highest, students[highest])