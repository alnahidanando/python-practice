# Tuple

student = ("Al Nahid", 22, "CSE")

print("Student:", student)
print("Name:", student[0])
print("Age:", student[1])
print("Department:", student[2])

print("Number of items:", len(student))


# Set

numbers = {10, 20, 30, 20, 10, 40}

print("Set:", numbers)

numbers.add(50)
print("After adding:", numbers)

numbers.remove(20)
print("After removing:", numbers)

print("Is 30 present?", 30 in numbers)


# Set operations

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
