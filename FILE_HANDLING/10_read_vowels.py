# Writing words
with open("file.txt", "w") as f:
    f.write("Hello Python Programming")

# Reading vowels
vowels = "aeiouAEIOU"

with open("file.txt", "r") as f:
    text = f.read()

for char in text:
    if char in vowels:
        print(char)
