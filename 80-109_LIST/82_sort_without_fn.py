n=[10,9,8,7,6,5,4,3,2,1]
for i in range(0,len(n)-1):
    for j in range(0,len(n)-i-1):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]

print(n)