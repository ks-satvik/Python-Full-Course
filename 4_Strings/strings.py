# ======================================================
# NOTES ON STRINGS & CHARACTERS IN PYTHON
# With Explanations
# ======================================================

# ------------------------------------------------------
# 1. STRING CREATION
# ------------------------------------------------------
# Strings can be created using single, double, or triple quotes.
single = 'Single quotes'
double = "Double quotes"
triple_single = """Triple quoted string for multiline"""
print(single)
print(double)
print(triple_single)

# An empty string is a string with 0 characters
empty = ""
print("Empty string:", empty)

# Escape characters let you include special characters in a string
escaped = "She said, \"Hello!\""
newline = "First line \nSecond line"   # Newline escape
tabbed = "Column1\tColumn2"           # Tab escape

print(escaped)
print(newline)
print(tabbed)

# ------------------------------------------------------
# 2. STRINGS ARE IMMUTABLE
# ------------------------------------------------------
# Strings cannot be changed after they are created.
original = "hello"
# original[0] = "H"  # ❌ Error: Strings are immutable

# To modify, we create a new string
modified = "H" + original[1:]
print("Modified string:", modified)

# ------------------------------------------------------
# 3. CHARACTER ACCESS & INDEXING
# ------------------------------------------------------
# We can access characters in a string using indexing and loops.
text = "Python"
print("First character:", text[0])
print("Last character:", text[-1])

# Iterate through string
print("Characters in string:")
for ch in text:
    print(ch)

# Convert string to list of characters
char_list = list(text)
print("As list:", char_list)

# ASCII values and conversions
print("ASCII of 'A':", ord('A'))    # Converts character to ASCII
print("Char of 65:", chr(65))       # Converts ASCII to character

# len() can be used to find length 
print(len(text))

# ------------------------------------------------------
# 4. SLICING STRINGS
# ------------------------------------------------------
s = "KumarSatvik"
# Slicing gives substrings: [start:stop] (stop excluded)
print("s[0:5]:", s[0:5])      # Kumar
print("s[:5]:", s[:5])        # Same as above
print("s[5:]:", s[5:])        # Satvik
print("s[::2]:", s[::2])      # Every second character
print("s[::-1]:", s[::-1])    # Reversed string

# ------------------------------------------------------
# 5. CONCATENATION & REPETITION
# ------------------------------------------------------
# Strings can be joined (+) or repeated (*)
s1 = "Hello"
s2 = "World"
combined = s1 + " " + s2
print("Combined string:", combined)

repeated = "ha" * 4
print("Repeated string:", repeated)

# ------------------------------------------------------
# 6. STRING METHODS (TRANSFORMATION)
# ------------------------------------------------------
msg = "  welcome To PYTHON strings  "

# Case conversion
print("Uppercase:", msg.upper())
print("Lowercase:", msg.lower())
print("Title Case:", msg.title())
print("Capitalize first:", msg.capitalize())
print("Swap case:", msg.swapcase())

# Whitespace removal
print("Strip:", msg.strip())   # removes both ends
print("LStrip:", msg.lstrip()) # left only
print("RStrip:", msg.rstrip()) # right only

# ------------------------------------------------------
# 7. STRING METHODS (SEARCH & ANALYSIS)
# ------------------------------------------------------
print("Find 'PYTHON':", msg.find("PYTHON"))   # Returns index or -1
print("Index of 'To':", msg.index("To"))      # Similar to find but errors on not found
print("Count of 'o':", msg.count("o"))

# Start and end checks
print("Starts with 'welcome':", msg.strip().startswith("welcome"))
print("Ends with 's':", msg.endswith("s"))


# ------------------------------------------------------
# 8. STRING METHODS (VALIDATION)
# ------------------------------------------------------
# Useful to check the type of string content
print("'1234'.isdigit():", "1234".isdigit())
print("'abc'.isalpha():", "abc".isalpha())
print("'abc123'.isalnum():", "abc123".isalnum())
print("'   '.isspace():", "   ".isspace())
print("'Hello'.istitle():", "Hello".istitle())

# ------------------------------------------------------
# 9. STRING METHODS (MODIFICATION)
# ------------------------------------------------------
data = "banana,apple,mango"

# Splitting into a list
fruits = data.split(",")
print("Split:", fruits)

# Joining with delimiter
joined = " | ".join(fruits)
print("Joined:", joined)

# Replacing substrings
replaced = data.replace("apple", "grape")
print("Replace result:", replaced)

# Padding & aligning
print("'42'.zfill(5):", "42".zfill(5))            # Pads with zeros
print("'hi'.center(10, '-'):", "hi".center(10, '-'))  # Center align
print("'hi'.ljust(10, '*'):", "hi".ljust(10, '*'))     # Left align
print("'hi'.rjust(10, '.'):", "hi".rjust(10, '.'))     # Right align

# ------------------------------------------------------
# 10. STRING FORMATTING TECHNIQUES
# ------------------------------------------------------
name = "Satvik"
score = 99.56789

# Classic %-style
print("Old style: Name: %s, Score: %.2f" % (name, score))

# str.format method
print("Using format(): Name: {}, Score: {:.2f}".format(name, score))

# f-string (modern and best)
print(f"f-string: Name: {name}, Score: {score:.2f}")



# ------------------------------------------------------
# 11. ESCAPE SEQUENCES
# ------------------------------------------------------
print("Newline:\\nHello\\nWorld")  # Newline
print("Tab:\\tA\\tB")              # Tab
print("Backslash: C:\\\\Path")     # Backslash
print("Quotes: She said, \\\"Hello\\\"")  # Double quote inside

# ------------------------------------------------------
# 12. RAW STRINGS
# ------------------------------------------------------
# Raw strings ignore escape characters
raw_path = r"C:\\Users\\Satvik\\Desktop"
print("Raw path:", raw_path)

# ------------------------------------------------------
# END OF FILE
# ------------------------------------------------------