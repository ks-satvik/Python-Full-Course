# ======================================================
# DICTIONARIES IN PYTHON - COMPLETE GUIDE
# ======================================================

# ------------------------------------------------------
# 1. DICTIONARY BASICS - KEY-VALUE PAIRS
# ------------------------------------------------------

# A dictionary is an unordered, mutable collection of key-value pairs.
# Keys must be unique and immutable (e.g., strings, numbers, tuples).
# Values can be any data type (including lists, other dicts, etc.).

# Creating dictionaries
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}

print("Dictionary:", person)

# Accessing values using keys
print("Name:", person["name"])
print("Age:", person["age"])

# Safe access using get()
print("Student?", person.get("is_student"))      # True
print("Gender?", person.get("gender", "Not found"))  # Returns default if not found

# ------------------------------------------------------
# 2. DICTIONARY OPERATIONS
# ------------------------------------------------------

# ADD / UPDATE
person["age"] = 26                      # Update existing
person["gender"] = "Female"            # Add new key-value pair
print("After update/add:", person)

# DELETE
del person["is_student"]               # Delete key-value pair
print("After deletion:", person)

# pop() - remove key and return value
removed = person.pop("gender")
print("Removed 'gender':", removed)

# popitem() - removes last inserted pair (Python 3.7+)
last_item = person.popitem()
print("Last item removed:", last_item)

# clear() - removes all items
temp = {"a": 1, "b": 2}
temp.clear()
print("Cleared dictionary:", temp)

# ------------------------------------------------------
# 3. DICTIONARY ITERATION
# ------------------------------------------------------

user = {"name": "Bob", "age": 30, "city": "NY"}

# Keys only
for key in user:
    print("Key:", key)

# Values only
for value in user.values():
    print("Value:", value)

# Both keys and values
for key, value in user.items():
    print(f"{key} → {value}")

# ------------------------------------------------------
# 4. CHECKING EXISTENCE
# ------------------------------------------------------

print("'name' in user?", 'name' in user)      # True
print("'email' not in user?", 'email' not in user)  # True

# ------------------------------------------------------
# 5. DICTIONARY METHODS
# ------------------------------------------------------

data = {"x": 1, "y": 2, "z": 3}

# keys(), values(), items()
print("Keys:", list(data.keys()))
print("Values:", list(data.values()))
print("Items:", list(data.items()))

# copy() - shallow copy
copy_data = data.copy()
print("Copy:", copy_data)

# fromkeys() - creates new dictionary from keys
new_dict = dict.fromkeys(["a", "b", "c"], 0)
print("From keys:", new_dict)

# setdefault() - returns value if key exists, else sets it
val = data.setdefault("x", 100)
print("Set default (existing):", val)

val2 = data.setdefault("w", 42)
print("Set default (new):", val2)
print("Updated dict:", data)

# update() - merges dictionaries
other = {"a": 100, "b": 200}
data.update(other)
print("After update:", data)

# ------------------------------------------------------
# 6. NESTED DICTIONARIES
# ------------------------------------------------------

student = {
    "name": "John",
    "marks": {
        "math": 90,
        "science": 85
    }
}

print("Math Marks:", student["marks"]["math"])

# Iterating nested
for subject, score in student["marks"].items():
    print(f"{subject} → {score}")

# ------------------------------------------------------
# 7. DICTIONARY COMPREHENSIONS
# ------------------------------------------------------
squares = {x: x*x for x in range(1, 6)}
print("Squares dict:", squares)
# Filtering comprehension
even_squares = {x: x*x for x in range(10) if x % 2 == 0}
print("Even squares dict:", even_squares)

# ------------------------------------------------------
# 8. USE CASES OF DICTIONARIES
# ------------------------------------------------------

# ✅ Storing user information
user_profile = {
    "username": "satvik",
    "followers": 128,
    "verified": True
}

# ✅ Word frequency count
text = "hello world hello python"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print("Word count:", word_count)

# ✅ Creating lookups or mappings
country_codes = {
    "IN": "India",
    "US": "United States",
    "JP": "Japan"
}
print("Country code lookup:", country_codes["IN"])

# ✅ Representing structured data
product = {
    "id": 101,
    "name": "Laptop",
    "price": 49999,
    "specs": {
        "ram": "8GB",
        "storage": "512GB SSD"
    }
}
print("Laptop RAM:", product["specs"]["ram"])

# ------------------------------------------------------
# END OF FILE
# ------------------------------------------------------