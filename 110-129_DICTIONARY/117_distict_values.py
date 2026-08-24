# 8. Write a Python program to print all distinct values in a dictionary. 

d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}

# temp=[]
# for i in d.values():
#     if i not in temp:
#         temp.append(i)

# print(temp)
#===============================

print(set(d.values()))
