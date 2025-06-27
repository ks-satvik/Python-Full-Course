# -------------------------------
# VARIABLES AND DATA TYPES IN PYTHON
# -------------------------------

# Python uses dynamic typing, meaning you don’t need to declare a variable type

# -------------------------------
# 1. VARIABLE ASSIGNMENT
# -------------------------------

x = 5               # Integer
y = 3.14            # Float
name = "Satvik"     # String
is_student = True   # Boolean

# Multiple assignment
a, b, c = 1, 2, 3
m = n = 10  # Same value to multiple variables

# -------------------------------
# 2. BASIC DATA TYPES
# -------------------------------

# Integer
age = 21

# Float
price = 19.99

# String
greeting = "Hello, Python!"

# Boolean
is_sunny = False

# NoneType
nothing = None

# -------------------------------
# 3. TYPE CHECKING & TYPE CASTING
# -------------------------------

print(type(age))        # <class 'int'>
print(type(price))      # <class 'float'>
print(type(greeting))   # <class 'str'>
print(type(is_sunny))   # <class 'bool'>
print(type(nothing))    # <class 'NoneType'>

# Type Casting
str_num = str(100)          # Converts int to string
int_str = int("50")         # Converts string to int
float_str = float("4.5")    # Converts string to float
bool_val = bool(0)          # Converts int to boolean (0 -> False)

# -------------------------------
# 4. ADVANCED DATA TYPES
# -------------------------------

# List - ordered, mutable, allows duplicates
my_list = [1, 2, 3, "hello", True]

# Tuple - ordered, immutable
my_tuple = (10, 20, 30)

# Set - unordered, no duplicates
my_set = {1, 2, 3, 3, 2}

# Dictionary - key-value pairs
my_dict = {
    "name": "Satvik",
    "age": 20,
    "student": True
}

# -------------------------------
# 5. VARIABLE NAMING RULES
# -------------------------------
# - Must begin with a letter or underscore (_)
# - Cannot start with a number
# - Can only contain alphanumeric characters and underscores
# - Case-sensitive: myVar and myvar are different

# Valid examples:
student_name = "Alice"
_age = 22
pi_value = 3.1415

# Invalid examples (will throw errors if uncommented):
# 2cool = "no"      # Starts with number
# my-name = "bad"   # Hyphens not allowed

# -------------------------------
# 6. BEST PRACTICES
# -------------------------------
# - Use lowercase with underscores for variable names (snake_case)
# - Choose descriptive names (e.g., total_price instead of tp)
# - Avoid using Python keywords (like list, int, str) as variable names

# Example of good naming:
total_price = 299.99
customer_age = 30
is_valid_user = True

# -------------------------------
# END OF FILE
# -------------------------------

