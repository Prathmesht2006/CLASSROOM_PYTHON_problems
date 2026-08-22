list1 = [10, 20, 4, 45, 99]
smallest = list1[0]
second_smallest = list1[0]

for i in list1:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i != smallest and (second_smallest == smallest or i < second_smallest):
        second_smallest = i

print("Second smallest number:", second_smallest)
