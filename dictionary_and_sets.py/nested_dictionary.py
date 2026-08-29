# Simple nested dictionary
student = {
    "name": "John",  # Outer dictionary key-value pair
    "age": 20,  # Student age
    "courses": {  # Inner dictionary (nested)
        "math": 95,  # Math course and score
        "science": 88  # Science course and score
    }
}

# Accessing nested dictionary values
print(student["name"])  # We ask the student dictionary "What is the name?" and it tells us "John"
print(student["courses"]["math"])  # We ask the student dictionary "Show me the courses", then ask "What is the math score?" and it tells us "95"
