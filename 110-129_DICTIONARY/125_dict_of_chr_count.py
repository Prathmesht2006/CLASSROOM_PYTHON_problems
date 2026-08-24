# 16. Write a Python program to create a dictionary from a string. i/p hello o/p : {‘h’:1,’e’:1,’l’:2…} 

s = "hello"
d = {}

for ch in s:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1

print(d)
