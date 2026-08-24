# 18. WAP to remove same element from list of values from dictionary. 
# 1:[11,12,13,11,5,12],2:[‘a’,’b’,’a’,’c’} 

d = {1: [11,12,13,11,5,12], 2: ['a','b','a','c']}

for k in d:
    d[k] = list(set(d[k]))

print(d)
