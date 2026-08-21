str="hello hello word hello word python"
str=str.split()
result=[]

for i in str:
    if i in result:
        continue
    else:
        result.append(i)


c=" ".join(result)
print(c)
