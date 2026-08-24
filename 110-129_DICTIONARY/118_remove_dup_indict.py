# 9. Write a Python program to remove duplicates from the dictionary 

d = {'a': 1, 'b': 2, 'c': 1,"a":4}

new_d = {}
for k,v in d.items():
    if k not in new_d.keys():
        new_d[k]=v

print(new_d)



