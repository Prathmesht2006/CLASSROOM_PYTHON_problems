# 10. Write a Python program to drop empty elements(None) from a given dictionary 

d = {'a': 1, 'b': None, 'c': 3}

d = {k:v for k,v in d.items() if v is not None}
print(d)
