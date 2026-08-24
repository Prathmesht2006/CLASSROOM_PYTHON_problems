# 11. WAP to filter a dictionary based on values 

d = {'a': 10, 'b': 20, 'c': 30}

filtered = {k: v for k, v in d.items() if v > 15}
print(filtered)
