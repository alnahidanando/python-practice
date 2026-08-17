# Python Dictionaries

agent = {
    "name": "My AI Agent",
    "role": "Assistant",
    "language": "Python",
    "status": "Learning"
}

print("Agent Information:")
print(agent)

print("\nAgent Name:")
print(agent["name"])

print("\nAgent Role:")
print(agent["role"])

# Add a new property
agent["goal"] = "Learn AI Agents"

print("\nUpdated Agent:")
print(agent)

# Loop through dictionary
print("\nAgent Details:")
for key, value in agent.items():
    print(key, ":", value)
