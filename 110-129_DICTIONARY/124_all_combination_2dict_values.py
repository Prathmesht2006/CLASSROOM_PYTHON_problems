# 15. Write a Python program to create and display all combinations of letters, selecting each letter 
# from a different key in a dictionary. I/P  {'1':['a','b'], '2':['c','d']}  O/P  ac ad bc bd 

d = {'1': ['a', 'b'], '2': ['c', 'd']}

for i in d["1"]:
    for j in d["2"]:
        print(i+j,end=" ")