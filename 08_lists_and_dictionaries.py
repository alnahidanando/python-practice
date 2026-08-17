# Lists and Dictionaries Together

tools = [
    {
        "name": "Calculator",
        "type": "math",
        "description": "Performs calculations"
    },
    {
        "name": "Search",
        "type": "web",
        "description": "Searches for information"
    },
    {
        "name": "File Reader",
        "type": "file",
        "description": "Reads files"
    }
]

print("Available Tools:")
print(tools)

print("\nTool Names:")

for tool in tools:
    print(tool["name"])

print("\nTool Details:")

for tool in tools:
    print("Name:", tool["name"])
    print("Type:", tool["type"])
    print("Description:", tool["description"])
    print()
