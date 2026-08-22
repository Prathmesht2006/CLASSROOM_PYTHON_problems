list1 = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
new_list = []

for i in list1:
    if i not in new_list:
        new_list.append(i)

print("After removing duplicates:", new_list)
