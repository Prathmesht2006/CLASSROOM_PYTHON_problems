import re

text = input("Enter a string: ")

# Find all integers in the string
numbers = re.findall(r"\d+", text)

# Convert to integer and filter even numbers
even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]

print("Even numbers:", even_numbers)
