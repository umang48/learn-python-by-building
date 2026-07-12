def student(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


student(name="Umang", age=25, city="Ahmedabad")