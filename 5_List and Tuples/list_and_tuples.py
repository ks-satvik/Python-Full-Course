# ======================================================
# LISTS AND TUPLES IN PYTHON - COMPLETE EXPLANATION
# ======================================================

# ------------------------------------------------------
# 1. LISTS - DEFINITION, METHODS, MUTABILITY
# ------------------------------------------------------

# Lists are ordered, mutable (changeable), and allow duplicate elements
# Lists can contain elements of different data types

# Creating a list
my_list = [10, 20, 30, "Python", True]

print("Original List:", my_list)

# Indexing
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Slicing
print("Slice [1:4]:", my_list[1:4])

# Mutability - changing value at an index
my_list[2] = 99
print("After modification:", my_list)

# Nested list (2D list)
nested_list = [[1, 2], [3, 4]]
print("Nested List:", nested_list)
print("Access nested element:", nested_list[1][0])  # Output: 3

# List can be empty
empty_list = []
print("Empty List:", empty_list)

# ------------------------------------------------------
# 2. COMMON LIST METHODS
# ------------------------------------------------------

numbers = [1, 2, 3]

# append() - Adds item to the end
numbers.append(4)
print("After append:", numbers)

# insert() - Adds item at a specific index
numbers.insert(1, 10)
print("After insert at index 1:", numbers)

# extend() - Adds multiple items
numbers.extend([5, 6])
print("After extend:", numbers)

# remove() - Removes first occurrence of value
numbers.remove(10)
print("After remove 10:", numbers)

# pop() - Removes item at index (last by default)
last_item = numbers.pop()
print("After pop:", numbers)
print("Popped item:", last_item)

# index() - Finds index of first matching element
print("Index of 3:", numbers.index(3))

# count() - Counts how many times an item appears
print("Count of 3:", numbers.count(3))

# sort() - Sorts list in-place (modifies original)
numbers.sort()
print("Sorted list:", numbers)

# reverse() - Reverses list in-place
numbers.reverse()
print("Reversed list:", numbers)

# clear() - Removes all elements
copy_list = numbers.copy()
copy_list.clear()
print("Cleared list:", copy_list)

# len() - Gets number of elements
print("Length of original list:", len(numbers))

# 'in' keyword - Membership test
print("Is 3 in list?", 3 in numbers)

# copy for copying same list
list_1 = [1,2,3]
list_2 = list_1.copy()
list_2[0] = 100
print(list_1,list_2)

# max() and min()
print(max(list_1))
print(min(list_1))

# finding intersection / common element
a1 = [1,2,3,4]
a2 = [4,5,6,7]

s1 = set(a1)
s2 = set(a2)

s3 = s1.intersection(s2)
print(list(s3))
  
# ------------------------------------------------------
# 3. LIST COMPREHENSIONS (Advanced Shortcut)
# ------------------------------------------------------

# Create list of squares
squares = [x**2 for x in range(6)]
print("List of squares using list comprehension:", squares)

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)

# ------------------------------------------------------
# 4. TUPLES - DEFINITION, IMMUTABILITY
# ------------------------------------------------------

# Tuples are ordered, immutable collections
# They can contain different data types

# Creating a tuple
my_tuple = (1, 2, "Python", False)
print("Tuple:", my_tuple)

# Accessing elements (same as list)
print("First element:", my_tuple[0])
print("Slice [1:3]:", my_tuple[1:3])

# Tuple with one item requires a trailing comma
single_element_tuple = (42,)
print("Single-element tuple:", single_element_tuple)

# Tuples are immutable - can't be modified
# my_tuple[0] = 10  # ❌ TypeError

# Nested tuple
nested = ((1, 2), (3, 4))
print("Nested tuple:", nested)
print("Access nested:", nested[1][0])

# Tuple methods
t = (1, 2, 2, 3)
print("Count of 2:", t.count(2))
print("Index of 3:", t.index(3))

# ------------------------------------------------------
# 5. COMPARISON OF LISTS AND TUPLES
# ------------------------------------------------------

# Lists vs Tuples

# MUTABILITY
# Lists are mutable → elements can be changed
# Tuples are immutable → fixed after creation

# PERFORMANCE
# Tuples are faster than lists due to immutability

# USAGE
# Lists are used for collections that may change
# Tuples are used for fixed collections (e.g., coordinates, database rows)

# MEMORY
# Tuples use slightly less memory than lists

# Example:
sample_list = [1, 2, 3]
sample_tuple = (1, 2, 3)

print("List:", sample_list)
print("Tuple:", sample_tuple)

# ------------------------------------------------------
# END OF FILE
# ------------------------------------------------------