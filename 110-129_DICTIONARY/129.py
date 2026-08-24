# 20. Write a Python program to find the key of the even value and should be greater than 25 in a dictionary
d = {'a': 10, 'b': 28, 'c': 40, 'd': 15}

for k, v in d.items():
    if v % 2 == 0 and v > 25:
        print(k)
