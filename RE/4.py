import re

name = input("Enter employee name: ")

# Only alphabets and spaces allowed, min 2 characters
if re.fullmatch(r"[A-Za-z ]{2,}", name):
    print("Valid Name")
else:
    print("Invalid Name")
