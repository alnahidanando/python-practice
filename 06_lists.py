# Python Lists

tasks = [
    "Search Google",
    "Read a file",
    "Calculate result",
    "Send email"
]

print("All Tasks:")
print(tasks)

print("\nFirst Task:")
print(tasks[0])

print("\nNumber of Tasks:")
print(len(tasks))

# Add a new task
tasks.append("Call API")

print("\nAfter Adding New Task:")
print(tasks)

# Loop through tasks
print("\nTask List:")
for task in tasks:
    print("-", task)
