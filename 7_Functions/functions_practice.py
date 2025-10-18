#Q1. Write a funtion greet_user that asks the user for their name and then prints a personalized greeting using that name.

'''
def greet_users(name) :
    print("Hello Mr./Mrs.",name,", you are invited to my son Aditya's Birthday Party! ")

name1 = input("Enter your name: ")
greet_users(name1)

name2 = input("Enter your name: ")
greet_users(name2)
'''

#Q2. Return the area of a triangle - arguments length and width

'''
def calculate_rectangle_area(length,width):
    area = length*width
    return area

length1 = float(input("Enter Length :"))
width1 = float(input("Enter Width :"))

area1 = calculate_rectangle_area(length1,width1)
print("Area of the rectangle is :", area1)

'''

#Q3. Calculate Factorial

'''
def calculate_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

Number = int(input("Enter Number : "))
Factorial = calculate_factorial(Number)
print("The factorial of",Number,"is",Factorial)

'''   
 
#Q4. Write a function filter_even_numbers that takes a list of integers as an argument and returns a new list containing only the even numbers

def filter_even_numbers(numbers):
    even_nums = []
    for n in numbers:
        if n % 2 == 0:
            even_nums.append(n)
    return even_nums

nums = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter_even_numbers(nums)
print("Even numbers:", evenNumbers)




