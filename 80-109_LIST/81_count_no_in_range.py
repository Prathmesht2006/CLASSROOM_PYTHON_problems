n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print("enter 2 nos(range):")
a=int(input())
b=int(input())

count=0
for i in n:
    if i in range(a,b+1):
        count+=1

print(count)