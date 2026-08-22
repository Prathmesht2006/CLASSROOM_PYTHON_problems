list=[1,2,3,4,5,4,3,2,6,7,8]
duplicates=[]

for i in list:
    if list.count(i)>1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)