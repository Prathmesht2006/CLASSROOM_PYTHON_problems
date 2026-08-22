list=[[1,2,3],[4,5,6], [10,11,12], [7,8,9]]

max=[]
temp=0

for i in list:
    sum=0
    for j in i:
        sum+=j
    if sum>temp:
        temp=sum
        max=i

print(max)

