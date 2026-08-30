# AP to check if two given sets have no elements in common

set1 = {1, 2, 3}
set2 = {4, 5, 6}

if set1.isdisjoint(set2):
    print("No common elements")
else:
    print("Common elements exist")
