n=[1,2,3,1,2,4,5,6,3,4]
result=[]
for i in n:
    if i in result:
        continue
    else:
        result.append(i)

print(result)
    
