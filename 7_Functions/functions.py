# ======================================================
# FUNCTIONS IN PYTHON - COMPREHENSIVE NOTES
# ======================================================

# ------------------------------------------------------
# 1. DEFINITION AND PURPOSE
# ------------------------------------------------------

# Functions are reusable blocks of code that perform a specific task.
# They improve code modularity, reusability, readability, and maintainability.

# Syntax:
# def function_name(parameters):
#     """optional docstring"""
#     code block

def greet():
    """This function prints a greeting."""
    print("Hello, welcome to Python!")

greet()  # Calling the function

# ------------------------------------------------------
# 2. FUNCTION DECLARATION: PARAMETERS & RETURN VALUES
# ------------------------------------------------------

# 2.1 Parameters and Arguments

def add(a, b):  # a and b are parameters
    return a + b

result = add(5, 3)  # 5 and 3 are arguments
print("Addition:", result)

# 2.2 Default Parameters

def power(base, exponent=2):
    return base ** exponent

print("Power with default:", power(5))
print("Power with custom exponent:", power(2, 3))

# 2.3 Keyword Arguments

def describe(name, age):
    print(f"{name} is {age} years old")

describe(age=22, name="Satvik")  # Order doesn't matter with keyword args

# 2.4 Variable-length Arguments

# *args - Tuple of positional arguments
def total_sum(*args):
    return sum(args)

print("Sum of values:", total_sum(1, 2, 3, 4))

# **kwargs - Dictionary of keyword arguments
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Kumar", course="Python", year=2025)

# ------------------------------------------------------
# 3. RETURNING MULTIPLE VALUES
# ------------------------------------------------------

def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 5, 1, 9, 7])
print("Min:", low, "Max:", high)

# ------------------------------------------------------
# 4. SCOPE AND LIFETIME OF VARIABLES
# ------------------------------------------------------

# Global Scope
x = 10  # Global variable

def print_global():
    print("Global x:", x)

print_global()

# Local Scope
def local_example():
    y = 20  # Local variable
    print("Local y:", y)

local_example()

# Modifying global variable
count = 0

def modify():
    global count
    count += 1

modify()
print("Modified global count:", count)

# ------------------------------------------------------
# 5. NESTED FUNCTIONS
# ------------------------------------------------------

def outer():
    msg = "Hello"

    def inner():
        print("Message from inner():", msg)

    inner()

outer()

# ------------------------------------------------------
# 6. LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ------------------------------------------------------

# Lambda functions are small anonymous functions defined with the `lambda` keyword

square = lambda x: x ** 2
print("Lambda square:", square(4))

# With multiple arguments
multiply = lambda a, b: a * b
print("Lambda multiply:", multiply(2, 5))

# Useful in sorting, filtering, mapping
nums = [5, 3, 8, 6]
nums_sorted = sorted(nums, key=lambda x: -x)
print("Sorted descending with lambda:", nums_sorted)

# ------------------------------------------------------
# 7. HIGHER-ORDER FUNCTIONS
# ------------------------------------------------------

# A function that takes another function as argument or returns a function

# map(): applies a function to every element
squared = list(map(lambda x: x ** 2, [1, 2, 3, 4]))
print("Map with lambda (squared):", squared)

# filter(): filters elements based on condition
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print("Filter with lambda (evens):", evens)

# reduce(): accumulates values (requires functools)
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print("Reduce with lambda (product):", product)

# ------------------------------------------------------
# 8. RECURSION
# ------------------------------------------------------

# A function that calls itself

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Recursive factorial of 5:", factorial(5))

# ------------------------------------------------------
# 9. DOCSTRINGS AND HELP
# ------------------------------------------------------

def square(x):
    """Returns the square of a number."""
    return x ** 2

print(square.__doc__)
help(square)

# ------------------------------------------------------
# 10. DECORATORS
# ------------------------------------------------------

# Decorators are functions that modify the behavior of other functions.
# They are often used for logging, access control, timing, etc.

# Basic decorator example
def decorator_func(original_func):
    def wrapper_func():
        print("Wrapper: Before calling the original function.")
        original_func()
        print("Wrapper: After calling the original function.")
    return wrapper_func

@decorator_func
def say_hello():
    print("Hello!")

say_hello()

# ------------------------------------------------------
# 11. GENERATORS
# ------------------------------------------------------

# Generators are a type of iterable, like lists or tuples.
# But unlike lists, they don’t store all values in memory at once.
# Instead, they yield items one by one — lazy evaluation.

# Creating a generator function using 'yield'
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
for num in count_up_to(5):
    print("Yielded:", num)

# Generator does not hold entire result in memory
gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # ❌ StopIteration

# Generator expressions: similar to list comprehension but with ()
squares = (x * x for x in range(5))
print("Squares from generator expression:")
for s in squares:
    print(s)

# Benefits:
# ✅ Memory efficient
# ✅ Can model infinite sequences
# ✅ Great for streaming data

# ------------------------------------------------------
# END OF FILE
# ------------------------------------------------------