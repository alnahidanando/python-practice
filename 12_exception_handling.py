# Exception Handling in Python

# try and except
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


# else
try:
    num = int(input("Enter another number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)


# finally
try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("This block always runs.")


# raise
age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")

print("Age:", age)
