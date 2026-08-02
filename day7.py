import json

# Read JSON file
with open("data.json", "r") as file:
    data = json.load(file)

students = data["students"]

cleaned_students = []
ids = []

for student in students:

    # Remove duplicate IDs
    if student["id"] in ids:
        continue

    ids.append(student["id"])

    # Clean Name
    if student["name"] is not None:
        student["name"] = student["name"].strip().title()

    # Clean Branch
    if student["branch"] is not None:
        student["branch"] = student["branch"].strip().upper()

    # Clean Email
    if student["email"] is not None:
        student["email"] = student["email"].strip().lower()

    # Handle missing Age
    if student["age"] == "" or student["age"] is None:
        student["age"] = None

    # Handle missing CGPA
    if student["cgpa"] == "" or student["cgpa"] is None:
        student["cgpa"] = None

    cleaned_students.append(student)
    ids.append(student["id"])

# Print cleaned data
for student in cleaned_students:
    print(student)

# Save cleaned data
with open("cleaned_data.json", "w") as file:
    json.dump({"students": cleaned_students}, file, indent=4)

print("Data cleaned successfully.")