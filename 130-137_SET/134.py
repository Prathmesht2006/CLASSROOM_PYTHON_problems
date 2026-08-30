# 5. Write a Python program to find the third largest number from a given set of numbers

s = {10, 40, 30, 20, 50}

lst = sorted(s, reverse=True)
print("Third largest:", lst[2])
