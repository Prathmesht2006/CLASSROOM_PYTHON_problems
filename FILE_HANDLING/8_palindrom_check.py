def is_palindrome(s):
    return s == s[::-1]

with open("file.txt", "r") as f:
    data = f.read().split()

for item in data:
    if is_palindrome(item):
        print(item)
