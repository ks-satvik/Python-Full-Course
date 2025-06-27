# -------------------------------
# OPERATORS IN PYTHON
# -------------------------------

# Python provides several categories of operators to perform operations on variables and values.

# -------------------------------
# 1. ARITHMETIC OPERATORS
# -------------------------------

a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponentiation:", a ** b) # 1000

# -------------------------------
# 2. RELATIONAL / COMPARISON OPERATORS
# -------------------------------

print("Equal to:", a == b)       # False
print("Not equal to:", a != b)   # True
print("Greater than:", a > b)    # True
print("Less than:", a < b)       # False
print("Greater or equal:", a >= b) # True
print("Less or equal:", a <= b)    # False

# -------------------------------
# 3. LOGICAL OPERATORS
# -------------------------------

x = True
y = False

print("AND:", x and y)           # False
print("OR:", x or y)             # True
print("NOT x:", not x)           # False

# -------------------------------
# 4. BITWISE OPERATORS
# -------------------------------

p = 5     # 0101 in binary
q = 3     # 0011 in binary

print("Bitwise AND:", p & q)     # 1 (0001)
print("Bitwise OR:", p | q)      # 7 (0111)
print("Bitwise XOR:", p ^ q)     # 6 (0110)
print("Bitwise NOT:", ~p)        # -6 (inverts all bits)
print("Left Shift:", p << 1)     # 10 (1010)
print("Right Shift:", p >> 1)    # 2 (0010)

# -------------------------------
# 5. ASSIGNMENT & AUGMENTED ASSIGNMENT OPERATORS
# -------------------------------

x = 10
x += 5     # Same as x = x + 5
print("x += 5:", x)              # 15

x -= 3     # x = x - 3
print("x -= 3:", x)              # 12

x *= 2     # x = x * 2
print("x *= 2:", x)              # 24

x /= 4     # x = x / 4
print("x /= 4:", x)              # 6.0

x %= 4     # x = x % 4
print("x %= 4:", x)              # 2.0

x **= 3    # x = x ** 3
print("x **= 3:", x)             # 8.0

x //= 2    # x = x // 2
print("x //= 2:", x)             # 4.0

# -------------------------------
# 6. MEMBERSHIP OPERATORS
# -------------------------------
# Used to test if a value is present in a sequence (like list, string, tuple)

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)       # True
print("grape" not in fruits)    # True

text = "hello world"
print("world" in text)          # True
print("hi" not in text)         # True

# -------------------------------
# 7. IDENTITY OPERATORS
# -------------------------------
# Used to compare memory locations of two objects

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)       # False (different objects in memory)
print(x is z)       # True (same memory reference)
print(x == y)       # True (same content)

print(x is not y)   # True
print(x is not z)   # False

# -------------------------------
# 8. TAKING INPUTS input()
# -------------------------------
# Used to take inputs and asigned to a variable

a = input("Enter a Number : ") 
b = input("Enter a Name : ")
c = "The age of " + b + " is " + a
print(type(b))
print(c)

# Writing a Program to add two numbers from the inputs given by the users
num_1 = int(input("Enter Number 1 : "))   # We did typecasting because if we don't, a will take input as string
num_2 = int(input("Enter Number 2 : "))
print(type(num_1))
ans = str(num_1 + num_2)
print("The sum of two given numbers are : " + ans)

# -------------------------------
# 9.Escape Sequences

'''
Common Escape Sequences are : 
-> \n : Newline
-> \t : Tab
-> \\ : Backslash
-> \" : Double Quotes
-> \' : Single Quotes
'''
# -------------------------------

# -------------------------------
# END OF FILE
# -------------------------------