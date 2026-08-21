# Program to remove unwanted characters from string

string = "A%^!B#*CD"

result = ""

for ch in string:
    
    # Keep only alphabets and numbers
    if ch.isalnum():
        result = result + ch

print("Original String :", string)
print("Output String   :", result)