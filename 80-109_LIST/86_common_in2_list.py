list1=[1,2,3,4,5,6,7,8,9]
list2=[1,2,3,4]
common=[]

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print(common)