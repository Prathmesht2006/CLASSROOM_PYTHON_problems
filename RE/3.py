import re

text = input("Enter a string: ")

# Extract only special characters
special_chars = re.findall(r"[^a-zA-Z0-9\s]", text)

print("Special symbols:", special_chars)
