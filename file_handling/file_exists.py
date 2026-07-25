from pathlib import Path

file_path = Path("sample.txt")

if file_path.exists():
    print("File exists")
else:
    print("File not found")