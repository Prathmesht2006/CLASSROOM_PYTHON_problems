# 12. Write a Python script to concatenate the following dictionaries to create a new one 

d1 = {'a': 1}
d2 = {'b': 2}
d3 = {'c': 3}

d = {}
for dic in (d1, d2, d3):
    d.update(dic)

print(d)
