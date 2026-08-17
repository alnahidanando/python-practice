name = "Al Nahid"
message = "I am learning Python for AI Agents"

print("Name:", name)
print("Message:", message)

print("First character:", name[0])
print("Last character:", name[-1])

print("First 7 characters:", name[:7])
print("From character 3:", name[3:])

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

text = "   Python is powerful   "
print("Without spaces:", text.strip())

sentence = "Python is easy to learn"
words = sentence.split()
print("Words:", words)

joined_text = "-".join(words)
print("Joined:", joined_text)

new_sentence = sentence.replace("easy", "fun")
print("Changed:", new_sentence)

age = 22
print(f"My name is {name} and I am {age} years old.")
