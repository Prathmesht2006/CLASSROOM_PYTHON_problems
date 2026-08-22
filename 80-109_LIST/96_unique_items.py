list1 = [1, 2, 2, 3, 4, 4, 5]
unique = []

for i in list1:
    if i not in unique:
        unique.append(i)

print("Unique values:", unique)
