try:
    file = open("sample.txt")

except FileNotFoundError:
    print("File not found")

finally:
    print("Execution completed")