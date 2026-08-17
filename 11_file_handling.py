# Write to a file

file = open("notes.txt", "w")
file.write("Python is the foundation of AI development.\n")
file.write("I am learning Python to build AI Agents.")
file.close()


# Read from a file

file = open("notes.txt", "r")
content = file.read()
print("File content:")
print(content)
file.close()


# Append to a file

file = open("notes.txt", "a")
file.write("\nI will learn LLMs, RAG and AI Agents.")
file.close()


# Read line by line

file = open("notes.txt", "r")

for line in file:
    print("Line:", line.strip())

file.close()


# Using with statement

with open("notes.txt", "r") as file:
    content = file.read()
    print("Using with:")
    print(content)
