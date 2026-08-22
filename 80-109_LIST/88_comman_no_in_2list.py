L1=[13,12,11]    
L2=[11,13,14] 
common=[]

for i in L1:
    if i in L2 and i not in common:
        common.append(i)



print(common)