import json

data = {
    "name": "Umang",
    "city": "Ahmedabad",
    "skills": ["Python", "PHP", "WordPress"]
}

with open("user.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON created")