 
# 6. WAP to match key values in two dictionaries. 

d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'c': 3}

# for k in d1:
#     if k in d2 and d1[k] == d2[k]:
#         print(k, "has same value")

# ==========or==========

for i in d1.items():
    if i in d2.items():
        print(i)


