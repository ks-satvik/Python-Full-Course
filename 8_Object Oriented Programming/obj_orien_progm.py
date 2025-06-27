# ======================================================
# OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON - DETAILED
# ======================================================

# ------------------------------------------------------
# 1. CORE CONCEPTS OF OOP
# ------------------------------------------------------

# OOP is a way of structuring programs so that properties and behaviors are bundled into objects.

# Key Pillars:
# Encapsulation – Restrict direct access to data using methods/properties
# Inheritance – Reuse code via parent-child class relationship
# Polymorphism – Use the same interface for different underlying types
# Abstraction – Hide internal implementation; only expose functionality

# Benefits:
# - Cleaner code organization
# - Code reuse via inheritance
# - Modular, scalable applications

# ------------------------------------------------------
# 2. CLASSES AND OBJECTS
# ------------------------------------------------------

# Class: A blueprint
# Object: An instance of a class

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")

# Create object
s1 = Student("Satvik", 101)
s2 = Student("Aarav", 102)

s1.display()
s2.display()

# ------------------------------------------------------
# 3. INSTANCE VS CLASS ATTRIBUTES
# ------------------------------------------------------

class Example:
    class_attr = "Shared across all instances"  # Class variable

    def __init__(self, value):
        self.value = value  # Instance variable

e1 = Example(5)
e2 = Example(10)

print(e1.class_attr, e1.value)
print(e2.class_attr, e2.value)

# ------------------------------------------------------
# 4. TYPES OF METHODS
# ------------------------------------------------------

class Demo:
    class_var = "class-level"

    def instance_method(self):
        return "This is an instance method"

    @classmethod
    def class_method(cls):
        return f"This is a class method accessing {cls.class_var}"

    @staticmethod
    def static_method():
        return "This is a static method (no access to class or instance)"

d = Demo()
print(d.instance_method())
print(Demo.class_method())
print(Demo.static_method())

# ------------------------------------------------------
# 5. ENCAPSULATION AND ACCESS MODIFIERS
# ------------------------------------------------------

# Access Modifiers:
# - public: default
# - protected: _single_leading_underscore
# - private: __double_leading_underscore

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner              # public
        self._balance = balance         # protected
        self.__pin = "1234"             # private

    def show_balance(self):
        print(f"{self.owner}'s balance is {self._balance}")

    def __show_pin(self):
        print("Accessing private method: PIN is", self.__pin)

acct = BankAccount("Satvik", 10000)
acct.show_balance()
# acct.__show_pin()  # ❌ Will raise AttributeError

# Access private manually (not recommended)
print(acct._BankAccount__pin)

# ------------------------------------------------------
# 6. INHERITANCE (SINGLE AND MULTILEVEL)
# ------------------------------------------------------

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):  # Single Inheritance
    def bark(self):
        print("Dog barks")

class Puppy(Dog):   # Multilevel Inheritance
    def weep(self):
        print("Puppy weeps")

p = Puppy()
p.eat()
p.bark()
p.weep()

# ------------------------------------------------------
# 7. MULTIPLE INHERITANCE
# ------------------------------------------------------

class Father:
    def bike(self):
        print("Father rides bike")

class Mother:
    def cook(self):
        print("Mother cooks")

class Child(Father, Mother):
    def study(self):
        print("Child studies")

c = Child()
c.bike()
c.cook()
c.study()

# ------------------------------------------------------
# 8. METHOD OVERRIDING & MRO (Method Resolution Order)
# ------------------------------------------------------

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(B):
    def show(self):
        super().show()  # Calls method from B (next in MRO)
        print("C")

c = C()
c.show()

print(C.mro())  # Shows the order of resolution

# ------------------------------------------------------
# 9. POLYMORPHISM – DUCK TYPING
# ------------------------------------------------------

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

def call_speak(animal):
    animal.speak()

call_speak(Cat())
call_speak(Dog())

# ------------------------------------------------------
# 10. ABSTRACTION WITH ABC
# ------------------------------------------------------

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

c = Circle(5)
print("Area of circle:", c.area())

# ------------------------------------------------------
# 11. COMPOSITION – "HAS-A" Relationship
# ------------------------------------------------------

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def drive(self):
        self.engine.start()
        print("Car is moving")

car = Car()
car.drive()

# ------------------------------------------------------
# 12. REAL-WORLD APPLICATIONS OF OOP
# ------------------------------------------------------

# - Banking system: Account, Customer, ATM classes
# - Game development: Player, Enemy, Obstacle classes
# - School system: Student, Teacher, Subject classes
# - Web app backend: Models, Views, Controllers (Django MVC)
# - GUI programming: Windows, Buttons, Events as objects

# ------------------------------------------------------
# END OF FILE
# ------------------------------------------------------