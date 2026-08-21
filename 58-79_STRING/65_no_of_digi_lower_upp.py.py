t=input("enter text:")
digit=upper=lower=special=0

for i in t:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        digit+=1
    else:
        special+=1
    
print("digits: ",digit)
print("lower: ",lower)
print("upper: ",upper)
print("special: ",special)
 