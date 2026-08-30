# WAP to remove an item from a set if it is present in the between two sets
set1 = [1, 2, 3, 4]
set2 = [3, 4, 5]
item = 3

if item in set1 and item in set2:
    set1.remove(item)
    set2.remove(item)

for i in set1:
    if i in set2:
        set1.remove(i)
        set2.remove(i)
    
print("Set1:", set1)
print("Set2:", set2)
