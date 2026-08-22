list1 = [10, 25, 3, 45, 8]
smallest = list1[0]
largest = list1[0]

for i in list1:
    if i < smallest:
        smallest = i
    if i > largest:
        largest = i

print("Smallest:", smallest)
print("Largest:", largest)
