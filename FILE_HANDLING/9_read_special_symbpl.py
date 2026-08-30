import string

with open("file.txt", "r") as f:
    text = f.read()

for char in text:
    if char in string.punctuation:
        print(char)
