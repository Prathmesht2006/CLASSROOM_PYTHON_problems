list=[1,2,3,4,5,6,7]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        print(list[i],list[j])
        