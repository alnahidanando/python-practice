# Modules and Packages in Python

# 1. Import a complete module
import math

number = 25

print("Square root:", math.sqrt(number))
print("Power:", math.pow(2, 3))
print("Pi:", math.pi)


# 2. Import specific functions
from math import factorial

print("Factorial of 5:", factorial(5))


# 3. Random module
import random

random_number = random.randint(1, 100)

print("Random number:", random_number)


# 4. Datetime module
import datetime

today = datetime.date.today()

print("Today's date:", today)


# 5. Module alias
import math as m

print("Square root:", m.sqrt(49))


# 6. Creating your own module
# Create another file named mymodule.py
#
# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b
#
# Then use:
#
# import mymodule
#
# print(mymodule.add(10, 20))
# print(mymodule.multiply(5, 4))


# 7. Using a package
# A package is a folder containing Python modules.
#
# Example:
#
# mypackage/
#     __init__.py
#     calculator.py
#
# calculator.py:
#
# def add(a, b):
#     return a + b
#
# Then:
#
# from mypackage.calculator import add
#
# print(add(10, 20))
