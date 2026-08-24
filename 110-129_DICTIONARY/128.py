# 19. Write a Python program to find the key of the maximum value in a dictionary. 

d = {'a': 10, 'b': 50, 'c': 30}

for k in d:
    if d[k]==max(d.values()):
        print(k)

# print(max(d, key=d.get))
