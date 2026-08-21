chr=input("enter string:")
result=""

for i in chr:
    if i in result:
        continue
    else:
        result+=i

print(result)