# Find numbers greater than specified number

lst = [10, 25, 5, 40, 15, 60]

num = int(input("Enter number: "))

result = []

for i in lst:
    if i > num:
        result.append(i)

print("Values greater than", num, "are:", result)