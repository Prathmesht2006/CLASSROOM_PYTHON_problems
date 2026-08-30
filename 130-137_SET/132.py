# 3. Given two sets of numbers, write a Python program to find the missing numbers in the
# second set as compared to the first and vice versa

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Missing in set2:", set1 - set2)
print("Missing in set1:", set2 - set1)
