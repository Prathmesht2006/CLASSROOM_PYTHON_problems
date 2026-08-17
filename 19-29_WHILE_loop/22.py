# Prime number check using while loop

num = int(input("Enter a number: "))

flag=0
i=2
while i<num:
    if num%i==0:
        flag=1
        break
    i=i+1

if num == 1:
    print("Not Prime")
elif flag == 0:
    print("Prime Number")
else:
    print("Not Prime")