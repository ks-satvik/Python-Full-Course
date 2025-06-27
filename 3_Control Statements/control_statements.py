# -------------------------------
# CONTROL STATEMENTS IN PYTHON
# -------------------------------

# Control statements manage the flow of execution in a program.
# They include: conditionals, loops, and loop control tools.

# -------------------------------
# 1. CONDITIONAL STATEMENTS (if, elif, else)
# -------------------------------

# Syntax:
# if condition:
#     code block
# elif another_condition:
#     code block
# else:
#     code block

x = 15

if x > 20:
    print("Greater than 20")
elif x == 15:
    print("Equal to 15")
else:
    print("Less than 20")

# -------------------------------
# 2. LOOP CONSTRUCTS (for, while)
# -------------------------------

# 2.1 FOR LOOP
# Used to iterate over a sequence (list, string, range, etc.)

for i in range(5):
    print("For loop iteration:", i)

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print("Name:", name)

# 2.2 WHILE LOOP
# Repeats as long as a condition is True

count = 0
while count < 3:
    print("While loop count:", count)
    count += 1

# -------------------------------
# 3. LOOP CONTROL STATEMENTS
# -------------------------------

# 3.1 BREAK - Exit the loop prematurely
for i in range(10):
    if i == 5:
        break
    print("Break at i =", i)

# 3.2 CONTINUE - Skip the current iteration
for i in range(5):
    if i == 2:
        continue
    print("Continue at i =", i)

# 3.3 PASS - Placeholder; does nothing
for i in range(3):
    pass  # To be implemented later

# -------------------------------
# 4. FLOW CONTROL CONCEPTS
# -------------------------------

# NESTED CONDITIONALS
age = 18
if age >= 18:
    if age < 60:
        print("Adult")
    else:
        print("Senior")
else:
    print("Minor")

# COMBINING CONDITIONS
num = 7
if num > 0 and num < 10:
    print("Single digit positive number")

# LOOPS WITH ELSE
# The 'else' block executes only if the loop completes normally (no break)

for i in range(3):
    print(i)
else:
    print("Loop finished without break")

for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This won't print because of break")
    

# ======================================================
# RANGE() FUNCTION IN PYTHON - FULL EXPLANATION
# ======================================================

# The range() function is used to generate a sequence of numbers.
# It is commonly used in for loops.

# ------------------------------------------------------
# SYNTAX: range(start, stop, step)
# ------------------------------------------------------
# - start: Starting value of the sequence (default is 0)
# - stop: End value (exclusive, meaning it stops BEFORE this number)
# - step: Increment value (default is 1)

# ------------------------------------------------------
# EXAMPLES
# ------------------------------------------------------

# 1. Only stop value
print("range(5):")
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# 2. Start and stop
print("\\nrange(2, 6):")
for i in range(2, 6):
    print(i)  # Output: 2, 3, 4, 5

# 3. Start, stop, and step
print("\\nrange(1, 10, 2):")
for i in range(1, 10, 2):
    print(i)  # Output: 1, 3, 5, 7, 9

# 4. Reverse counting using negative step
print("\\nrange(5, 0, -1):")
for i in range(5, 0, -1):
    print(i)  # Output: 5, 4, 3, 2, 1

# 5. Loop through list indices
print("\\nLoop through list using range(len(list)):")
my_list = ['a', 'b', 'c']
for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")

# ------------------------------------------------------
# QUICK USE CASES:
# ------------------------------------------------------
# range(10)           -> 0 to 9
# range(5, 16)        -> 5 to 15
# range(0, 10, 2)     -> Even numbers
# range(1, 10, 2)     -> Odd numbers
# range(10, 0, -1)    -> Reverse from 10 to 1

# ------------------------------------------------------
# NOTE:
# range() does not create a list in memory.
# It's a memory-efficient iterable.

# Convert to list if needed:
nums = list(range(5))
print("\\nConvert range to list:", nums)

# -------------------------------
# END OF FILE
# -------------------------------