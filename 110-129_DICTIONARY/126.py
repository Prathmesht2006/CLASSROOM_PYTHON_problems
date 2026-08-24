# 17. Write a Python program to verify that all values in a dictionary are the same 
# {'a’: 12, ‘b': 12, ‘c’: 12}  Check all are 12 in the dictionary. True False 

d = {'a': 12, 'b': 12, 'c': 12}

print(len(set(d.values())) == 1)
#==================================

