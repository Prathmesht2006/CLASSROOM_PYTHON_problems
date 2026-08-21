# Program to print distinct words in sorted order

string = "red, white, black, red, green, black"

# Split words using comma
words = string.split(",")

# Remove extra spaces
words = [word.strip() for word in words]

# Remove duplicates using set
distinct_words = set(words)

# Sort words alphabetically
sorted_words = sorted(distinct_words)

# Join words into string
result = ", ".join(sorted_words)

print("Input String :", string)
print("Expected Result :", result)